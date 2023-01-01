/**
 * Dans ce fichier son définis tout les types de truc qui peuvent se trouver
 * dand l'annuaire.
 * Cela comprends :
 * - Armes
 * - Armures
 * - Dons
 * - Fiche de personnage = Créatures
 * - Objets Magiques  
 * 
 * TODO : ajouter des methodes parse/jsonify pour convertir entre json et objet
 */

import { PlageNumeraire } from "./routes/bestiaire/filtre"

export class Arme {
    static nomType = "Arme"

    /**
     * 
     * @param {number} id ID unique de l'arme
     * @param {string} nom nom de l'arme, il peut y avoir plusieurs dagues avec des caractéristiques différentes
     * @param {(string|null)} description Description de l'arme, pas obligatoire
     * @param {number} prix prix de l'arme, nul si exemple, objet légendaire
     * @param {number} critique multiplicateur de coup critique ? 
     * @param {number} portee portée de l'arme en metres
     * @param {string} degats dégat de l'arme ( 2x D8 )
     * @param {number} poids poids de l'arme  en kilos 
     * @param {number} armure  points d'armure apportée par l'arme
     * @param {string} caracteristique une seule caractéristique ( ex puissance )
     * @param {string[]} categories Il peut y avoir plusieurs catégories
     * @param {(string|null)} nomBalise id du don, peut être nul quand pas de don associé
     */
    constructor(
        id,
        nom,
        description,
        prix,
        critique,
        portee,
        degats,        
        poids,
        armure,
        caracteristique,
        categories,
        nomBalise
    ) {
        this.id = id
        this.nomType = Arme.nomType;
        this.nom = nom
        this.description = description
        this.prix = prix
        this.critique = critique
        this.portee = portee
        this.degats = degats        
        this.poids = poids
        this.armure = armure
        this.caracteristique = caracteristique
        this.categories = categories
        this.nomBalise = nomBalise 
    }
}

export class Armure {
    static nomType = "Armure"
    
    /**
     * 
     * @param {number} id Id de l'armure
     * @param {string} nom  Nom de l'armure ( pas unique )
     * @param {string} description Description de l'armure
     * @param {(number | null)} prix Prix de l'armure ( peut être null dans le cas d'une armure spéciale/légendaire)
     * @param {number} poids Poids de l'armure en kilo
     * @param {number} armure Points d'armure 
     * @param {string} caracteristique une seule caractéristique ( ex puissance )
     * @param {string} categorie Il peut y avoir que une catégorie par armure 
     * @param {number} malusArmure Malus lié au poids de l'armure ( -5 => -50% ) 
     * @param {string} nomBalise id du don, peut être nul quand pas de don associé 
     */
    constructor(
        id,
        nom,
        description,
        prix,
        poids,
        armure,
        caracteristique,
        categorie,
        malusArmure,
        nomBalise
    ){
        this.id = id
        this.nomType = Armure.nomType;
        this.nom = nom
        this.description = description
        this.prix = prix
        this.poids = poids
        this.armure = armure
        this.caracteristique = caracteristique
        this.categorie = categorie
        this.malusArmure = malusArmure
        this.nomBalise = nomBalise
    } 
}

export class Don {
    static nomType = "Don"
    
    /**
     * 
     * @param {number} id  id/nom du don
     * @param {string} nom Nom du don, ne peut pas être nul 30 caractères max, unique
     * @param {string} caracteristique une seule caractéristique ( ex puissance )
     * @param {string} histoire histoire du don 
     */
    constructor(
        id,
        nom,
        caracteristique,
        histoire
    ) {
        this.id = id
        this.nomType = Don.nomType;
        this.nom = nom
        this.caracteristique = caracteristique
        this.histoire = histoire
    }
}

export class CaracteristiquePersonnage {
    /**
     * 
     * @param {number} puissance /100
     * @param {number} finesse /100
     * @param {number} vigueur /100
     * @param {number} savoir /100
     * @param {number} instinct /100
     * @param {number} social /100
     * @param {number} stress /100
     */
    constructor (
        puissance,
        finesse,
        vigueur,
        savoir,
        instinct,
        social,
        stress
    ) {
        this.puissance = puissance
        this.finesse = finesse
        this.vigueur = vigueur
        this.savoir = savoir
        this.instinct = instinct
        this.social = social
        this.stress = stress
    }
}

export class FichePersonnage {
    static nomType = "Créature"
    
