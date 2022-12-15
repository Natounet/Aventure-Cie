USE aventureCie;

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

-- Les fichiers JSON


{   "__comment":"Langues parlées"
    "langues":["langue1", "langue2"]
}

{   "__comment":"Caractéristiques"
    "caracteristiques":[
        "puissance":"...",
        "finesse":"...",
        "vigueur":"...",
        "savoir":"...",
        "instinct":"...",
        "social":"...",
        "stress":"..."
    ]
}

{
    "__comment":"Compétences",
    "competences":[
        "nomCompetence1":"...%",
        "nomCompetence2":"...%",
        "..."

    ]
}

{
    "__comment":"Loot possible",
    "loot":[
        "nomItem":{
            "idItem": "id...",
            "quantitee":2,
        },
        "nomItem2":{
            "idItem": "id...",
            "quantitee":2,
        },
    ]
}

{
    "__comment":"Inventaire",
    "inventaire":[
        "nomItem":{
            "idItem": "id...",
            "quantitee":2,
        },
        "nomItem2":{
            "idItem": "id...",
            "quantitee":2,
        },
    ]
}


-- Equipeemnt = epee, armure ... peut pas avoir deux fois le même item
{
    "__comment":"Equipement",
    "equipement":[
        "nomItem":"idItem",
        "nomItem2":"idItem2"
    ]
}

{
    "__comment":"Dons",
    "dons":[
        "nomBalise1",
        "nomBalise2"
    ]
}

