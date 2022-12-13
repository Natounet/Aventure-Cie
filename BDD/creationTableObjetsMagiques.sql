USE compagnieCie;

CREATE TABLE IF NOT EXISTS objetsMagiques(

    id int AUTO_INCREMENT NOT NULL PRIMARY KEY, -- Id de l'objet magique
    nom varchar(100) NOT NULL, -- nom de l'objet magique
    description text, -- description de l'objet magique ( peut être nul )
    prix int, -- prix de l'objet magique, peut être null si non achetable
    histoire text, -- Histoire de l'objet, peut être nul
    localisation text not null, -- lore
    utlisation varchar(100) not null, -- jour/semaine/mois/année/heure
    spam boolean not null, -- vrai / faux ( peut être utilisable à l'infini)
    coutPsyche int not null, -- coût en psyché
    coutVie int not null, -- coût en vie
    caracteristique varchar(100) NOT NULL, -- une seule caractéristique ( ex puissance )
    typeObjet varchar(100) NOT NULL , -- exemple : lunette, bottes, ...
    idDon int, -- Id du don si existant

    FOREIGN KEY(idDon) REFERENCES dons(id)

);