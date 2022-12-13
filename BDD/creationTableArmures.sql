USE compagnieCie;

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