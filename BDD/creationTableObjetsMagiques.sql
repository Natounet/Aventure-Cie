USE aventureCie;

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

