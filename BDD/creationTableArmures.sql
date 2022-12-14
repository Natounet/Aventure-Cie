USE compagnieCie;

CREATE TABLE IF NOT EXISTS armures(
    
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT, -- Id de l'armure
    nom varchar(100) NOT NULL, -- Nom de l'armure ( pas unique )
    description text NOT NULL, -- Description de l'armure
    prix float, -- Prix de l'armure ( peut être null dans le cas d'une armure spéciale/légendaire)

    -- Caractéristiques
    poids float  NOT NULL, -- Poids de l'armure en kilo
    armure int NOT NULL, -- Poinds d'armure

    caracteristique varchar(100) NOT NULL, -- une seule caractéristique ( ex puissance )
    categorie varchar(100) NOT NULL,  -- Il peut y avoir que une catégorie par armure
    malusArmure int NOT NULL, -- Malus lié au poids de l'armure ( -5 => -50% )

    nomBalise varchar(100), -- id du don, peut être nul quand pas de don associé
    
    
    FOREIGN KEY (nomBalise) REFERENCES dons(nomBalise)


);

