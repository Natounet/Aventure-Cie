# Aventure-Cie


Tâches a réaliser
- [x] : Créer et mettre en place la base de données
- [ ]     1 - Fiche perso ( Fait appel à des items des autres tables
- [x]     2 - Dons
- [x]     3 - Armes
- [x]     4 - Armures
- [x]     5 - Objet Magiques
- [ ] : Mettre en place une recherche de fiche de personnage dans la base de données :
- [ ]     1 - par ordre alphabétique
- [ ]     2 - par catégories
- [ ]     3 - Par nom
- [ ] : Mise en place de l'annuaire
- [ ]     1 - Affichage des élements de chaques catégories
- [ ]     3 - Ajout de le posibilité de clicker sur un élement pour voir plus de détails
- [ ]     2 - Possibilité d'ajouter des élements à chaques catégories
- [ ] : Mise en place de la création de personnage
- [ ]     1 - Formulaire pour créer le personnage
- [ ]     2 - Export des caractéristiques en format PDF
- [ ] : Mise en place de la création des PNJ Aléatoires


Choix des technologies : 
  - BDD : Mysql
  - FRONT : Svelte
  - BACK : FastAPI + Svelte kit
 
Docker puis Google Cloud

Diagramme de la base de donnée

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'textColor': '#000000','primaryColor':'#FFFFFF','lineColor':'#000000'}}}%%
erDiagram


DONS{
    varchar nomBalise
    varchar nom
    varchar caracteristique 
    text histoire    
}

ARMES ||--|{ DONS: nomBalise
ARMES{ 
    int id
    varchar nom
    text description
    float prix
    int critique
    int portee
    varchar degats
    float poids
    int armure
    varchar caracteristique
    json categories
    varchar nomBalise
}


ARMURES ||--|{ DONS:nomBalise
ARMURES{
    int id
    varchar nom
    text description
    float prix
    float poids
    int armure
    varchar caracteristique
    varchar categorie
    int malusArmure
    varchar nomBalise
}

objetsMagiques ||--|{ DONS: nomBalise
objetsMagiques{
    int id
    varchar nom
    text description
    float prix
    text histoire
    text localisation
    varchar utilisation
    boolean spam
    int coutPsyche
    int coutVie
    varchar caracteristique
    varchar typeObjet
    varchar nomBalise
}

fichePersonnage{
    int id
    varchar nom
    JSON langues
    float taille
    float poids
    int age
    varchar sexe
    int niveau
    varchar biome
    json caracteristiques
    int pv
    int pointPsyche
    int armure
    varchar positionBase
    json competences
    json lootPossible
    json inventaire
    json equipement
    int facteurPuissance
    json dons
    text description
    blob image
}
```
