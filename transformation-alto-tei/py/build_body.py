from lxml import etree


def body(root, data):
    text = etree.SubElement(root, "text")
    body = etree.SubElement(text, "body")
    div = etree.SubElement(body, "div")
    opener = etree.SubElement(div, "opener")
    header = None
    title = None
    dateline = None
    salute = None
    annotations = None
    closer = None
    postscriptsigned = None
    
    last_element = div[-1]
    lastCloserElt = None
    
    # On assigne un booléen pour délimiter le opener
    zoneOpener = True
    zoneMain = False
    zoneCloser = False
    
    for index, line in enumerate(data):
        # On écrit un pb si le numéro de la ligne est 1
        if int(line.n) == 1:
            pb = etree.Element("pb", corresp=f"#{line.page_id}")
            # Si le dernier élément est un fw
            if last_element.tag != "fw":
                # On teste si le dernier élément a des enfants
                try:
                    # Si oui, on ajoute le pb au dernier enfant
                    last_element.getchildren()[-1].append(pb)
                    # Si le dernier élément est un fw
                except:
                    # Sinon on l'ajoute à la div
                    last_element.append(pb)
            else:
                div.append(pb)
            last_element = div[-1]
        
        # prepare attributes for the text block's zone
        zone_atts = {"corresp": f"#{line.zone_id}", "type": line.zone_type}
        # prepare <lb/> with this line's xml:id as @corresp
        lb = etree.Element("lb", corresp=f"#{line.id}")
        # Contenu des lignes de texte
        lb.tail = f"{line.text}"

        # NumberingZone, QuireMarksZone, and RunningTitleZone line
        if line.zone_type == "NumberingZone" or line.zone_type == "RunningTitleZone":
            # enclose any page number, quire marks, or running title inside a <fw>

            # Si le dernier élément n'est pas un fw
            if last_element.tag != "fw":
                fw = etree.Element("fw", zone_atts)
                fw.append(lb)
                last_element.addnext(fw)
                last_element = div[-1]
                comment = etree.Comment("Vérifier que le numéro corresponde à la lettre et mettre à jour le type : "
                                        "pageNum si numéro de page, letterNum si numéro de lettre")
                fw.append(comment)
            # Si le dernier élément est un fw
            else:
                last_element.append(lb)

        # MarginTextZone
        elif line.zone_type == "MarginTextZone":
            # create a <note> if one is not already the preceding sibling
            if last_element.tag != "note":
                note = etree.Element("note", zone_atts)
                note.append(lb)
                comment = etree.Comment("Vérifier que la note corresponde à la lettre et mettre à jour le type")
                note.append(comment)
                div.append(note)
                last_element = div[-1]
            else:
                last_element.append(lb)
        
        # Pour les autres types de zones
        else:
            # Si on rencontre une DefaultLine, c'est que le opener est terminé
            if line.line_type == "DefaultLine":
                zoneOpener = False
                zoneMain = True
            
            # Si on rencontre une signature, c'est que l'on commence le closer
            if line.line_type == "CustomLine:signature" and not last_element.tag == "postscript":
                zoneOpener = False
                zoneMain = False
                zoneCloser = True
            # Cas rare d'une signature dans un post-scriptum
            elif line.line_type == "CustomLine:signature" and last_element.tag == "postscript":
                if postscriptsigned is None:
                    signed = etree.Element("signed")
                    signed.append(lb)
                    last_element.append(signed)
                else:
                    signed.append(lb)
                
            if zoneOpener:
                # Header
                if line.line_type in "CustomLine:header":
                    if header is None:
                        header = etree.SubElement(opener, "fw")
                        header.set("type", "letterhead")
                    header.append(lb)
                # Titre
                if line.line_type in "HeadingLine:title":
                    if title is None:
                        title = etree.SubElement(opener, "title")
                    title.append(lb)
                # Dateline
                if line.line_type in "CustomLine:dateline":
                    if dateline is None:
                        dateline = etree.SubElement(opener, "dateline")
                    dateline.append(lb)
                # Salute
                if line.line_type in "CustomLine:salute":
                    if salute is None:
                        salute = etree.SubElement(opener, "salute")
                    salute.append(lb)
                # Notes
                if line.line_type in "CustomLine:annotations":
                    if annotations is None:
                        annotations = etree.SubElement(opener, "note")
                    annotations.append(lb)
                # TODO poser des resp et construire des éléments handNote
                # On met à jour le dernier enfant de la div
                last_element = div[-1]
            
            # CORPS DE LA LETTRE
            elif zoneMain:
                # On réinitialise les variables d'éléments
                annotations = None
                
                # Corrections interlinéaires
                if line.line_type == "InterlinearLine":
                    comment = etree.Comment("Correction interlinéaire")
                    choice = etree.Element("choice")
                    choice.append(comment)
                    corr = etree.SubElement(choice, "corr")
                    corr.append(lb)
                    # Pour ajouter une correction à la fin d'un vers
                    if last_element.getchildren()[-1].tag == "l":
                        last_element.getchildren()[-1].append(choice)
                    # Pour ajouter une correction dans un paragraphe
                    else:
                        last_element.append(choice)
                # Vers
                elif line.line_type == "CustomLine:verse":
                    # Si le vers est précédé d'un paragraphe
                    if last_element.tag == "p":
                        # On crée un élément lg
                        lg = etree.SubElement(last_element, "lg")
                        l = etree.SubElement(lg, "l")
                        l.append(lb)
                        lg.append(l)
                        div.append(lg)
                        last_element = div[-1]
                    elif last_element.tag == "lg":
                        l = etree.SubElement(lg, "l")
                        l.append(lb)
                        lg.append(l)
                    elif last_element.tag == "postscript":
                        # Si le vers est précédé d'un paragraphe
                        if last_postscript_elt.tag == "p":
                            # On crée un élément lg
                            lg = etree.SubElement(last_element, "lg")
                            l = etree.SubElement(lg, "l")
                            l.append(lb)
                            lg.append(l)
                            postscript.append(lg)
                            last_postscript_elt = postscript[-1]
                        elif last_postscript_elt.tag == "lg":
                            l = etree.SubElement(lg, "l")
                            l.append(lb)
                            lg.append(l)
                # Pour les autres types de lignes
                else:
                    # On instancie un premier p avec la première ligne DefaultLine ou après une partie versifiée
                    # ou après un saut de page
                    if last_element.tag != "p" and last_element.tag != "closer":
                        p = etree.SubElement(div, "p")
                        p.append(lb)
                        last_element = div[-1]
                    elif last_element.tag == "p":
                        
                        last_element.append(lb)
                    # Post-scriptum
                    elif last_element.tag == "closer":
                        postscript = etree.SubElement(div, "postscript")
                        p = etree.SubElement(postscript, "p")
                        p.append(lb)
                        last_element = div[-1]
                        last_postscript_elt = postscript[-1]
                        
            # CLOSER
            elif zoneCloser:
                if closer is None:
                    closer = etree.SubElement(div, "closer")
                    last_element = div[-1]
               
                # Un closer ne peut commencer que par une signature
                if lastCloserElt is None:
                    signed = etree.SubElement(closer, "signed")
                    signed.append(lb)
                    closer.append(signed)
                    lastCloserElt = closer[-1]
                # Si le closer possède déjà des lignes
                else:
                    signed.append(lb)
                
           

        """
        # NumberingZone, QuireMarksZone, and RunningTitleZone line
        if line.zone_type == "NumberingZone" \
            or line.zone_type == "QuireMarksZone" or line.zone_type == "RunningTitleZone":
            # enclose any page number, quire marks, or running title inside a <fw>
            type = last_element.xpath("@type")
            if type:
                type = type[0]
            # Si le dernier élément n'est pas un fw ou si le type est différent
            if last_element.tag != "fw" or type != line.zone_type:
                fw = etree.Element("fw", zone_atts)
                last_element.addnext(fw)
                fw.append(lb)
            # Si le dernier élément est un fw ou si le type est le même
            else:
                last_element.append(lb)
        """
        """
        
        """
        """
        # MainZone line
        elif line.zone_type == "MainZone":
            # On récupère le type du dernier élément
            type = last_element.xpath("@type")
            if type:
                type = type[0]
            # Si le dernier élément n'est pas un ab ou si le type est différent
            if last_element.tag != "ab" or type != line.zone_type:
                # On crée un nouvel élément ab
                ab = etree.Element("ab", zone_atts)
                last_element.addnext(ab)
                # On actualise le dernier élément
                last_element = div[-1]

            
           # if the line is not emphasized, append it to the last element in the <ab>
            else:
                last_element.append(lb)
        """
    # Encoder le closer
