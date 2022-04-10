import json

dictPage = {'18':
	{'lem': None, 'ctxt': '18'},
 'bain':
	{'lem': None, 'ctxt': 'Il fait si BAIN  Monsieur  que je peuse que Me papp  vers'},
 '':
	{'lem': None, 'ctxt': '(rr p  p )'},
 'peuse':
	{'lem': 'pense',
	 'ctxt': 'Il fait si bain  Monsieur  que je PEUSE que Me papp  vers',
	 'deja utilisé': ['il fait si bain, Monsieur, que je PENSE que MME papp, vers']},
 'Me':
	{'lem': 'Mme',
	 'ctxt': 'Il fait si bain  Monsieur  que je peuse que ME papp  vers',
	 'deja utilisé': ['il fait si bain, Monsieur, que je peuse que MME papp, vers']},
 'papp':
	{'lem': None, 'ctxt': 'Il fait si bain  Monsieur  que je peuse que Me PAPP  vers'},
 'vers':
	{'lem': None, 'ctxt': 'Il fait si bain  Monsieur  que je peuse que Me papp  VERS'},
 'Loutu':
	{'lem': 'Louise',
	 'ctxt': 'LOUTU et le grans fel pourriuz venir à pêed ou en voiture passer',
	 'deja utilisé': ['LOUISE et le grans fel pourriuz venir à pêed ou en voiture passer']},
 'grans':
	{'lem': 'grand', 'ctxt': 'Loutu et le GRANS fel pourriuz venir à pêed ou en voiture passer'},
 'fel':
	{'lem': 'fils', 'ctxt': 'Loutu et le grans FEL pourriuz venir à pêed ou en voiture passer'},
 'pourriuz':
	{'lem': 'pourriez',
	 'ctxt': 'Loutu et le grans fel POURRIUZ venir à pêed ou en voiture passer',
	 'deja utilisé': []},
 'pêed':
	{'lem': 'pied', 'ctxt': 'Loutu et le grans fel pourriuz venir à PÊED ou en voiture passer'},
 'voiture':
	{'lem': None, 'ctxt': 'Loutu et le grans fel pourriuz venir à pêed ou en VOITURE passer'},
 'journé':
	{'lem': 'journée',
	 'ctxt': 'la JOURNÉ arec vous c est dit ou la Kermesse  pois vrous promner',
	 'deja utilisé': ["la JOURNEE arec vous c'est dit ou la Kermesse, pois vrous promner"]},
 'arec':
	{'lem': 'avec',
	 'ctxt': 'la journé AREC vous c est dit ou la Kermesse  pois vrous promner',
	 'deja utilisé': ["la journée AVEC vous c'est dit ou la Kermesse, pois vrous promner"]},
 'Kermesse':
	{'lem': 'Kermesse',
	 'ctxt': 'la journé arec vous c est dit ou la KERMESSE  pois vrous promner',
	 'deja utilisé': ['la journé arec vous c&#39;est dit ou la KERMESSE, pois vrous promner']},
 'pois':
	{'lem': None, 'ctxt': 'la journé arec vous c est dit ou la Kermesse  POIS vrous promner'},
 'vrous':
	{'lem': 'vous', 'ctxt': 'la journé arec vous c est dit ou la Kermesse  pois VROUS promner'},
 'promner':
	{'lem': 'promener',
	 'ctxt': 'la journé arec vous c est dit ou la Kermesse  pois vrous PROMNER',
	 'deja utilisé': ["la journée vous c'est dit ou la Kermesse, pois vrous PROMENER"]},
 'cot':
	{'lem': None, 'ctxt': 'de ce COT vuis enteudrons les vuotous  et c est toujours quelque'},
 'vuis':
	{'lem': None, 'ctxt': 'de ce cot VUIS enteudrons les vuotous  et c est toujours quelque'},
 'enteudrons':
	{'lem': 'entendrons',
	 'ctxt': 'de ce cot vuis ENTEUDRONS les vuotous  et c est toujours quelque',
	 'deja utilisé': ["de ce côté ; nous ENTENDRONS les vuotous, et c'est toujours quelque"]},
 'vuotous':
	{'lem': 'violons', 'ctxt': 'de ce cot vuis enteudrons les VUOTOUS  et c est toujours quelque'},
 'toujours':
	{'lem': None, 'ctxt': 'de ce cot vuis enteudrons les vuotous  et c est TOUJOURS quelque'},
 '(os':
	{'lem': None, 'ctxt': '(OS que de vor la pie '},
 'vor':
	{'lem': None, 'ctxt': '(os que de VOR la pie '},
 'pie':
	{'lem': None, 'ctxt': '(os que de vor la PIE '},
 'conterai':
	{'lem': None, 'ctxt': 'Je CONTERAI vre commssions à Louse   il me faut mille'},
 'vre':
	{'lem': None, 'ctxt': 'Je conterai VRE commssions à Louse   il me faut mille'},
 'commssions':
	{'lem': 'commissions', 'ctxt': 'Je conterai vre COMMSSIONS à Louse   il me faut mille'},
 'Louse':
	{'lem': 'Louise',
	 'ctxt': 'Je conterai vre commssions à LOUSE   il me faut mille',
	 'deja utilisé': ['Je conterai vre commssions à LOUISE ; il me faut mille']},
 'Metles':
	{'lem': 'petites',
	 'ctxt': 'METLES chosés de Crane1s ',
	 'deja utilisé': ['PETITES chosés de Crane1s.']},
 'chosés':
	{'lem': 'choses', 'ctxt': 'Metles CHOSÉS de Crane1s '},
 'Crane1s':
	{'lem': None,
	 'ctxt': 'Metles chosés de CRANE1S '},
 'Vene':
	{'lem': 'Venez',
	 'ctxt': 'VENE donc ous  J emtrgse les drmes et vplue les messours',
	 'deja utilisé': ['VENEZ donc ous. J&#39;emtrgse les drmes et vplue les messours']},
 'ous':
	{'lem': None, 'ctxt': 'Vene donc OUS  J emtrgse les drmes et vplue les messours'},
 'emtrgse':
	{'lem': None, 'ctxt': 'Vene donc ous  J EMTRGSE les drmes et vplue les messours'},
 'drmes':
	{'lem': 'dames', 'ctxt': 'Vene donc ous  J emtrgse les DRMES et vplue les messours'},
 'vplue':
	{'lem': None, 'ctxt': 'Vene donc ous  J emtrgse les drmes et VPLUE les messours'},
 'messours':
	{'lem': 'messieurs', 'ctxt': 'Vene donc ous  J emtrgse les drmes et vplue les MESSOURS'},
 'Mor':
	{'lem': 'Mr',
	 'ctxt': 'A MOR Pruu ha aehae deLdberg)',
	 'deja utilisé': ['A MR Prons ha aehae de Liedberg)']},
 'Pruu':
	{'lem': 'Prons',
	 'ctxt': 'A Mor PRUU ha aehae deLdberg)',
	 'deja utilisé': ['A Mr PRONS ha aehae de Liedberg)']},
 'ha':
	{'lem': None, 'ctxt': 'A Mor Pruu HA aeHAe deLdberg)'},
 'aehae':
	{'lem': None, 'ctxt': 'A Mor Pruu ha AEHAE deLdberg)'},
 'deLdberg)':
	{'lem': 'de Liedberg)',
	 'ctxt': 'A Mor Pruu ha aehae DELDBERG)',
	 'deja utilisé': ['A Mr Prons ha aehae DE LIEDBERG)']},
 '15':
	{'lem': None, 'ctxt': 'Dyck  le 15 Salembiezt '},
 'Salembiezt':
	{'lem': 'Septembre',
	 'ctxt': 'Dyck  le 15 SALEMBIEZT ',
	 'deja utilisé': ['Dyck, le 15 SEPTEMBRE.']},
 '(Signé)':
	{'lem': '(Signé)',
	 'ctxt': '(SIGNÉ) J 2e 2 ',
	 'deja utilisé': ['(SIGNÉ) J 2e 2.']},
 '2e':
	{'lem': None, 'ctxt': '(Signé) J 2E 2 '},
 '2':
	{'lem': None, 'ctxt': 'asn surtont que ma ve puisse 2 y agitez librement vous avrez'},
 '1816':
	{'lem': None, 'ctxt': 'Dyck  le je Saroibre  1816 '},
 'LdSalm4':
	{'lem': 'de Salm)',
	 'ctxt': 'LDSALM4'},
 'Salm)':
	{'lem': 'Salm)',
	 'ctxt': 'd SALM)',
	 'deja utilisé': ['d SALM)']},
 'fnez':
	{'lem': None, 'ctxt': 'FNEZ vous ahez fon  Monseur  nour remstes à le cier Louire le'},
 'ahez':
	{'lem': 'assez', 'ctxt': 'fnez vous AHEZ fon  Monseur  nour remstes à le cier Louire le'},
 'fon':
	{'lem': 'bon', 'ctxt': 'fnez vous ahez FON  Monseur  nour remstes à le cier Louire le'},
 'Monseur':
	{'lem': 'Monsieur',
	 'ctxt': 'fnez vous ahez fon  MONSEUR  nour remstes à le cier Louire le',
	 'deja utilisé': ['fnez vous ahez fon, MONSIEUR, nour remstes à le cier Louise le']},
 'nour':
	{'lem': None, 'ctxt': 'fnez vous ahez fon  Monseur  NOUR remstes à le cier Louire le'},
 'remstes':
	{'lem': 'remettre', 'ctxt': 'fnez vous ahez fon  Monseur  nour REMSTES à le cier Louire le'},
 'cier':
	{'lem': 'cher', 'ctxt': 'fnez vous ahez fon  Monseur  nour remstes à le CIER Louire le'},
 'Louire':
	{'lem': 'Louise',
	 'ctxt': 'fnez vous ahez fon  Monseur  nour remstes à le cier LOUIRE le',
	 'deja utilisé': ['fnez vous ahez fon, Monsieur, nour remstes à le cier LOUISE le']},
 'marieu':
	{'lem': None, 'ctxt': 'MARIEU de gros de saples jaune c jout j aui dire que je déproais en'},
 'gros':
	{'lem': None, 'ctxt': 'marieu de GROS de saples jaune c jout j aui dire que je déproais en'},
 'saples':
	{'lem': 'Naples', 'ctxt': 'marieu de gros de SAPLES jaune c jout j aui dire que je déproais en'},
 'jaune':
	{'lem': None, 'ctxt': 'marieu de gros de saples JAUNE c jout j aui dire que je déproais en'},
 'jout':
	{'lem': 'joint', 'ctxt': 'marieu de gros de saples jaune c JOUT j aui dire que je déproais en'},
 'aui':
	{'lem': None, 'ctxt': 'marieu de gros de saples jaune c jout j AUI dire que je déproais en'},
 'déproais':
	{'lem': None, 'ctxt': 'marieu de gros de saples jaune c jout j aui dire que je DÉPROAIS en'},
 'aune':
	{'lem': None, 'ctxt': 'avoir une AUNE de Brabant  de pareit   Mais il faut qu il soit bien'},
 'Brabant':
	{'lem': 'Brabant',
	 'ctxt': 'avoir une aune de BRABANT  de pareit   Mais il faut qu il soit bien',
	 'deja utilisé': ['avoir une aune de BRABANT, de pareit ? Mais il faut qu&#39;il soit bien']},
 'pareit':
	{'lem': 'pareil', 'ctxt': 'avoir une aune de Brabant  de PAREIT   Mais il faut qu il soit bien'},
 'semblable':
	{'lem': None, 'ctxt': 'SEMBLABLE   car il ne sagt de rien mous que de Messortr des manche  8'},
 'car':
	{'lem': None, 'ctxt': 'semblable   CAR il ne sagt de rien mous que de Messortr des manche  8'},
 'sagt':
	{'lem': "s'agit", 'ctxt': 'semblable   car il ne SAGT de rien mous que de Messortr des manche  8',
	 'deja utilisé': ["semblable ; car il ne S'AGIT de rien mous que de ressortir des manche, 8"]},
 'mous':
	{'lem': 'moins', 'ctxt': 'semblable   car il ne sagt de rien MOUS que de Messortr des manche  8'},
 'Messortr':
	{'lem': 'ressortir',
	 'ctxt': 'semblable   car il ne sagt de rien mous que de MESSORTR des manche  8',
	 'deja utilisé': ["semblable ; car il ne s'agit de rien mous que de RESSORTIR des manche, 8"]},
 'manche':
	{'lem': None, 'ctxt': 'semblable   car il ne sagt de rien mous que de Messortr des MANCHE  8'},
 '8':
	{'lem': None, 'ctxt': 'semblable   car il ne sagt de rien mous que de Messortr des manche  8'},
 'bagne':
	{'lem': None, 'ctxt': 'ou ne BAGNE pas avec cela   s il n y en a pas  je m en passerai'},
 'passerai':
	{'lem': None, 'ctxt': 'ou ne bagne pas avec cela   s il n y en a pas  je m en PASSERAI'},
 'vais':
	{'lem': None, 'ctxt': 'Je VAIS enfin  je crois  faire le fameux voy age de Colague  et'},
 'crois':
	{'lem': None, 'ctxt': 'Je vais enfin  je CROIS  faire le fameux voy age de Colague  et'},
 'fameux':
	{'lem': None, 'ctxt': 'Je vais enfin  je crois  faire le FAMEUX voy age de Colague  et'},
 'voy age':
	{'lem': 'voyage', 'ctxt': 'Je vais enfin  je crois  faire le fameux VOY age de Colague  et'},
 'Colague':
	{'lem': 'Cologne',
	 'ctxt': 'Je vais enfin  je crois  faire le fameux voy age de COLAGUE  et',
	 'deja utilisé': ['Je vais enfin, je crois, faire le fameux voy age de COLOGNE, et']},
 'hasard':
	{'lem': None, 'ctxt': 'à tout HASARD  vous seriez bien amables de venir toruis deman ou'},
 'seriez':
	{'lem': None, 'ctxt': 'à tout hasard  vous SERIEZ bien amables de venir toruis deman ou'},
 'amables':
	{'lem': 'aimables', 'ctxt': 'à tout hasard  vous seriez bien AMABLES de venir toruis deman ou'},
 'toruis':
	{'lem': None, 'ctxt': 'à tout hasard  vous seriez bien amables de venir TORUIS deman ou'},
 'deman':
	{'lem': 'demain',
	 'ctxt': 'Arevor hone à DEMAN ',
	 'deja utilisé': ['A revoir hone à DEMAIN.']},
 'apres':
	{'lem': 'après', 'ctxt': 'APRES demain  Il n est gues tion ie que de Keinete et en abant pag-'},
 'gues tion':
	{'lem': 'question', 'ctxt': 'apres demain  Il n est GUES tion ie que de Keinete et en abant pag-'},
 'ie':
	{'lem': None, 'ctxt': 'apres demain  Il n est gues tion IE que de Keinete et en abant pag-'},
 'Keinete':
	{'lem': 'Kermesse',
	 'ctxt': 'apres demain  Il n est gues tion ie que de KEINETE et en abant pag-',
	 'deja utilisé': ['apres demain. il n&#39;est gues tion ie que de KERMESSE et en abant pag-']},
 'abant':
	{'lem': 'allant', 'ctxt': 'apres demain  Il n est gues tion ie que de Keinete et en ABANT pag-'},
 'pag-':
	{'lem': None, 'ctxt': 'apres demain  Il n est gues tion ie que de Keinete et en abant PAG-'},
 'mener':
	{'lem': None, 'ctxt': 'MENER du coté des bieuse pabités nous verrions encore une quure '},
 'coté':
	{'lem': None, 'ctxt': 'mener du COTÉ des bieuse pabités nous verrions encore une quure '},
 'bieuse':
	{'lem': None, 'ctxt': 'mener du coté des BIEUSE pabités nous verrions encore une quure '},
 'pabités':
	{'lem': 'habités', 'ctxt': 'mener du coté des bieuse PABITÉS nous verrions encore une quure '},
 'verrions':
	{'lem': None, 'ctxt': 'mener du coté des bieuse pabités nous VERRIONS encore une quure '},
 'quure':
	{'lem': None, 'ctxt': 'mener du coté des bieuse pabités nous verrions encore une QUURE '},
 '(dasle':
	{'lem': None, 'ctxt': '(DASLE Prine  L)'},
 'Prine':
	{'lem': 'Prince',
	 'ctxt': '(dasle PRINE  L)'},
 'L)':
	{'lem': 'de',
	 'ctxt': '(dasle Prine  L)'},
 '(eaer':
	{'lem': None, 'ctxt': '(EAER  je pars perdi '},
 'pars':
	{'lem': None, 'ctxt': '(eaer  je PARS perdi '},
 'perdi':
	{'lem': None, 'ctxt': '(eaer  je pars PERDI '},
 'Voite':
	{'lem': 'Voilà',
	 'ctxt': 'VOITE la nuissance tuit a fait à la raison daus potre cher pairs',
	 'deja utilisé': ['VOILÀ la puissance tuit a fait à la raison daus potre cher pairs']},
 'nuissance':
	{'lem': 'puissance',
	 'ctxt': 'Voite la NUISSANCE tuit a fait à la raison daus potre cher pairs',
	 'deja utilisé': ['Voilà la PUISSANCE tuit a fait à la raison daus potre cher pairs']},
 'tuit':
	{'lem': 'tout', 'ctxt': 'Voite la nuissance TUIT a fait à la raison daus potre cher pairs'},
 'raison':
	{'lem': None, 'ctxt': 'Voite la nuissance tuit a fait à la RAISON daus potre cher pairs'},
 'daus':
	{'lem': 'dans', 'ctxt': 'Voite la nuissance tuit a fait à la raison DAUS potre cher pairs'},
 'potre':
	{'lem': 'notre', 'ctxt': 'Voite la nuissance tuit a fait à la raison daus POTRE cher pairs'},
 'pairs':
	{'lem': None, 'ctxt': 'Voite la nuissance tuit a fait à la raison daus potre cher PAIRS'},
 'aurons':
	{'lem': None, 'ctxt': 'et nous AURONS de la banguillité  Dien merce Je l aime dens le monte'},
 'banguillité':
	{'lem': 'tranquillité', 'ctxt': 'et nous aurons de la BANGUILLITÉ  Dien merce Je l aime dens le monte'},
 'Dien':
	{'lem': 'Dieu',
	 'ctxt': 'et nous aurons de la banguillité  DIEN merce Je l aime dens le monte',
	 'deja utilisé': ['et nous aurons de la banguillité, DIEU merce Je l&#39;aime dens le monte']},
 'merce':
	{'lem': 'merci', 'ctxt': 'et nous aurons de la banguillité  Dien MERCE Je l aime dens le monte'},
 'dens':
	{'lem': 'dans', 'ctxt': 'et nous aurons de la banguillité  Dien merce Je l aime DENS le monte'},
 'monte':
	{'lem': None, 'ctxt': 'et nous aurons de la banguillité  Dien merce Je l aime dens le MONTE'},
 'asn':
	{'lem': None, 'ctxt': 'ASN surtont que ma ve puisse 2 y agitez librement vous avrez'},
 'surtont':
	{'lem': 'surtout',
	 'ctxt': 'asn SURTONT que ma ve puisse 2 y agitez librement vous avrez',
	 'deja utilisé': ['asn SURTOUT que ma ve puisse 2&#39;y agitez librement vous avrez']},
 've':
	{'lem': 'vie', 'ctxt': 'asn surtont que ma VE puisse 2 y agitez librement vous avrez'},
 'agitez':
	{'lem': None, 'ctxt': 'asn surtont que ma ve puisse 2 y AGITEZ librement vous avrez'},
 'librement':
	{'lem': None, 'ctxt': 'asn surtont que ma ve puisse 2 y agitez LIBREMENT vous avrez'},
 'avrez':
	{'lem': None, 'ctxt': 'asn surtont que ma ve puisse 2 y agitez librement vous AVREZ'},
 'inallr':
	{'lem': 'en aller', 'ctxt': 'en bien tort de vous INALLR la jour de notre monde  Mous udoens'},
 'jour':
	{'lem': None, 'ctxt': 'en bien tort de vous inallr la JOUR de notre monde  Mous udoens'},
 'notre':
	{'lem': None, 'ctxt': 'en bien tort de vous inallr la jour de NOTRE monde  Mous udoens'},
 'Mous':
	{'lem': 'Nous',
	 'ctxt': 'en bien tort de vous inallr la jour de notre monde  MOUS udoens',
	 'deja utilisé': ['en bien tort de vous inallr la jour de notre monde. NOUS udoens']},
 'udoens':
	{'lem': None, 'ctxt': 'en bien tort de vous inallr la jour de notre monde  Mous UDOENS'},
 'pasé':
	{'lem': 'passé', 'ctxt': 'PASÉ de jelis moments la soir  J ai ité heureuse comme une vraie'},
 'jelis':
	{'lem': 'jolis', 'ctxt': 'pasé de JELIS moments la soir  J ai ité heureuse comme une vraie'},
 'moments':
	{'lem': None, 'ctxt': 'pasé de jelis MOMENTS la soir  J ai ité heureuse comme une vraie'},
 'ité':
	{'lem': 'été', 'ctxt': 'pasé de jelis moments la soir  J ai ITÉ heureuse comme une vraie'},
 'vraie':
	{'lem': None, 'ctxt': 'pasé de jelis moments la soir  J ai ité heureuse comme une VRAIE'},
 'enfnt':
	{'lem': 'enfant', 'ctxt': 'ENFNT haunr me conorve cete pinesse d espouir à défant de l autre'},
 'haunr':
	{'lem': None, 'ctxt': 'enfnt HAUNR me conorve cete pinesse d espouir à défant de l autre'},
 'conorve':
	{'lem': 'conserve', 'ctxt': 'enfnt haunr me CONORVE cete pinesse d espouir à défant de l autre'},
 'pinesse':
	{'lem': 'jeunesse', 'ctxt': 'enfnt haunr me conorve cete PINESSE d espouir à défant de l autre'},
 'espouir':
	{'lem': None, 'ctxt': 'enfnt haunr me conorve cete pinesse d ESPOUIR à défant de l autre'},
 'défant':
	{'lem': 'défaut', 'ctxt': 'enfnt haunr me conorve cete pinesse d espouir à DÉFANT de l autre'},
 'Vest':
	{'lem': "C'est", 'ctxt': 'VEST la sourre de tout ce qu il y  a dé bon et de consolmnt dans lavdier',
	 'deja utilisé': ["C'EST la sourre de tout ce qu&#39;il y &#39;a dé bon et de consolmnt dans lavdier"]},
 'sourre':
	{'lem': 'source', 'ctxt': 'Vest la SOURRE de tout ce qu il y  a dé bon et de consolmnt dans lavdier'},
 'dé':
	{'lem': 'de', 'ctxt': 'Vest la sourre de tout ce qu il y  a DÉ bon et de consolmnt dans lavdier'},
 'consolmnt':
	{'lem': 'consolant', 'ctxt': 'Vest la sourre de tout ce qu il y  a dé bon et de CONSOLMNT dans lavdier'},
 'lavdier':
	{'lem': None, 'ctxt': 'Vest la sourre de tout ce qu il y  a dé bon et de consolmnt dans LAVDIER'},
 'Pai':
	{'lem': "J'ai", 'ctxt': 'PAI écrit des volumes ce matin  vous en êtes la dernière feuille',
	 'deja utilisé': ["J'AI écrit des volumes ce matin, vous en êtes la dernière feuille"]},
 'écrit':
	{'lem': None, 'ctxt': 'Pai ÉCRIT des volumes ce matin  vous en êtes la dernière feuille'},
 'volumes':
	{'lem': None, 'ctxt': 'Pai écrit des VOLUMES ce matin  vous en êtes la dernière feuille'},
 'feuille':
	{'lem': None, 'ctxt': 'Pai écrit des volumes ce matin  vous en êtes la dernière FEUILLE'},
 'savez':
	{'lem': None, 'ctxt': 'vous SAVEZ a ris des éharchandes de Poris auc derners les bous '},
 'ris':
	{'lem': 'cris', 'ctxt': 'vous savez a RIS des éharchandes de PoRIS auc derners les bous '},
 'éharchandes':
	{'lem': 'marchandes',
	 'ctxt': 'vous savez a ris des ÉHARCHANDES de Poris auc derners les bous ',
	 'deja utilisé': ['vous savez a ris des MARCHANDES de Paris auc derners les bous.']},
 'Poris':
	{'lem': 'Paris',
	 'ctxt': 'vous savez a ris des éharchandes de PORIS auc derners les bous ',
	 'deja utilisé': ['vous savez a ris des marchandes de PARIS auc derners les bous.']},
 'auc':
	{'lem': None, 'ctxt': 'vous savez a ris des éharchandes de Poris AUC derners les bous '},
 'derners':
	{'lem': None, 'ctxt': 'vous savez a ris des éharchandes de Poris auc DERNERS les bous '},
 'bous':
	{'lem': None, 'ctxt': 'vous savez a ris des éharchandes de Poris auc derners les BOUS '},
 'apendant':
	{'lem': 'cependant', 'ctxt': 'APENDANT je ne veux vous rien dire d agréable ausjourd hunit   cer il'},
 'ausjourd':
	{'lem': '''aujourd'hui''', 'ctxt': 'apendant je ne veux vous rien dire d agréable AUSJOURD hunit   cer il'},
 'cer':
	{'lem': 'car', 'ctxt': 'apendant je ne veux vous rien dire d agréable ausjourd hunit   CER il'},
 'semble':
	{'lem': None, 'ctxt': 'me SEMBLE que vors m arez bouvé massade la drnière fois'},
 'vors':
	{'lem': 'vous', 'ctxt': 'me semble que VORS m arez bouvé massade la drnière fois'},
 'arez':
	{'lem': 'avez', 'ctxt': 'me semble que vors m AREZ bouvé massade la drnière fois'},
 'bouvé':
	{'lem': None, 'ctxt': 'me semble que vors m arez BOUVÉ massade la drnière fois'},
 'massade':
	{'lem': 'maussade', 'ctxt': 'me semble que vors m arez bouvé MASSADE la drnière fois'},
 'drnière':
	{'lem': 'dernière', 'ctxt': 'me semble que vors m arez bouvé massade la DRNIÈRE fois'},
 'fois':
	{'lem': None, 'ctxt': 'me semble que vors m arez bouvé massade la drnière FOIS'},
 'Prucs':
	{'lem': 'Prons',
	 'ctxt': 'A Mr Mr PRUCS au (ataue de Liederg)'},
 '(ataue':
	{'lem': 'château', 'ctxt': 'A Mr Mr Prucs au (ATAUE de Liederg)'},
 'Liederg)':
	{'lem': 'Liedberg)',
	 'ctxt': 'A Mr Mr Prucs au (ataue de LIEDERG)',
	 'deja utilisé': ['A Mr Mr Prucs au (ataue de LIEDBERG)']},
 '(k':
	{'lem': None, 'ctxt': '(K  (Cerrese p)'},
 '(Cerrese':
	{'lem': '(Cerrese',
	 'ctxt': '(k  (CERRESE p)'},
 'p)':
	{'lem': None, 'ctxt': '(k  (Cerrese P)'},
 'Saroibre':
	{'lem': 'Septembre',
	 'ctxt': 'Dyck  le je SAROIBRE  1816 ',
	 'deja utilisé': ['Dyck, le je SEPTEMBRE, 1816.']},
 'Arevor':
	{'lem': 'A revoir',
	 'ctxt': 'AREVOR hone à deman ',
	 'deja utilisé': ['A REVOIR hone à demain.']},
 'hone':
	{'lem': None, 'ctxt': 'Arevor HONE à deman '},
 '(Sgné)':
	{'lem': '(Signé)',
	 'ctxt': '(SGNÉ) Cons tence de Sal',
	 'deja utilisé': ['(SIGNÉ) Cons tence de Salm']},
 'Cons tence':
	{'lem': 'Constance',
	 'ctxt': '(Sgné) CONS tence de Sal'},
 'Sal':
	{'lem': 'Salm',
	 'ctxt': '(Sgné) Cons tence de SAL',
	 'deja utilisé': ['(Signé) Cons tence de SALM']}}

with open("./py/dictPages/DictCdS02_Konv002-02_0067.json", mode="w", encoding="UTF-8") as f:
	json.dump(dictPage, f, indent=2, ensure_ascii=False)
	print("Imprimé correctement")