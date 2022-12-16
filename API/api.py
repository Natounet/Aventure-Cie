#encoding:utf-8
from fastapi import FastAPI 
import json
import bleach # Sanitizer
from datetime import datetime # Pour la date  



from verifications import *
from classes import *
from sql import *

app = FastAPI()

   
with open('jsonSchemas/schemaCategoriesArmes.json','r') as f:
    categoriesSchema = json.load(f)
    
    
    
def log(chaine: str) -> None:
    
    with open('APIlog.txt','a',encoding='utf-8') as file:
        file.write(f"{chaine}\n")
        
    
def sanitizeChaine(chaine: str) -> str:
    """ Fonction qui sanitize une chaine en utilisant le module bleach
        Retourne la chaine sanitized """
    
    chaine = chaine.strip()
    return bleach.clean(chaine,strip=True)




### FONCTIONS DE VERIFICATION




@app.post("/ajout/don")
async def creerDon(don: Don) -> list:
    """ Route permettant la création d'un don dans la base de données
    
        Attributs d'un don : \n
            *nomBalise: str #nom Unique du don pour le référencer
            *nom: str # Nom du don descriptif
            *caracteristique: str # ex Puissance
            *histoire: [str,None] # Histoire du don ( non obligatoire )
            
        Retourne une liste d'erreurs ( vide si pas d'erreurs)

    
    """
        
    ### Néttoyage des chaines ###
    
    don.nomBalise = sanitizeChaine(don.nomBalise)
    don.nom = sanitizeChaine(don.nom)
    don.caracteristique = sanitizeChaine(don.caracteristique).capitalize()
    
    if don.histoire is not None:
        don.histoire = sanitizeChaine(don.histoire)
    
    
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
        return ["Il y a eu une erreur lors de la creation du don."]

    
    
    ### LOG DU DON ###
    log(f"{datetime.now().strftime('%d/%m/%Y %X')} - Creation d'un don")
    log(f"NomBalise du don : {don.nomBalise}")
    log(f"Nom du don : {don.nom}")
    log(f"Caractéristique du don : {don.caracteristique}")
    log(f"Histoire du don : {don.histoire}")
    log(f"")

    
    
    
    return []
    
        
    

@app.post("/ajout/arme")
async def creerArme(arme: Arme) -> list:
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
 
        Retourne une liste d'erreurs ( vide si pas d'erreurs)


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
    messageErreur = verifications(nom=arme.nom, prix= arme.prix, critique=arme.critique, portee=arme.portee, degats=arme.degats, poids=arme.poids, armure=arme.armure, caracteristique=arme.caracteristique)
    
    # Vérification du JSON catégories

    if(not schemaValide(arme.categories, categoriesSchema)):
        messageErreur.append("Les catégories entrées ne sont pas valides.")

    # Vérification de la description

    if(arme.description is not None):
        if(not verificationTailleChaine(arme.description,1,1000)):
            messageErreur.append("La taille de la description est actuellement limitée à 1000 caractères")
    
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
        return ["Le don associé à l'arme n'existe pas."]
    
    ### Creation de l'arme dans la BDD ###
    
    if(not creerArmeDansLaBDD(arme)):
        return ["Il y a eu une erreur dans la création de l'arme."]
   
    

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

    return []

@app.post("/ajout/armure")
async def creerArmure(armure: Armure) -> list:
    """ Route permettant de créer une armure dans la base de données 
    
        Attributs armure:\n
            * nom: str # Nom de l'armure
            * description: Union[str,None] # Description de l'armure ( peut ne pas être présente )
            * prix: Union[float, None] # Prix de l'armure ( peut ne pas être présente )
            * poids: float # Poids de l'armure
            * armure: int # Points d'armure
            * caracteristique: str # Caractéristique dépendante de l'arme ( ex: Puissance )
            * categorie: str # Catégorie de l'armure ( type d'armure, voir config.py )
            * malusArmure: int # Malus lié au poids de l'armure ( -5 = -5% )
            * nomBalise: Union[str, None] # nomBalise du don associé si présent

        Retourne une liste d'erreurs ( vide si pas d'erreurs)


    """

    ### Nettoyage des chaînes ### 

    armure.nom = sanitizeChaine(armure.nom)

    if armure.description is not None:
        armure.description = sanitizeChaine(armure.description)
    
    armure.caracteristique = sanitizeChaine(armure.caracteristique).capitalize()
    armure.categorie = sanitizeChaine(armure.categorie).capitalize()

    if armure.nomBalise is not None:
        armure.nomBalise = sanitizeChaine(armure.nomBalise)

    ### Vérification des attributs

    messageErreur = verifications(nom=armure.nom, prix=armure.prix, poids=armure.poids, armure=armure.armure, caracteristique=armure.caracteristique, malusArmure=armure.malusArmure)

    if (verificationCategorieArmure(armure.categorie) != ""): # Si erreur
        messageErreur.append(verificationCategorieArmure(armure.categorie))

    if(armure.description is not None):
        if(not verificationTailleChaine(armure.description,1,1000)):
            messageErreur.append("La taille de la description est actuellement limitée à 1000 caractères.")

        
    #### Vérification de la présence de nomBalise dans la BDD ####
    
    if(armure.nomBalise is not None and not nomBaliseDansBDD(armure.nomBalise)):
        messageErreur.append("Le don associé à l'armure n'existe pas.")
    
    ### Cas d'erreurs

    if messageErreur != []:
        return messageErreur

    
    ### Creation de l'armure dans la BDD ###

    if(not creerArmureDansLaBDD(armure)):
        return ["Il y a eu une erreur dans la création de l'armure."]

    log(f"{datetime.now().strftime('%d/%m/%Y %X')} - Creation d'une armure")
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
    
    return []

