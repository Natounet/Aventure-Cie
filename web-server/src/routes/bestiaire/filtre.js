/**
 * Classe mère des filtres, qui correspond a l'abscence de filtre. Un filtre a 
 * des paramètres, définis par l'utilisateur, et chaque type de typesAnnuaire.js
 * a un dictionnaire statique qui associe certains champs a un filtre.
 * Par exemple, le type FichePersonnage a un attribut taille, qui sera 
 * associé a un filtre de type PlageNumeraire, par un dictionnaire (filtres). 
 * Les paramètre de ce filtre sont un minimum et un maximum. Dans l'interface, 
 * l'utilisateur pourra modifier ces paramètres, et la méthode tester() de 
 * PlageNumeraire retournera true que si la taille est comprise entre maximum et 
 * minimum. On pourra ensuite appeler passeFiltre() sur n'importe quelle instance
 * de n'importe quel type pour savoir si l'instance passe les filtres paramétrés
 * par l'utilisateur.
 * Ce système de type de filtre permet de savoir quoi afficher dans l'interface,
 * par exemple la taille sera géré par un slider, alors que les langues seront
 * géré par l'utilisateur avec des cases a cocher. Pour garantir une flexibilité
 * maximale, chaque champs de chaque type d'item qu'on peut trouver dans 
 * l'annuaire est associé a un filtre, si demain on veut rajouter un nouveau, on
 * a juste a lui associer le bon filtre et l'interface ce génera correctement.
 * 
 * Enfin, une version plus evoluée pourrait être obtenue en ajouter une méthode
 * score() pour chacun des filtres, pour trouver les trucs de l'annuaires les 
 * plus proches de ce que l'utilisateur tape dans la barre de recherche.
 */
export class Filtre {
    constructor(actif, name) {
        this.actif = actif
        this.name = name
    }

    /**
     * La fonction tester est la fonction qui vérifie si une valeure passe le 
     * filtre.
     * @param {Object} valeur 
     * @returns {boolean} true si la valeur passe le filtre, false sinon.
     */
    tester(valeur) {
        return true
    }
}

/**
 * Plage numéraire est un filtre qui prends a un maximum et un minimum, et 
 * retourne true si la valeur est comprise entre les deux, sinon elle retourne
 * false.
 */
export class PlageNumeraire extends Filtre {
    constructor (actif, name, min, max) {
        super(actif, name)
        this.min = min
        this.max = max
        this.borneInf = min
        this.borneSup = max
    }
    
    /**
     * 
     * @param {number} valeur une valeur numérique
     * @returns true si la valeur est entre le minimum et le maximum
     */
    tester(valeur) {
        return this.borneInf <= valeur && this.borneSup >= valeur
    }
}

/**
 * ListeCochable est un filtre qui prends a un attribut qui donne la liste des 
 * valeur possibles pour l'attribut auxquel est associé le filtre, et pour 
 * chacune de ces valeurs possible, un booléen qui dit si la valeur passe le 
 * filtre ou non.
 * Concrètement, l'utilisateur vera une liste de cases a cocher, et cochera les
 * valeurs qu'il veut filtrer. Par exemple, l'attribut "langue" des fiches de 
 * personnage sera associé a un filtre de type ListeCochable, qui aura comme
 * valeur possible toutes les langues du jeu, et l'utilisateur pourra cocher
 * les langues qu'il veut. 
 */
export class ListeCochable {

}

/**
 * DistanceLexicographique est un filtre qui a comme attibut la recherche qu'a
 * mis le joueurs. Le filtre retourne true selon des critère de distance
 * lexicographique.
 * Il n'y aura donc qu'un seul champs par type de truc dans l'annuaire qui aura
 * comme filtre DistanceLexicographique, en général le nom du truc.
 * Exemple : si l'utilisateur tape "Cocatrix" dans la barre de recherche, les 
 * nom "Cocatrix dorée" ou "Cocatrix des Alpes" devrait passé le filtre (donc 
 * tester() devrait retourner true quand on lui donne un de ces noms en paramètre)
 */
export class DistanceLexicographique {

}

