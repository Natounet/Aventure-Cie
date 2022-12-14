#encoding:utf-8
from fastapi import FastAPI
import json

from verifications import *
from classes import *
import bleach
from datetime import datetime
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
            *histoire: [str,None] # Histoire du don
        """
        
    ### Néttoyage des chaines ###
    
    don.nomBalise = bleach.clean(don.nomBalise)
    don.nom = bleach.clean(don.nom)
    don.caracteristique = bleach.clean(don.caracteristique).capitalize()
    don.histoire = bleach.clean(don.histoire)
    
    
    ### Vérifications des autres attributs ###
    messageErreur = verifications(nom=don.nom,caracteristique=don.caracteristique)
    
    if don.histoire is not None:
        if(not verificationTailleChaine(don.histoire,0,1000)):
            messageErreur.append("La taille de l'histoire est trop élevée")
    
    ### Vérification que nomBalise n'est pas présent dans la BDD ###

    
    # Si il y a des erreurs
    if messageErreur != []:
        return messageErreur
    
    # Si pas d'érreurs
    
    
    ### LOG DU DON ###
    log(f"Creation d'un don - {datetime.now().strftime('%d/%m/%Y %X')}")
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
    
    
    
    
    
    # Implémenter fonction pour vérifier si nomBalise existe dans la BDD
    # Vérification du nomBalise
    
    # Creation de l'arme dans la BDD
    
    
   
    

    log(f"Creation d'une arme - {datetime.now().strftime('%d/%m/%Y %X')}")
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
