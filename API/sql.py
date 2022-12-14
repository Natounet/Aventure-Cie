from mysql.connector import connect, DatabaseError, InterfaceError, MySQLConnection
from decouple import config # Pour récuperer des variables d'environnement
import json
import classes

""" Cette classe s'occupe de tout ce qui est en lien avec la base de données 
    Gère la connexion et fait les requêtes """


### SETTINGS ###

USER = "root"
PASSWORD = config('dbPassword')
HOST = "localhost"
DATABASE = "aventureCie"






def connexionBDD() -> MySQLConnection:
    """ Fonction se connectant à la base de donnée
        Retourne un objet connexion à la BDD ou None si erreur
        Peut être utilisé avec cursor() pour envoyer des requêtes
        La connexion doit être fermée après utilisation """
        
    connexion = None

    try:
        connexion = connect(host=HOST, user=USER, password=PASSWORD,database=DATABASE)
      
    except (DatabaseError, InterfaceError) as Error:
        print(f"Ces erreurs ce sont produites lors de l'ajout d'une arme : {Error}")
        
    return connexion

def nomBaliseDansBDD(nomBaliseEntree: str) -> bool:
    """ Fonction vérifiant si un nom de balise existe dans la BDD
        Retourne True si il existe, false sinon"""
        
    connexion = connexionBDD()
    if connexion is not None:
        cursor = connexion.cursor()
        cursor.execute("SELECT nomBalise FROM dons WHERE nomBalise=%(nomBalise)s",{'nomBalise':nomBaliseEntree})
        
        if cursor.fetchall() != []: # nom balise présent dans la table
            connexion.close()
            return True
                
        connexion.close() # Fermeture de la connexion
        return False # Nom balise non présent dans la table
        
    return False # Une erreur s'est produite
        
def idArmeDansBDD(idArme: int) -> bool:
    
    connexion = connexionBDD()
    if connexion is not None:
        cursor = connexion.cursor()
        cursor.execute("SELECT id FROM armes WHERE id=%(idArme)s",{'idArme':idArme})
        
        if cursor.fetchall() != []: # nom balise présent dans la table
            connexion.close()
            return True
                
        connexion.close() # Fermeture de la connexion
        return False # Nom balise non présent dans la table
        
    return False # Une erreur s'est produite

def idArmureDansBDD(idArmure: int) -> bool:
    
    connexion = connexionBDD()
    if connexion is not None:
        cursor = connexion.cursor()
        cursor.execute("SELECT id FROM armures WHERE id=%(idArmure)s",{'idArmure':idArmure})
        
        if cursor.fetchall() != []: # nom balise présent dans la table
            connexion.close()
            return True
                
        connexion.close() # Fermeture de la connexion
        return False # Nom balise non présent dans la table
        
    return False # Une erreur s'est produite


def idObjetMagiquesDansBDD(idObjetsMagiques: int) -> bool:
    
    connexion = connexionBDD()
    if connexion is not None:
        cursor = connexion.cursor()
        cursor.execute("SELECT id FROM objetsMagiques WHERE id=%(idObjetsMagiques)s",{'idObjetsMagiques':idObjetsMagiques})
        
        if cursor.fetchall() != []: # nom balise présent dans la table
            connexion.close()
            return True
                
        connexion.close() # Fermeture de la connexion
        return False # Nom balise non présent dans la table
        
    return False # Une erreur s'est produite


def idObjetDiversDansBDD(idObjetDivers: int) -> bool:
    
    connexion = connexionBDD()
    if connexion is not None:
        cursor = connexion.cursor()
        cursor.execute("SELECT id FROM objetsDivers WHERE id=%(idObjetDivers)s",{'idObjetDivers':idObjetDivers})
        
        if cursor.fetchall() != []: # nom balise présent dans la table
            connexion.close()
            return True
                
        connexion.close() # Fermeture de la connexion
        return False # Nom balise non présent dans la table
        
    return False # Une erreur s'est produite


def creerDonDansLaBDD(don: classes.Don) -> bool:
    """ Fonction permettant d'ajouter un don dans la base de donnée 
        Prends en paramètre un don sous la forme d'un objet don 
        Retourne True si le don a été ajouté,
        False sinon """
        
    connexion = connexionBDD()
    
    try:
        if connexion is not None:
            
            cursor = connexion.cursor()
            query = "INSERT INTO dons VALUES(%(nomBalise)s,%(nom)s,%(caracteristique)s,%(histoire)s);"
            donnees = {"nomBalise":don.nomBalise,"nom":don.nom,"caracteristique":don.caracteristique,"histoire":don.histoire}
            # Création de la commande
            cursor.execute(query,donnees)
            
            # Ajout du don
            connexion.commit()
            
            connexion.close()
            return True # Création effectuée
    
    except (DatabaseError, InterfaceError) as Error:
            connexion.close()
            print("Il y a une erreur lors de l'ajout du don " + str(Error))
            return False
    
    return False # Il y a eu une erreur dans la connexion

