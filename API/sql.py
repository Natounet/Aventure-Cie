from mysql.connector import connect, DatabaseError, InterfaceError, MySQLConnection
from decouple import config # Pour récuperer des variables d'environnement
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
        print(f"Ces erreurs ce sont produites : {Error}")
        
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
        

def creerDonDansLaBDD(don: classes.Don) -> bool:
    """ Fonction permettant d'ajouter un don dans la base de donnée 
        Prends en paramètre un don sous la forme d'un objet don 
        Retourne True si le don a été ajouté,
        False sinon """
        
    connexion = connexionBDD()
    if connexion is not None:
        
        cursor = connexion.cursor()
        query = "INSERT INTO dons VALUES(%(nomBalise)s,%(nom)s,%(caracteristique)s,%(histoire)s);"
        donnees = {"nomBalise":don.nomBalise,"nom":don.nom,"caracteristique":don.caracteristique,"histoire":don.histoire}
        # Création de la commande
        cursor.execute(query,donnees)
        
        # Ajout du don
        connexion.commit()
        
        connexion.close()
        return True
    
    
    
    
    return False # Il y a eu une erreur dans la connexion

