USE compagnieCie;

CREATE TABLE IF NOT EXISTS armes(
    id int not null AUTO_INCREMENT unique, -- ID unique de l'arme
    nom varchar(30) not null, -- nom de l'arme, il peut y avoir plusieurs dagues avec des caractéristiques différentes
    description varchar(1000), -- Description de l'arme, pas obligatoire
    prix int, -- prix de l'arme, nul si exemple, objet légendaire
    

    -- Caractéristiques de l'arme
    critique int not null, -- multiplicateur de coup critique ? 
    portee int not null, -- portée de l'arme en metres
    degat varchar(10) not null, -- dégat de l'arme ( 2x D8 )
    poids int not null, -- poids de l'arme de l'arme en kilo
    armure int not null, -- points d'armure apportée par l'arme

    caracteristique varchar(20) NOT NULL, -- une seule caractéristique ( ex puissance )
    categories JSON NOT NULL, -- Il peut y avoir plusieurs catégories,
    -- elles seront stockés en json

    idDon int, -- id du don, peut être nul quand pas de don associé

    PRIMARY KEY(id),
    FOREIGN KEY (idDon) REFERENCES don(id)
)

