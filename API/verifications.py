
from jsonschema import validate
from string import ascii_letters

from config import *

def schemaValide(objetJSON: list, schemaJSON) -> bool:
    """ Fonction permettant de valider un objet JSON avec un schéma
        Retourne True si valide, False sinon"""
    

    
    print(schemaJSON)
        
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
        if lettre not in ascii_letters and lettre != " ":
            return False
        
    return True
        
    

def verificationCaracteresBannis(chaine: str) -> bool:
    """ Fonction qui vérifie la présence ou non de caractères bannis dans une chaîne de caractère
        Retourne True si elle n'en contient pas, false sinon
    """
        
    caracteresBannis = [">","<","'","-","/","\\","#"]
    
    if caracteresBannis in chaine:
        return False
    return True


##### VERIFICATION ATTRIBUTS #####


def verificationNom(nom: str) -> bool:
    """ Verifie si un nom est valide 
        Retourne True si il est valide,
        Retourne false sinon"""

    
    # Taille nom non réglementaire
    if(not verificationTailleChaine(nom,1,30)):
        return False
    
    # Le nom ne comporte que des caractères alpha
    if(not verificationAlpha(nom)):
        return False
    
    return True


def verificationPrix(prix: float) -> bool:
    """ Vérification du prix """
    
    if(prix < 0):
        return False
    
    return True



def verifiationCritique(critique: int) -> bool:
    """ Vérifie si un multiplicateur critique est valide"""
    
    if(critique < 1):
        return False
    
    return True

def verificationDegats(degats: str) -> bool:
    """ Vérifie si les dégats sont valides"""
    
    # Trop d'infos
    if(not verificationTailleChaine(degats,1,10)):
        return False
    
    return True

def verificationPortee(portee: float) -> bool:
    """ Vérifie si la portée est cohérente """
    
    if(portee <= 0):
        return False
    
    return True

def verificationPoids(poids: float) -> bool:
    """ Vérification du poids """
    
    if(poids < 0):
        return False
    
    return True

def verificationArmure(armure: int) -> bool:
    """ Non implémentée pour l'instant """
    
    return True

def verificationCaracteristique(caracteristique: str) -> bool:
    """ Vérifie si la caractéristique entrée est dans la liste des caractéristiques existantes"""
    
    if caracteristique.lower() not in caracteristiques:
        return False
    else:
        return True