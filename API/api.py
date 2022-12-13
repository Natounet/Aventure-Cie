from fastapi import FastAPI
import json

from verifications import *
from classes import *
import bleach

app = FastAPI()

   
with open('jsonSchemas/categoriesSchema.json','r') as f:
    categoriesSchema = json.load(f)
    
    
    
def log(chaine: str) -> None:
    
    with open('APIlog.txt','a') as file:
        file.write(f"{chaine}\n")
        
    


def sanitizeChaine(chaine: str) -> str:
    """ Fonction qui sanitize une chaine en utilisant le module bleach
        Retourne la chaine sanitized """
    
    chaine = chaine.strip()
    return bleach.clean(chaine,strip=True)




### FONCTIONS DE VERIFICATION




@app.post("/ajout/don")
async def creerDon(don: Don):
    return don

@app.post("/ajout/arme")
async def creerArme(arme: Arme):
    """ Route permettant de créer une arme dans la base de données"""
    
    arme.nom = sanitizeChaine(arme.nom)
    
    ### Vérification du nom ###
    
    if(not verificationNom(arme.nom)):
        return "Le nom est invalide."
    
    # Description peut être null
    if arme.description is not None:
        arme.description = sanitizeChaine(arme.description)
    
    # Prix
    if arme.prix is not None:
        if arme.prix == 0:
            arme.prix = None
        else:
            if(not verificationPrix(arme.prix)):
                return "Il y a un problème dans le prix."
    

    # Critique
    
    if(not verifiationCritique(arme.critique)):
        return "Il y a un problème de multiplicateur de critique."
    
    # Portee
    
    if(not verificationPortee(arme.portee)):
        return "Il y a un problème dans la valeur de portée."
    
    # Degats
    
    if(not verificationDegats(arme.degats)):
        return "Il y a un problème dans la valeur de dégats."
    
    # Poids
    
    if(not verificationPoids(arme.poids)):
        return "Il y a un problème dans le poids."
    
    # Armure
    
    if(not verificationArmure(arme.armure)):
        return "Il y a un problème dans la valeur de l'armure."
    
    # Caracteristique
    
    arme.caracteristique = arme.caracteristique.strip()
    if(not verificationCaracteristique(arme.caracteristique)):
        return "La caractéristique n'est pas valide."
    
    # Catégories
    
    if(not schemaValide(arme.categories, categoriesSchema)):
        return "Les catégories entrées ne sont pas valides."
    
    
    # Implémenter fonction pour vérifier si nomBalise existe dans la BDD
    # Vérification du nomBalise
    
    # Creation de l'arme dans la BDD
    
    
    
    
    log(f"Nom de l'arme : {arme.nom}")
    log(f"Description de l'arme : {arme.description}")
    log(f"Prix de l'arme : {arme.prix}")
    log(f"Critique de l'arme : {arme.critique}")
    log(f"Portée de l'arme : {arme.portee}")
    log(f"Dégats de  l'arme : {arme.degat}")
    log(f"Poids de l'arme : {arme.poids}")
    log(f"Armure de l'arme : {arme.armure}")
    log(f"Caracteristique de l'arme : {arme.caracteristique}")
    log(f"Catégories de l'arme : {str(arme.categories)}")
    log(f"")

    return "L'arme à bien été créée."
