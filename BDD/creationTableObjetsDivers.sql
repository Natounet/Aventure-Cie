
CREATE TABLE IF NOT EXISTS objetsDivers(
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY , -- ID de l'objet divers
    nom varchar(30) NOT NULL, -- Dénomination de 'l'objet
    description text, -- Description de l'objet
    prix int, -- Prix de l'objet
    taille float not null, -- Taille de l'objet
    poids float not null, -- Poids de l'objet
    armure int -- Points d'armure dans des cas précis
)