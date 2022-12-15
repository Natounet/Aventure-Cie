from mysql.connector import connect, DatabaseError, InterfaceError, MySQLConnection
from decouple import config # Pour récuperer des variables d'environnement

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
        print(f"Ces erreurs ce sont produites : {Error}")
        
    return connexion

def nomBaliseDansBDD(nomBaliseEntree: str) -> bool:
    """ Fonction vérifiant si un nom de balise existe dans la BDD
        Retourne True si il existe, false sinon"""
        
    connexion = connexionBDD()
    if connexion is not None:
        cursor = connexion.cursor()
        cursor.execute("SELECT nomBalise FROM dons;")
        for nomBalise in cursor.fetchall():
            if nomBaliseEntree == nomBalise[0]: # Si le nomBalise est présent dans la table
                connexion.close() # Fermeture de la connexion
                return True
        
        connexion.close() # Fermeture de la connexion
        return False # Nom balise non présent dans la table
        
    return False # Une erreur s'est produite
        
        
