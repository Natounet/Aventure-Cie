#encoding:utf-8


from fastapi import FastAPI
import json

from verifications import *
from classes import *
import bleach

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




### FONCTIONS DE VERIFICATION




@app.post("/ajout/don")
async def creerDon(don: Don):
    return don

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
    # Néttoyage des chaines

    arme.nom = sanitizeChaine(arme.nom)
    arme.caracteristique = sanitizeChaine(arme.caracteristique)
    
    # Description peut être null / pas besoin d'être verifiée si nettoyée
    if arme.description is not None:
        arme.description = sanitizeChaine(arme.description)

    # Nom balise peut être null
    if arme.nomBalise is not None:
        arme.nomBalise = sanitizeChaine(arme.nomBalise)

    arme.degats = sanitizeChaine(arme.degats)


    # Vérification des attributs

    # messageErreur est une liste des erreurs
    messageErreur = verifications(nom=arme.nom, prix= arme.prix, critique=arme.critique, portee=arme.portee, degats=arme.degats, poids=arme.poids, armure=arme.armure, caracteristique=arme.caracteristique,nomBalise=arme.nomBalise)
    
    
    # Vérification des catégories d'arme
    
    if(not schemaValide(arme.categories, categoriesSchema)):
        messageErreur.append("Les catégories entrées ne sont pas valides.")
    
    
    # Implémenter fonction pour vérifier si nomBalise existe dans la BDD
    # Vérification du nomBalise
    
    # Creation de l'arme dans la BDD
    
    
    # En cas d'erreur
    if messageErreur != []:
        return messageErreur
    
    

    
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
