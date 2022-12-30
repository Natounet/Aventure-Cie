import {Arme, Armure, Don, FichePersonnage, ObjetMagique, ObjetDivers} from "/src/typesAnnuaire.js"


export async function load() {
    const toutLesItems = [ //ici il faut fetch les items depuis l'api. Devrait être
    //fait dans page.server.js pour que ce soit fait coté serveur
        new Arme(1, "Epée", "super épée", 10.0, 1, 10, "dé 8", 10, 1, "puissance", ["épée lourdes"], null),
        new Arme(2, "Epée", "épée nulle", 10.0, 1, 10, "dé 8", 10, 1, "puissance", ["épée lourdes"], null),
        new Arme(3, "Epée", "super épée", 10.0, 1, 10, "dé 8", 10, 1, "puissance", ["épée lourdes"], null),
        new Arme(4, "Epée", "super épée", 10.0, 1, 10, "dé 8", 10, 1, "puissance", ["épée lourdes"], null),
        new Arme(5, "Epée", "super épée", 10.0, 1, 10, "dé 8", 10, 1, "puissance", ["épée lourdes"], null),
        new Arme(6, "Epée", "super épée", 10.0, 1, 10, "dé 8", 10, 1, "puissance", ["épée lourdes"], null),
        new Arme(7, "Epée", "super épée", 10.0, 1, 10, "dé 8", 10, 1, "puissance", ["épée lourdes"], null)
    ];
    return {toutLesItems}
}