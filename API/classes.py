from pydantic import BaseModel
from typing import Union # Permet de définir plusieurs types possible à une variable


class Don(BaseModel):
    nom: str # Nom descriptif du don
    nomBalise: str # nom unique du don
    caracteristique: str # Caractéristique du don (ex: Puissance)
    histoire: Union[str, None] # Histoire du don, peut être nul
    
class Arme(BaseModel):
    nom: str # Nom de l'arme
    description: Union[str, None] # Description de l'arme, peut être nul
    prix: Union[float, None] # Prix de l'arme, peut être nul
    critique: int # mutliplicateur de coûts critiques
    portee: int # Portée en mètres de l'arme
    degats: str # Quels dés de dégats ( ex: 2 D8)
    poids: float # Poids de l'arme en kilo
    armure: int # Bonus/Malus d'armure
    caracteristique: str # Caractéristique de l'arme ( ex : Puissance )
    categories: list # Catégorise SOUS LA FORME D'UN JSON
    nomBalise: Union[str, None] # NomBalise du don qu'il possède si existant ( peut être nul)
 
class Armure(BaseModel):
    nom: str # Nom de l'armure
    description: Union[str,None] # Description de l'armure ( peut ne pas être présente )
    prix: Union[float, None] # Prix de l'armure ( peut ne pas être présente )
    poids: float # Poids de l'armure
    armure: int # Points d'armure
    caracteristique: str # Caractéristique dépendante de l'arme ( ex: Puissance )
    categorie: str # Catégorie de l'armure ( type d'armure, voir config.py )
    malusArmure: int # Malus lié au poids de l'armure ( -5 = -5% )
    nomBalise: Union[str, None] # nomBalise du don associé si présent


class objetMagique(BaseModel):
    nom: str # Nom de l'objet magique
    description: Union[str,None] # Description de l'objet magique ( peut ne pas être donné)
    prix: Union[float, None] # Prix de l'objet, ( peut ne pas être donné)
    histoire: Union[str, None] # Histoire de l'objet ( peut ne pas être donné)
    localisation: Union[str, None] # Lore de l'objet ( peut ne pas être donné)
    utilisation: str # Utilisation tous les x temps ( ) jour/semaine/mois/année/heure
    spam: bool # Peut être utilisable à l'infini 
    coutPsyche: int # Cout en psyche de l'objet
    coutVie: int # Cout en vie de l'objet
    caracteristique: str # Caracteristique, ex : Puissance
    typeObjet: str # Type de l'objet magique exemple : lunette, bottes, ...
    nomBalise: Union[str, None] # nom du don lié à l'objet ( peut ne pas être donné)

class objetDivers(BaseModel):
    nom: str # nom de l'objet divers
    description: Union[str, None] # Dénomination de 'l'objet
    prix: Union[float, None] # Description de l'objet
    taille: float # Prix de l'objet
    poids: float # Poids de l'objet
    armure: Union[int, None] # Points d'armure dans des cas précis


