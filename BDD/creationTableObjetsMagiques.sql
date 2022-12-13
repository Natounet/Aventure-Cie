USE compagnieCie;

CREATE TABLE IF NOT EXISTS objetsMagiques(

    id int AUTO_INCREMENT UNIQUE NOT NULL, -- Id de l'objet magique
    nom varchar(30) NOT NULL, -- nom de l'objet magique
    description varchar(1000), -- description de l'objet magique ( peut être nul )
    prix int, -- prix de l'objet magique, peut être null si non achetable
    histoire varchar(1000), -- Histoire de l'objet, peut être nul
    localisation varchar(30) not null, -- 
    utlisation varchar(10) not null, -- jour/semaine/mois/année/heure
    spam boolean not null, -- vrai / faux
    coutPsyche int not null, -- coût en psyché
    coutVie int not null, -- coût en vie
    caracteristique varchar(20) NOT NULL, -- une seule caractéristique ( ex puissance )
    typeObjet varchar(20) NOT NULL , -- exemple : lunette, bottes, ...
    idDon int, -- Id du don si existant

    PRIMARY KEY(id),
    FOREIGN KEY(idDOn) REFERENCES don(id)

)