def creerArmeDansLaBDD(arme: classes.Arme):
    """ Fonction permettant de créer une arme dans la base de données
        Prends en paramètre un objet arme
        Retourne true si l'arme a été crée
        False sinon 
        
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
    
    connexion = connexionBDD()
    try: 
        if connexion is not None:
            
            cursor = connexion.cursor()
            query = """INSERT INTO armes(nom,description,prix,critique,portee,degats,poids,armure,caracteristique,categories,nomBalise)
                    VALUES(%(nom)s,%(description)s,%(prix)s,%(critique)s,%(portee)s,
                    %(degats)s,%(poids)s,%(armure)s,%(caracteristique)s,
                    %(categories)s,%(nomBalise)s)"""
            
            params = {"nom":arme.nom,"description":arme.description,"prix":arme.prix,"critique":arme.critique,
                    "portee":arme.portee,"degats":arme.degats,"poids":arme.poids,"armure":arme.armure,"caracteristique":arme.caracteristique,
                    "categories":json.dumps(arme.categories),"nomBalise":arme.nomBalise}


            cursor.execute(query,params)
            connexion.commit()
            
            connexion.close()
            return True
        
    except (DatabaseError, InterfaceError) as Error:
            connexion.close()
            print(Error)
            return False

    return False
        
def creerArmureDansLaBDD(armure: classes.Armure) -> bool:
    """ Fonction permettant de créer une armure dans la base de données
        Prends en paramètre un objet armure
        Retourne true si l'armure a été crée
        False sinon 
        
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

    connexion = connexionBDD()
    
    if connexion is not None:
        try:
            
            cursor = connexion.cursor()
            
            query = """ INSERT INTO armures(nom,description,prix,poids,armure,caracteristique,categorie,malusArmure,nomBalise)
                        VALUES (%(nom)s,%(description)s,%(prix)s,%(poids)s,%(armure)s,
                        %(caracteristique)s,%(categorie)s,%(malusArmure)s,%(nomBalise)s)"""
                        
            params = {"nom":armure.nom,"description":armure.description,"prix":armure.prix,"poids":armure.poids,
                    "armure":armure.armure, "caracteristique":armure.caracteristique,"categorie":armure.categorie,"malusArmure":armure.malusArmure,
                    "nomBalise":armure.nomBalise}    
            
            cursor.execute(query,params)
            
            connexion.commit()
            
            return True
        
        except (DatabaseError, InterfaceError) as Error:
            connexion.close()
            print("Il y a une erreur lors de l'ajout de l'armure " + str(Error))
            return False
    
    return False

