create database aventureCie;
use aventureCie;

-- Creation de la table des dons

CREATE TABLE IF NOT EXISTS dons(
    nomBalise varchar(100) NOT NULL UNIQUE PRIMARY KEY, -- nom de   la balise ( je sais pas ce que c'est)
    nom varchar(100) NOT NULL, -- Nom du don, ne peut pas être nul 30 caractères max
                               -- doit être unique ( pas 2 même dans la table )
    
    caracteristique varchar(100) NOT NULL, -- une seule caractéristique ( ex puissance )
    histoire text -- histoire du don
    

);

-- Creation de la table des armes

CREATE TABLE IF NOT EXISTS armes(
    id int not null AUTO_INCREMENT PRIMARY KEY, -- ID unique de l'arme
    nom varchar(100) not null, -- nom de l'arme, il peut y avoir plusieurs dagues avec des caractéristiques différentes
    description text, -- Description de l'arme, pas obligatoire
    prix float, -- prix de l'arme, nul si exemple, objet légendaire
    

    -- Caractéristiques de l'arme
    critique int not null, -- multiplicateur de coup critique ? 
    portee int not null, -- portée de l'arme en metres
    degats varchar(100) not null, -- dégat de l'arme ( 2x D8 )
    poids float not null, -- poids de l'arme  en kilos
    armure int not null, -- points d'armure apportée par l'arme

    caracteristique varchar(100) NOT NULL, -- une seule caractéristique ( ex puissance )
    categories JSON NOT NULL, -- Il peut y avoir plusieurs catégories,
    -- elles seront stockés en json

    nomBalise varchar(100), -- id du don, peut être nul quand pas de don associé

    FOREIGN KEY (nomBalise) REFERENCES dons(nomBalise)
);

-- Création de la table des armures

CREATE TABLE IF NOT EXISTS armures(
    
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT, -- Id de l'armure
    nom varchar(100) NOT NULL, -- Nom de l'armure ( pas unique )
    description text, -- Description de l'armure
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

-- Creation de la table des objets magiques

CREATE TABLE IF NOT EXISTS objetsMagiques(

    id int AUTO_INCREMENT NOT NULL PRIMARY KEY, -- Id de l'objet magique
    nom varchar(100) NOT NULL, -- nom de l'objet magique
    description text, -- description de l'objet magique ( peut être nul )
    prix float, -- prix de l'objet magique, peut être null si non achetable
    histoire text, -- Histoire de l'objet, peut être nul
    localisation text, -- lore
    utilisation varchar(100) not null, -- jour/semaine/mois/année/heure
    spam boolean not null, -- vrai / faux ( peut être utilisable à l'infini)
    coutPsyche int not null, -- coût en psyché, peut être nul
    coutVie int not null, -- coût en vie, peut être nul
    caracteristique varchar(100) NOT NULL, -- une seule caractéristique ( ex puissance )
    typeObjet varchar(100) NOT NULL , -- exemple : lunette, bottes, ...
    nomBalise varchar(100), -- Id du don si existant

    FOREIGN KEY(nomBalise) REFERENCES dons(nomBalise)

);

-- Creation de la base des fiches de personnage

CREATE TABLE IF NOT EXISTS fichePersonnage(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nom varchar(100) NOT NULL, -- Nom du personnage / Monstre
    langues JSON NOT NULL, -- langues parlées voir persoLangue.json
    taille float NOT NULl, -- Taille en mètres
    poids float NOT NULL, -- Poids en kilogrammes
    age int NOT NULL, -- Age ( entre 8 et 600 ans)
    sexe varchar(20) NOT NULL, -- Peuple du personnage
    niveau int NOT NULL, -- Niveau de montre / personnage
    biome varchar(100) NOT NULL, -- Biome
    caracteristiques JSON NOT NULL, -- Caractéristiques sous forme de JSON, voir persoCara.json
    pv int NOT NULL, -- Points de vie
    pointPsyche int NOT NULL, -- Points de psyche
    armure int NOT NULL, -- Points armure
    positionBase varchar(100), -- Position de base ( Offensive, Defensive, ...)
    competences JSON NOT NULL, -- Coompétences, voir persoComp.json
    lootPossible JSON NOT NULL, -- Loot possible, voir persoLootPossible.json
    inventaire JSON NOT NULL, -- Inventaire, voir persoInventaire.json
    equipement JSON NOT NULL, -- Equipement, voir persoEquipement.json
    facteurPuissance int NOT NULL, -- Facteur de puissance,
    dons JSON NOT NULL, -- Dons, voir persoDons.json
    description TEXT, -- Description
    image BLOB -- Image représentant le Perso/Monstre
);