import os
import json
from lxml import etree
from bs4 import BeautifulSoup
from spellchecker import SpellChecker
from constantes import XMLaCORRIGER, DICTCDS, DICTGENERAL, DICTPAGES, VERITESTERRAIN as VT


def get_lemmes():
    """
    Cette fonction parse le contenu des vérités de terrain et retourne un set des mots qu'elles contiennent.
    :returns: mots contenus dans les vérités de terrain.
    :return type: set
    """
    ponctuation = ",;':!.()"
    chiffres = "1234567890"
    motsParses = []
    # On boucle sur chaque fichier contenu dans le dossier des vérités de terrain
    for root, dirs, files in os.walk(VT):
        for filename in files:
            # On pose comme condition de ne traiter que des fichiers XML (le dossier contient aussi des images)
            if filename[-3] == "xml":
                # On ouvre le fichier
                with open(VT + filename) as f:
                    xml = etree.parse(f)
                racine = xml.getroot()
                nsmap = {'alto': "http://www.loc.gov/standards/alto/ns-v4#"}
                textes = xml.xpath("//alto:String/@CONTENT", namespaces=nsmap)
                for ligne in textes:
                    # On nettoie le texte de sa ponctuation
                    for signe in ponctuation:
                        ligne = ligne.replace(signe, " ").replace("  ", " ")
                    # On nettoie le texte de sa ponctuation
                    for signe in chiffres:
                        ligne = ligne.replace(signe, " ").replace("  ", " ")
                    mots = ligne.split(' ')
                    for mot in mots:
                        # On verifie que le mot ne soit pas vide et pas césuré
                        if mot and mot[-1] != '-':
                            motsParses.append(mot)
    
    # On convertit les mots récoltés en set pour éliminer les doublons et on ajoute les nouveaux au set lemmes
    motsParses = set(motsParses)
    return motsParses


def suppress_punctuation(text):
    """ Suppress punctuation in a text
    
    :param text str: Text to clean up
    :returns: Text without punctuation
    :rtype: str
    """
    punctuation = "!:;\",?'’."
    for sign in punctuation:
        text = text.replace(sign, " ")
    return text

# TODO poser un décorateur click
def spellcheck_texts_page_XML():
    """
    - author: Floriane Chiffoleau
    - date: February 2021
    - description: Recovering orthographic errors in PAGE XML files
    - input: PAGE XML files
    - output: Python dictionnaries
    - usage :
        ======
        python name_of_this_script.py arg1 arg2 arg3
    
        arg1: folder of the PAGE XML files
        arg2: folder for the Python dictionnaries
        arg3: local dictionary adapted to the content's language of the PAGE XML
    
    """
    # On charge le dictionnaire local dans un fichier Json pour pouvoir le passer à SpellChecker
    spell = SpellChecker(language=None, local_dictionary=DICTGENERAL, case_sensitive=True)
    # With 'case_sensitive=True', we precise that all the words are processed as they are written in the text
    # This means that all the uppercase words will be considered wrong but that helps correct them
    # To use that technique, we have to call a local dictionary
    
    # On charge le contenu du dictionnaire dictCDS
    with open(DICTCDS) as jsonf:
        dictCDS = json.load(jsonf)
    
    for root, dirs, files in os.walk(XMLaCORRIGER):
        for filename in files:
            dictionary = {}
            # On ouvre le fichier XML d'entrée
            
            xml = etree.parse(XMLaCORRIGER + filename)
            print("Le fichier " + XMLaCORRIGER + filename + " est en cours de lecture.")
            # TODO renvoyer un message d'erreur explicite si le format de XML n'est pas Page (ou gérer aussi Alto)
            nsmap = {'page': "http://schema.primaresearch.org/PAGE/gts/pagecontent/2019-07-15"}
            tous_unicode = xml.xpath("//page:Unicode", namespaces=nsmap)
            
            for unicode in tous_unicode:
                content = unicode.text
                # Les traitements ne peuvent avoir lieu que si le contenu n'est pas vide
                if content:
                    content = suppress_punctuation(content)
                    
                    words = content.split(" ")
                    # On boucle sur chaque mot de l'élément Unicode courant
                    for index, mot in enumerate(words):
                        contexte = content.replace(mot, mot.upper())
                        # On cherche chaque mot dans les lemmes des vérités de terrain
                        if mot not in get_lemmes():
                            # On cherche chaque mot dans le dictCDS
                            if dictCDS.get(mot):
                                # On vérifie que la solution ne soit pas ambiguë (id est qu'il existe bien un lemme)
                                # et qu'il n'ait pas déjà été ajouté au dictionnaire de page
                                if dictCDS[mot].get('lem') and mot not in dictionary.keys():
                                    # On écrit l'entrée du dictionnaire pour préciser le contexte
                                    dictionary[mot] = {
                                        'lem': dictCDS[mot]['lem'],
                                        'ctxt': contexte.replace("'", ' '),
                                        'deja utilisé': dictCDS[mot]['ctxt']
                                    }
                                elif not dictCDS[mot].get('lem') and mot not in dictionary.keys():
                                    dictionary[mot] = {
                                        'lem': dictCDS[mot]['lem'],
                                        'remarque': "déjà marqué comme AMBIGU"
                                    }
                            # On cherche les mots dans dictionnaireComplet grâce à la fonction spell
                            elif spell.unknown(mot) and mot not in dictionary.keys():
                                # On écrit l'entrée du dictionnaire pour préciser le contexte
                                dictionary[mot] = {
                                    'lem': spell.correction(mot),
                                    'ctxt': contexte.replace("'", ' ')
                                }
                            # S'il n'a aucune proposition de correction identifiée
                            elif mot not in dictionary.keys():
                                dictionary[mot] = {
                                    'lem': None,
                                    'ctxt': contexte.replace("'", ' ')
                                }
            
            # On écrit le résultat dans un fichier de sortie au format .py
            with open(DICTPAGES.strip() + "page_" + filename.replace(".xml", ".json"), "w") as jsonf:
                json.dump(dictionary, jsonf, indent=3, ensure_ascii=False, sort_keys=False)
                print(f"=> Le dictionnaire {DICTPAGES.strip() + 'page_' + filename.replace('.xml', '.json')}"
                      f" a été écrit correctement.\n")

spellcheck_texts_page_XML()