@app.post("/ajout/objetMagique")
def creerObjetMagique(objetMagique: classes.objetMagique):

    """ Route permettant de créer un objet magique dans la base de données 

        Attributs objet magique:\n
            * nom: str # Nom de l'objet magique
            * description: Union[str,None] # Description de l'objet magique ( peut ne pas être donné)
            * prix: Union[float, None] # Prix de l'objet, ( peut ne pas être donné)
            * histoire: Union[str, None] # Histoire de l'objet ( peut ne pas être donné)
            * localisation: Union[str, None] # Lore de l'objet ( peut ne pas être donné)
            * utilisation: str # Utilisation tous les x temps ( ) jour/semaine/mois/année/heure
            * spam: bool # Peut être utilisable à l'infini 
            * coutPsyche: int # Cout en psyche de l'objet 
            * coutVie: int # Cout en vie de l'objet 
            * caracteristique: str # Caracteristique, ex : Puissance
            * typeObjet: str # Type de l'objet magique exemple : lunette, bottes, ...
            * nomBalise: Union[str, None] # nom du don lié à l'objet ( peut ne pas être donné)
        
    
    """


    ### Nettoyage des chaînes ###

    objetMagique.nom = sanitizeChaine(objetMagique.nom)

    if objetMagique.description is not None:
        objetMagique.description = sanitizeChaine(objetMagique.description)
    
    if objetMagique.histoire is not None:
        objetMagique.histoire = sanitizeChaine(objetMagique.histoire)

    if objetMagique.localisation is not None:
        objetMagique.localisation = sanitizeChaine(objetMagique.localisation)
    
    objetMagique.utilisation = sanitizeChaine(objetMagique.utilisation).capitalize()
    
    if objetMagique.caracteristique is not None:
        objetMagique.caracteristique = sanitizeChaine(objetMagique.caracteristique).capitalize()
    
    if objetMagique.typeObjet is not None:
        objetMagique.typeObjet = sanitizeChaine(objetMagique.typeObjet).capitalize()

    if objetMagique.nomBalise is not None:
        objetMagique.nomBalise = sanitizeChaine(objetMagique.nomBalise)

    ### Vérification des attributs

    messageErreur = (verifications(nom=objetMagique.nom, caracteristique=objetMagique.caracteristique,typeObjet=objetMagique.typeObjet,prix=objetMagique.prix))

    # Histoire
    if objetMagique.histoire is not None:
        if(not verificationTailleChaine(objetMagique.histoire,1,1000)):
                messageErreur.append("La taille de l'histoire est actuellement limitée à 1000 caractères.")

    # Localisation
    if objetMagique.localisation is not None:
        if(not verificationTailleChaine(objetMagique.localisation,1,1000)):
                messageErreur.append("La taille de la localisation est actuellement limitée à 1000 caractères.")

    # Description
    if objetMagique.description is not None:
        if(not verificationTailleChaine(objetMagique.description,1,1000)):
                messageErreur.append("La taille de la description est actuellement limitée à 1000 caractères.")

    # Utilisation
    if(not verificationTailleChaine(objetMagique.utilisation,1,10)):
            messageErreur.append("La taille de l'utilisation ne doit pas dépassée 10 caractères.")

    if(verificationUtilisation(objetMagique.utilisation) != ""):
        messageErreur.append(verificationUtilisation(objetMagique.utilisation))

    # Coût psyche

    if(objetMagique.coutPsyche < 0):
        messageErreur.append("Le coût en psyche ne peut pas être négatif.")

    # Coût PV

    if(objetMagique.coutVie < 0):
        messageErreur.append("Le coût en point de vie ne peut être négatif.")

    #### Vérification de la présence de nomBalise dans la BDD ####
    
    if(objetMagique.nomBalise is not None and not nomBaliseDansBDD(objetMagique.nomBalise)):
        messageErreur.append("Le don associé à l'armure n'existe pas.")
    

    ### Si erreur ###

    if messageErreur != []:
        return messageErreur
        

    ### Ajout de l'objet magique dans la BDD ###
    
    if(not creerObjetMagiqueDansLaBDD(objetMagique)):
        "Il y a eu une erreur lors de la création de l'objet magique."

    log(f"{datetime.now().strftime('%d/%m/%Y %X')} - Creation d'un objet magique")
    log(f"Nom de l'objet magique: {objetMagique.nom}")
    log(f"Description de l'objet magique: {objetMagique.description}")
    log(f"Prix de l'objet magique: {objetMagique.prix}")
    log(f"Histoire de l'objet magique: {objetMagique.histoire}")
    log(f"Localisation de l'objet magique: {objetMagique.localisation}")
    log(f"Utilisation de l'objet magique: {objetMagique.utilisation}")
    log(f"Spam de l'objet magique: {objetMagique.spam}")
    log(f"Coût en psyche de l'objet magique: {objetMagique.coutPsyche}")
    log(f"Coût en point de vie de l'objet magique: {objetMagique.coutVie}")
    log(f"Caracteristique de l'objet magique: {objetMagique.caracteristique}")
    log(f"Type de l'objet magique: {objetMagique.typeObjet}")
    log(f"nomBalise de l'objet magique: {objetMagique.nomBalise}")
    log("")

    return []