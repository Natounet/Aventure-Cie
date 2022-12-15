#encoding:utf-8


from jsonschema import validate
from config import caracteristiques,categoriesArme,typeObjetsMagiques

def schemaValide(objetJSON: list, schemaJSON) -> bool:
    """ Fonction permettant de valider un objet JSON avec un schéma
        Retourne True si valide, False sinon"""

    try:
        validate(objetJSON, schemaJSON)
        return True # Fichier répondant au schéma
    except Exception as e:
        print(e)
        return False # Fichier ne répondant pas au schéma
    
    
def verificationTailleChaine(chaine: str, minimum: int ,maximum: int ) -> bool:
    """ Fonction qui vérifie si une chaîne de caractère est dans la longueur mimimale et maximale
        La chaine avoir une taille supérieure ou égale au minimum
        et inférieure ou égale au maximun
        Retourne True si c'est le cas,
        False sinon """
        
    return len(chaine) >= minimum and len(chaine) <= maximum

def verificationAlpha(chaine: str) -> bool:
    """ Fonction permettant de savoir si une chaîne ne contient que des caractères alpha numériques
        Rappel : A-Z, a-z et l'espace,
        Si c'est le cas, retourne true,
        Sinon, retourne false"""
        
    for lettre in chaine:
        if not lettre.isalpha() and lettre != " ":
            return False
        
    return True
        
    
def verificationCategoriesArme(listeCategories: list) -> str:
    """ Fonction vérifiant si une liste de catégories d'arme est valide
        Chaque élement de la liste doivent être présent dans les catégories définies en config
        Il ne doit pas y avoir de doublons"""
        
    categoriesFinal = []
    
    for cat in listeCategories:
        if cat not in categoriesFinal:
            categoriesFinal.append(cat)
        else:
            return "Il y a des doublons dans les catégories."
    
    for cat in categoriesFinal:
        if cat not in categoriesArme:
            return f"La catégorie {cat} n'éxiste pas."
                
    return ""
        
    

def verificationCaracteresBannis(chaine: str) -> bool:
    """ Fonction qui vérifie la présence ou non de caractères bannis dans une chaîne de caractère
        Retourne True si elle n'en contient pas, false sinon
    """
        
    caracteresBannis = [">","<","'","-","/","\\","#"]
    
    if caracteresBannis in chaine:
        return False
    return True


##### VERIFICATION ATTRIBUTS #####


def verificationNom(nom: str) -> str:
    """ Verifie si un nom est valide 
        Retourne True si il est valide,
        Retourne false sinon"""

    
    # Taille nom non réglementaire
    if(not verificationTailleChaine(nom,1,30)):
        return "Le nom est invalide."
    
    # Le nom ne comporte que des caractères alpha
    if(not verificationAlpha(nom)):
        return "Le nom est invalide."
    
    return ""


def verificationPrix(prix: float) -> str:
    """ Vérification du prix """
    
    if(prix < 0):
        return "Il y a un problème dans le prix."
    
    return ""



def verifiationCritique(critique: int) -> str:
    """ Vérifie si un multiplicateur critique est valide"""
    
    if(critique < 1):
        return "Il y a un problème de multiplicateur de critique."
    
    return ""

def verificationDegats(degats: str) -> str:
    """ Vérifie si les dégats sont valides"""
    
    # Trop d'infos
    if(not verificationTailleChaine(degats,1,10)):
        return "Il y a un problème dans la valeur de dégats."
    
    return ""

def verificationPortee(portee: float) -> str:
    """ Vérifie si la portée est cohérente """
    
    if(portee <= 0):
        return "Il y a un problème dans la valeur de portée."
    
    return ""

def verificationPoids(poids: float) -> str:
    """ Vérification du poids """
    
    if(poids <= 0):
        return "Il y a un problème dans le poids."
    
    return ""



def verificationArmure(armure: int) -> str:
    """ Vérifie l'armure
        Elle peut être négative 
        Ne sert à rien, la vérification du type est faite en amont"""
    
    if type(armure) is not int:
        return "Le nombre de points d'armure doit être un entier."
    
    return ""

def verificationCaracteristique(caracteristique: str) -> str:
    """ Vérifie si la caractéristique entrée est dans la liste des caractéristiques existantes"""
    
    print(caracteristique)
    if caracteristique not in caracteristiques:
        return "La caractéristique n'est pas valide."
    else:
        return ""


def verificationMalusArmure(malusArmure: int) -> str:
    ''' Vérifie si malusArmure est correcte '''

    if(malusArmure % 5 != 0):
        return "MalusArmure doit être un multiple de 5%."
    elif(malusArmure < 0 or malusArmure > 50):
        return "MalusArmure doit être compris entre 0 et 50. 5 correspond à -5%"
    else:
        return ""

# Non implémentée
def verifiationTypeObject(typeObject: str) -> str:
    """ Vérifie si le typeObject existe """

    if typeObject not in typeObjetsMagiques:
        return f"{typeObject} n'existe pas."

    return ""





"""
Les vérifications faites par la fonction

Vérifié : 
nom
prix
critique
portee
degats
poids
armure
caracteristique
nomBalise
malusArmure
typeObjet

Non verifié : 

description

Arme : 
    categories

Armure :
    categorie

Objet magique :  

coutPsyche
spam
utlisation
localisation
coutVie
histoire

"""





def verifications(nom: str = None, prix: float = None, critique: int = None, portee: float = None, degats: str = None, poids: float = None, armure: int = None, caracteristique: str = None, nomBalise: str = None, malusArmure: float = None, typeObject: str = None):
    """ Fonction qui s'occupe de vérifier seulement les arguments donnés explicitement
        Pour les armes, on vérifiera que les attributs des armes 
        
        La fonction retourne None si il n'y a aucune erreur,
        Sinon, retourne une chaîne contenant les erreurs
        """

    messageErreur = []

    if(nom is not None):
        messageErreur.append(verificationNom(nom))

    if(prix is not None):
        messageErreur.append(verificationPrix(prix))

    if(critique is not None):
        messageErreur.append(verifiationCritique(critique))
    
    if(portee is not None):
        messageErreur.append(verificationPortee(portee))

    if(degats is not None):
        messageErreur.append(verificationDegats(degats))

    if(poids is not None):
        messageErreur.append(verificationPoids(poids))

    if(armure is not None):
        messageErreur.append(verificationArmure(armure))

    if(caracteristique is not None):
        messageErreur.append(verificationCaracteristique(caracteristique))

    if(malusArmure is not None):
        messageErreur.append(verificationMalusArmure(malusArmure))

    if(typeObject is not None):
        messageErreur.append(verifiationTypeObject(typeObject))

    

   
    cleanMessageErreur = [ x for x in messageErreur if x != "" ]
    return cleanMessageErreur