def creerObjetMagiqueDansLaBDD(objetMagique: classes.objetMagique) -> bool:
    """ Fonction permettant de créer un objet magique dans la base de données
        Prends en paramètre un objet magique
        Retourne true si l'objet a été crée
        False sinon 
        
        
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
    
    connexion = connexionBDD()
    
    if connexion is not None:
        try:
            cursor = connexion.cursor()
            
            query = """INSERT INTO objetsMagiques(nom,description,prix,histoire,localisation
                    ,utilisation,spam,coutPsyche,coutVie,caracteristique,typeObjet,nomBalise)
                VALUES (%(nom)s,%(description)s,%(prix)s,%(histoire)s,%(localisation)s,%(utilisation)s
                ,%(spam)s,%(coutPsyche)s,%(coutVie)s,%(caracteristique)s,%(typeObjet)s,%(nomBalise)s
                )
            """
            
            values = {"nom":objetMagique.nom,"description":objetMagique.description,"prix":objetMagique.prix,"histoire":objetMagique.histoire,
                      "localisation":objetMagique.localisation,"utilisation":objetMagique.utilisation,"spam":objetMagique.spam,
                      "coutPsyche":objetMagique.coutPsyche,"coutVie":objetMagique.coutVie,"caracteristique":objetMagique.caracteristique,
                      "typeObjet":objetMagique.typeObjet,"nomBalise":objetMagique.nomBalise}
            
            cursor.execute(query,values)
            
            connexion.commit()
            
            connexion.close()
            
            return True
        
        except (DatabaseError, InterfaceError) as Error:
            connexion.close()
            print("Il y a une erreur lors de l'ajout de l'objet magique " + str(Error))
            return False
        
    return False


def creerObjetDiversDansLaBDD(objetDiv: classes.objetDivers) -> bool:
    """ Fonction permettant de créer un objet divers dans la base de données
        Prends en paramètre un objet divers
        Retourne true si l'objet a été crée
        False sinon 
        
        * nom: str # nom de l'objet divers
        * description: Union[str, None] # Dénomination de 'l'objet
        * prix: Union[float, None] # Description de l'objet
        * taille: float # Prix de l'objet
        * poids: float # Poids de l'objet
        * armure: Union[int, None] # Points d'armure dans des cas précis
    """
    
    connexion = connexionBDD()
    
    if connexion is not None:
        try:
            
            cursor = connexion.cursor()
            
            query = """ INSERT INTO objetsDivers
                        (nom,description,prix,taille,poids,armure)
                        VALUES(%(nom)s,%(description)s,%(prix)s,%(taille)s,%(poids)s,%(armure)s);"""
            
            params = {"nom":objetDiv.nom,"description":objetDiv.description,"prix":objetDiv.prix,"taille":objetDiv.taille,
                      "poids":objetDiv.poids,"armure":objetDiv.armure}
            
            cursor.execute(query,params)
            
            connexion.commit()
            
            connexion.close()
            
            return True
        
        except (DatabaseError, InterfaceError) as Error:
            print(Error)
            connexion.close()
            return False
    
    return False


def creerPersonnageDansBDD(perso: classes.Perso) -> bool:
    """ Fonction permettant de créer un personnage dans la base de données
        Prends en paramètre un personnage
        Retourne true si le personnage a été crée
        False sinon 
        
        
        * nom: str # Nom du personnage
        * langues: list # Langues parlées par le personnage
        * taille: float # Taille du personnage
        * poids: float # Poids du personnage
        * age: int # Age du personnage
        * peuple: str # Peuple du personnage
        * niveau: int # Niveau du personnage
        * biome: str # Biome du personnage
        * caracteristiques: dict # Caractéristiques du personnages ( Puissance, Vigueur, ..)
        * pointVie: int # Points de vie
        * pointPsyche: int # Points de psyché
        * armure: int # Points d'armure
        * positionBase: Union[str, None] # Position de base du personnage si indiqué
        * competences: list # Compétences du personnage + caracterisitque liée ( Puissance, Vigueur )
        * lootPossible: dict # loot possible du personnage
        * inventaire: dict # Inventaire du personnage
        * equipement: dict # Equipement du personnage
        * facteurPuissance: int # Facteur de puissance
        * dons: list # Dons du personnage
        * description: Union[str, None] # Description si existante du personnage
        
    """    
    
    connexion = connexionBDD()
    
    if connexion is not None:
        
        try:
            cursor = connexion.cursor()
            
            query = """
                        INSERT INTO fichePersonnage(
                            nom,langues,taille,poids,age,peuple,niveau,biome,caracteristiques,
                            pointVie,pointPsyche,armure,positionBase,competences,lootPossible, inventaire,
                            equipement,facteurPuissance,dons,description)
                        VALUES(
                            %(nom)s,%(langues)s,%(taille)s,%(poids)s,%(age)s,%(peuple)s,%(niveau)s,%(biome)s,%(caracteristiques)s
                            ,%(pointVie)s,%(pointPsyche)s,%(armure)s,%(positionBase)s,%(competences)s
                            ,%(lootPossible)s,%(inventaire)s,%(equipement)s,%(facteurPuissance)s,%(dons)s,%(description)s);"""
                            
            params = {"nom":perso.nom,"langues":json.dumps(perso.langues),"taille":perso.taille,"poids":perso.poids,"age":perso.age,"peuple":perso.peuple,
                      "niveau":perso.niveau,"biome":perso.biome,"caracteristiques":json.dumps(perso.caracteristiques),"pointVie":perso.pointVie,
                      "pointPsyche":perso.pointPsyche,"armure":perso.armure,"positionBase":perso.positionBase,"competences":json.dumps(perso.competences),
                      "lootPossible":json.dumps(perso.lootPossible),"inventaire":json.dumps(perso.inventaire),"equipement":json.dumps(perso.equipement),
                      "facteurPuissance":perso.facteurPuissance,"dons":json.dumps(perso.dons),"description":perso.description}
            
            cursor.execute(query,params)
            
            connexion.commit()
            
            connexion.close()
            
            return True
        except (DatabaseError, InterfaceError) as Error:
            print("Erreur lors de la création d'un personnage :" + str(Error))
            connexion.close()
            return False
        
    return False