    /**
     * 
     * @param {number} id 
     * @param {string} nom 
     * @param {string[]} langue 
     * @param {number} taille 
     * @param {number} poids 
     * @param {number} age 
     * @param {string} sexe 
     * @param {number} niveau 
     * @param {string} biome 
     * @param {CaracteristiquePersonnage} caracteristique 
     * @param {number} pv 
     * @param {number} pointPsyche 
     * @param {number} armure 
     * @param {string} positionBase 
     * @param {Object} competences 
     * @param {Object} inventaire 
     * @param {Object} equipement 
     * @param {number} facteurPuissance 
     * @param {string[]} dons tableau de nom balise
     * @param {string | null} description 
     * @param {Blob | null} image lazy loading ! On ne va chercher l'image qu'au
     * dernier moment, et on ne la parse pas en json.
     */
    constructor (
        id, 
        nom,
        langue,
        taille,
        poids,
        age,
        sexe,
        niveau,
        biome,
        caracteristique,
        pv,
        pointPsyche,
        armure,
        positionBase,
        competences,
        inventaire,
        equipement,
        facteurPuissance,
        dons,
        description,
        image
    ) {
        this.id = id 
        this.nomType = FichePersonnage.nomType;
        this.nom = nom
        this.langue = langue
        this.taille = taille
        this.poids = poids
        this.age = age
        this.sexe = sexe
        this.niveau = niveau
        this.biome = biome
        this.caracteristique = caracteristique
        this.pv = pv
        this.pointPsyche = pointPsyche
        this.armure = armure
        this.positionBase = positionBase
        this.competences = competences
        this.inventaire = inventaire
        this.equipement = equipement
        this.facteurPuissance = facteurPuissance
        this.dons = dons
        this.description = description
        this.image = image
    }
}

export class ObjetMagique {
    static nomType = "Objet Magique"
    
    /**
     * 
     * @param {number} id 
     * @param {string} nom 
     * @param {string | null} description 
     * @param {number | null} prix 
     * @param {string | null} histoire 
     * @param {string | null} localisation 
     * @param {string} utilisation 
     * @param {boolean} spam 
     * @param {number} coutPsyche 
     * @param {number} coutVie 
     * @param {string} caracteristique 
     * @param {string} typeObjet 
     * @param {string | null} nomBalise 
     */
    constructor (
        id,
        nom,
        description,
        prix,
        histoire,
        localisation,
        utilisation,
        spam,
        coutPsyche,
        coutVie,
        caracteristique,
        typeObjet,
        nomBalise
    ) {
        this.id = id
        this.nomType = ObjetMagique.nomType;
        this.nom = nom
        this.description = description
        this.prix = prix
        this.histoire = histoire
        this.localisation = localisation
        this.utilisation = utilisation
        this.spam = spam
        this.coutPsyche = coutPsyche
        this.coutVie = coutVie
        this.caracteristique = caracteristique
        this.typeObjet = typeObjet
        this.nomBalise = nomBalise
    }
}

export class ObjetDivers {
    static nomType = "Objets"
    
    /**
     * 
     * @param {Number} id 
     * @param {string} nom 
     * @param {string|null} description 
     * @param {Number|null} prix 
     * @param {Number} taille 
     * @param {Number} poids 
     * @param {Number|null} armure 
     */
    constructor(
        id,
        nom,
        description,
        prix,
        taille,
        poids,
        armure
    ) {
        this.id = id
        this.nomType = ObjetDivers.nomType;
        this.nom = nom
        this.description = description
        this.prix = prix
        this.taille = taille
        this.poids = poids
        this.armure = armure
    }
}

/**
 * Associe les identifiant des attributs des différents types
 * d'item au nom de cet attribut. Par exemple, l'attribut 
 * "pointVie" a pour nom "Points de Vie".
 * Si un attribut n'est pas dans la table, c'est que
 * que son identifiants est son nom. Par exemple "age" à comme 
 * nom "age".
 */
// export const attributesnomTypes = {
//     "id" : "identifiant",
//     "critique": "Multiplicateur Critique",
//     "nomBalise": "Don associé",
//     "malusArmure" : "Malus d'armure",
//     "pointVie": "Points de Vie",
//     "pointPsyche": "Point de Psychée",
//     "positionBase": "Position par défault",
//     "competences": "Compétences",
//     "lootPossible": "Loots Possibles",
//     "equipement": "Equipement",
//     "facteurPuissance": "Facteur de puissance",
//     "coutPsyche": "Cout en psychée",
//     "coutVie": "Cout en vie",
//     "typeObjet": "Type d'objet",
// }