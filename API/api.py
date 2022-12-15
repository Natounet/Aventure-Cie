#encoding:utf-8
from fastapi import FastAPI 
import json
import bleach # Sanitizer
from datetime import datetime # Pour la date  



from verifications import *
from classes import *
from sql import *

app = FastAPI()

   
with open('jsonSchemas/categoriesSchema.json','r') as f:
    categoriesSchema = json.load(f)
    
    
    
def log(chaine: str) -> None:
    
    with open('APIlog.txt','a',encoding='utf-8') as file:
        file.write(f"{chaine}\n")
        
    
def sanitizeChaine(chaine: str) -> str:
    """ Fonction qui sanitize une chaine en utilisant le module bleach
        Retourne la chaine sanitized """
    
    chaine = chaine.strip()
    return bleach.clean(chaine,strip=True)


def premiereLettreMajuscule(chaine: str) -> str:
    """ Fonction qui retourne une chaine avec seulement la première lettre en majuscule
        ex: "bOnJOUr -> Bonjour"""
        
    return chaine.capitalize()


### FONCTIONS DE VERIFICATION




@app.post("/ajout/don")
async def creerDon(don: Don):
    """ Route permettant la création d'un don dans la base de données
    
        Attributs d'un don : \n
            *nomBalise: str #nom Unique du don pour le référencer
            *nom: str # Nom du don descriptif
            *caracteristique: str # ex Puissance
            *histoire: [str,None] # Histoire du don ( non obligatoire )
        """
        
    ### Néttoyage des chaines ###
    
    don.nomBalise = bleach.clean(don.nomBalise)
    don.nom = bleach.clean(don.nom)
    don.caracteristique = bleach.clean(don.caracteristique).capitalize()
    
    if don.histoire is not None:
        don.histoire = bleach.clean(don.histoire)
    
    
    ### Vérifications des autres attributs ###
    messageErreur = verifications(nom=don.nom,caracteristique=don.caracteristique)
    
    if don.histoire is not None:
        if(not verificationTailleChaine(don.histoire,0,1000)):
            messageErreur.append("La taille de l'histoire est trop élevée")
    
    ### Vérification que nomBalise n'est pas présent dans la BDD ###

    if(don.nomBalise is not None and nomBaliseDansBDD(don.nomBalise)):
        messageErreur.append("Ce nom balise est déjà utilisé")
        
    # Si il y a des erreurs
    if messageErreur != []:
        return messageErreur
    
    # Si pas d'érreurs
    
    
    if(not creerDonDansLaBDD(don)):
        return "Il y a eu une erreur lors de la creation du don."

    
    
    ### LOG DU DON ###
    log(f"{datetime.now().strftime('%d/%m/%Y %X')} - Creation d'un don")
    log(f"NomBalise du don : {don.nomBalise}")
    log(f"Nom du don : {don.nom}")
    log(f"Caractéristique du don : {don.caracteristique}")
    log(f"Histoire du don : {don.histoire}")
    log(f"")

    
    
    
    return "Le don a été crée."
    
        
    

