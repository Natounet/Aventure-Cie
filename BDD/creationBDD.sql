create database compagnieCie;

-- Creation des dons

CREATE TABLE IF NOT EXISTS dons(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, -- id du don, unique, permettra de récupérer des dons ailleurs
    nom varchar(100) NOT NULL, -- Nom du don, ne peut pas être nul 30 caractères max
    nomBalise varchar(100) NOT NULL UNIQUE, -- nom de la balise ( je sais pas ce que c'est)
                                           -- doit être unique ( pas 2 même dans la table )
    
    caracteristique varchar(100) NOT NULL -- une seule caractéristique ( ex puissance )

    

);

-- Creation des armes 

CREATE TABLE IF NOT EXISTS armes(
    id int not null AUTO_INCREMENT PRIMARY KEY, -- ID unique de l'arme
    nom varchar(100) not null, -- nom de l'arme, il peut y avoir plusieurs dagues avec des caractéristiques différentes
    description text, -- Description de l'arme, pas obligatoire
    prix int, -- prix de l'arme, nul si exemple, objet légendaire
    

    -- Caractéristiques de l'arme
    critique int not null, -- multiplicateur de coup critique ? 
    portee int not null, -- portée de l'arme en metres
    degat varchar(100) not null, -- dégat de l'arme ( 2x D8 )
    poids int not null, -- poids de l'arme de l'arme en kilo
    armure int not null, -- points d'armure apportée par l'arme

    caracteristique varchar(100) NOT NULL, -- une seule caractéristique ( ex puissance )
    categories JSON NOT NULL, -- Il peut y avoir plusieurs catégories,
    -- elles seront stockés en json

    idDon int, -- id du don, peut être nul quand pas de don associé

    FOREIGN KEY (idDon) REFERENCES dons(id)
);

-- Creation des armures

CREATE TABLE IF NOT EXISTS armures(
    
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT, -- Id de l'armure
    nom varchar(100) NOT NULL, -- Nom de l'armure ( pas unique )
    description text NOT NULL, -- Description de l'armure
    prix int, -- Prix de l'armure ( peut être null dans le cas d'une armure spéciale/légendaire)

    -- Caractéristiques
    poids int  NOT NULL, -- Poids de l'armure en kilo
    armure int NOT NULL, -- Poinds d'armure

    caracteristique varchar(100) NOT NULL, -- une seule caractéristique ( ex puissance )
    categories varchar(100),  -- Il peut y avoir que une catégorie par armure


    idDon int, -- id du don, peut être nul quand pas de don associé
    
    
    FOREIGN KEY (idDon) REFERENCES dons(id)


);

-- Creation des objets magiques 