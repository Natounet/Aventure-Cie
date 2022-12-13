USE compagnieCie;


CREATE TABLE IF NOT EXISTS dons(
    nomBalise varchar(100) NOT NULL UNIQUE PRIMARY KEY, -- nom de   la balise ( je sais pas ce que c'est)
    nom varchar(100) NOT NULL, -- Nom du don, ne peut pas être nul 30 caractères max
                               -- doit être unique ( pas 2 même dans la table )
    
    caracteristique varchar(100) NOT NULL, -- une seule caractéristique ( ex puissance )
    histoire text -- histoire du don
    

);