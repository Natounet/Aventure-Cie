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

class Armes {
    /**
     * 
     * @param {number} id ID unique de l'arme
     * @param {string} nom nom de l'arme, il peut y avoir plusieurs dagues avec des caractéristiques différentes
     * @param {(string|null)} descritption Description de l'arme, pas obligatoire
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
        descritption,
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
        this.nom = nom
        this.descritption = descritption
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

class Armures {
    /**
     * 
     * @param {number} id Id de l'armure
     * @param {string} nom  Nom de l'armure ( pas unique )
     * @param {string} descritption Description de l'armure
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
        descritption,
        prix,
        poids,
        armure,
        caracteristique,
        categorie,
        malusArmure,
        nomBalise
    ){
        this.id = id
        this.nom = nom
        this.descritption = descritption
        this.prix = prix
        this.poids = poids
        this.armure = armure
        this.caracteristique = caracteristique
        this.categorie = categorie
        this.malusArmure = malusArmure
        this.nomBalise = nomBalise
    } 
}

class Dons {
    /**
     * 
     * @param {string} nomBalise  id/nom du don
     * @param {string} nom Nom du don, ne peut pas être nul 30 caractères max, unique
     * @param {string} caracteristique une seule caractéristique ( ex puissance )
     * @param {string} histoire histoire du don 
     */
    constructor(
        nomBalise,
        nom,
        caracteristique,
        histoire
    ) {
        this.nomBalise = nomBalise
        this.nom = nom
        this.caracteristique = caracteristique
        this.histoire = histoire
    }
}

class CaracteristiquePersonnage {
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

class FichePersonnage {
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
        descritption,
        image
    ) {
        this.id = id 
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
        this.descritption = descritption
        this.image = image
    }
}

class ObjetMagique {
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