@app.post("/ajout/arme")
async def creerArme(arme: Arme):
    """ Route permettant de créer une arme dans la base de données

        Attributs arme : \n
            * nom: str # Nom de l'arme
            * description: Union[str, None] # Description de l'arme, peut être nul
            * prix: Union[float, None] # Prix de l'arme, peut être nul
            * critique: int # mutliplicateur de coûts critiques
            * portee: int # Portée en mètres de l'arme
            * degats: str # Quels dés de dégats ( ex: 2 D8)
            * poids: float # Poids de l'arme en kilo
            * armure: int # Bonus/Malus d'armure
            * caracteristique: str # Caractéristique de l'arme ( ex : Puissance )
            * categories: list # Catégorise SOUS LA FORME D'UN JSON
            * nomBalise: Union[str, None] # NomBalise du don qu'il possède si existant ( peut être nul)
 

    """
    #### Néttoyage des chaines ####

    arme.nom = sanitizeChaine(arme.nom)
    arme.caracteristique = sanitizeChaine(arme.caracteristique).capitalize()
    
    # Description peut être null / pas besoin d'être verifiée si nettoyée
    if arme.description is not None:
        arme.description = sanitizeChaine(arme.description)

    # Nom balise peut être null
    if arme.nomBalise is not None:
        arme.nomBalise = sanitizeChaine(arme.nomBalise)

    arme.degats = sanitizeChaine(arme.degats)

    #### Vérification des attributs ####

    # messageErreur est une liste des erreurs
    messageErreur = verifications(nom=arme.nom, prix= arme.prix, critique=arme.critique, portee=arme.portee, degats=arme.degats, poids=arme.poids, armure=arme.armure, caracteristique=arme.caracteristique,nomBalise=arme.nomBalise)
    
    # Vérification du JSON catégories

    if(not schemaValide(arme.categories, categoriesSchema)):
        messageErreur.append("Les catégories entrées ne sont pas valides.")
    
    # Formattage du nom des catégories
    for i in range(len(arme.categories)):
        arme.categories[i] = arme.categories[i].capitalize()
    
    # Vérification des catégories d'arme
    
    if(verificationCategoriesArme(arme.categories) != ""):
        messageErreur.append(verificationCategoriesArme(arme.categories))
    
    # En cas d'erreurs pour certains attributs
    if messageErreur != []:
        return messageErreur
    
    #### Vérification de la présence de nomBalise dans la BDD ####
    
    if(arme.nomBalise is not None and not nomBaliseDansBDD(arme.nomBalise)):
        return "Le don associé à l'arme n'existe pas."
    
    ### Creation de l'arme dans la BDD ###
    
    if(not creerArmeDansLaBDD(arme)):
        return "Il y a eu une erreur dans la création de l'arme."
   
    

    log(f"{datetime.now().strftime('%d/%m/%Y %X')} - Creation d'une arme")
    log(f"Nom de l'arme : {arme.nom}")
    log(f"Description de l'arme : {arme.description}")
    log(f"Prix de l'arme : {arme.prix}")
    log(f"Critique de l'arme : {arme.critique}")
    log(f"Portée de l'arme : {arme.portee}")
    log(f"Dégats de  l'arme : {arme.degats}")
    log(f"Poids de l'arme : {arme.poids}")
    log(f"Armure de l'arme : {arme.armure}")
    log(f"Caracteristique de l'arme : {arme.caracteristique}")
    log(f"Catégories de l'arme : {str(arme.categories)}")
    log(f"")

    # Creation de l'arme dans la BDD
    return "L'arme à bien été créée."

@app.post("/ajout/armure")
def creerArmure(armure: Armure):
    """ Route permettant de créer une armure dans la base de données 
    
        * nom: str # Nom de l'armure
        * description: Union[str,None] # Description de l'armure ( peut ne pas être présente )
        * prix: Union[float, None] # Prix de l'armure ( peut ne pas être présente )
        * poids: float # Poids de l'armure
        * armure: int # Points d'armure
        * caracteristique: str # Caractéristique dépendante de l'arme ( ex: Puissance )
        * categorie: str # Catégorie de l'armure ( type d'armure, voir config.py )
        * malusArmure: int # Malus lié au poids de l'armure ( -5 = -5% )
        * nomBalise: Union[str, None] # nomBalise du don associé si présent

    """

    ### Nettoyage des chaînes ### 

    armure.nom = bleach.clean(armure.nom)

    if armure.description is not None:
        armure.description = bleach.clean(armure.description)
    
    armure.caracteristique = bleach.clean(armure.caracteristique).capitalize()
    armure.categorie = bleach.clean(armure.categorie).capitalize()

    if armure.nomBalise is not None:
        armure.nomBalise = bleach.clean(armure.nomBalise)

    ### Vérification des attributs

    messageErreur = verifications(nom=armure.nom, prix=armure.prix, poids=armure.poids, armure=armure.armure, caracteristique=armure.caracteristique, malusArmure=armure.malusArmure)

    if (verificationCategorieArmure(armure.categorie) != ""): # Si erreur
        messageErreur.append(verificationCategorieArmure(armure.categorie))

    if(armure.description is not None):
        if(not verificationTailleChaine(armure.description,1,1000)):
            messageErreur.append("La taille de la description est actuellement limitée à 1000 caractères")

        
    #### Vérification de la présence de nomBalise dans la BDD ####
    
    if(armure.nomBalise is not None and not nomBaliseDansBDD(armure.nomBalise)):
        messageErreur.append("Le don associé à l'arme n'existe pas.")
    
    ### Cas d'erreurs

    if messageErreur != []:
        return messageErreur

    
    ### Creation de l'armure dans la BDD ###


    log(f"{datetime.now().strftime('%d/%m/%Y %X')} - Creation d'une arme")
    log(f"Nom de l'armure : {armure.nom}")
    log(f"Description de l'armure : {armure.description}")
    log(f"Prix de l'armure : {armure.prix}")
    log(f"Poids de l'armure : {armure.poids}")
    log(f"Armure de l'armure : {armure.armure}")
    log(f"Caracteristique de l'armure : {armure.caracteristique}")
    log(f"Catégorie de l'armure : {armure.categorie}")
    log(f"malusArmure de l'armure : {armure.malusArmure}")
    log(f"nomBalise de l'armure : {armure.nomBalise}")
    log("")

    return "L'armure a été crée."
