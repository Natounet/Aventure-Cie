USE compagnieCie;


CREATE TABLE IF NOT EXISTS dons(
    id INT NOT NULL AUTO_INCREMENT UNIQUE, -- id du don, unique, permettra de récupérer des dons ailleurs
    nom varchar(30) NOT NULL, -- Nom du don, ne peut pas être nul 30 caractères max
    nomBalise varchar(20) NOT NULL UNIQUE, -- nom de la balise ( je sais pas ce que c'est)
                                           -- doit être unique ( pas 2 même dans la table )
    
    caracteristique varchar(20) NOT NULL, -- une seule caractéristique ( ex puissance )

    PRIMARY KEY(id)

);