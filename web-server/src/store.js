import { init } from 'svelte/internal';
import { writable } from 'svelte/store';

var psy,pv 
var a_repartir=[]

const nom_caracterisique=["Puissance","Finesse","Vigueur","Savoir","instinct","Social","Stress"]
const indice_cara={"Puissance":0,"Finesse":1,"Vigueur":2,"Savoir":3,"instinct":4,"Social":5,"Stress":6}
const bonus=0
const malus=1
class modification_people{
    constructor(nb_point, characteristics){
        this.nb_point =nb_point;
        this.characteristics =characteristics;
        this.index_char={"Puissance":0,"Finesse":1,"Vigueur":2,"Savoir":3,"instinct":4,"Social":5,"Stress":6}
        this.tab_possibilitys=creation_tab_possibilitys(characteristics,this.index_char)
        this.isbonus=isbonus_method(nb_point)
    }
    static creation_tab_possibilitys(characteristics_args,index_char_args) {
        var tab=new Array(7).fill(false)
        characteristics_args.forEach(element => {
            tab[index_char_args[element]]=true
        });
        return tab
    }
    static isbonus_method(nb_point_args){
        return nb_point_args>=0;
}
}
class attribut{
    constructor(name,description,bonus,characteristics_affecte) {
        this.name_atribut=name;
        this.name_atribut=description;
        this.bonus_points=bonus;
        this.isbonus=isbonus_method(bonus);
        this.characteristics_affecte=characteristics_affecte
    }
    static isbonus_method(bonus_args){
        return i>=0;
    }
}
class personnage{
    constructor(peuple){
        this.peuple=peuple;
        this.pv;
        this.ps;
        this.a_repartir;
        this.attribut=[];
        this.characteristics=["Puissance","Finesse","Vigueur","Savoir","instinct","Social","Stress"]
    }
    static configuration_pour_peuple(peuple){
        switch(peuple){
            case "nain":
                this.pv=21
                this.psy=8
                this.a_repartir=[new modification_people(-10,["Puissance","Finesse","Savoir","Social"]),new modification_people(20,["Savoir","Social"])]
                this.ajout_attribut("vision dans le noir","Un savoir-faire dans une compétence  d’Instinc",0,[])
                this.ajout_attribut(new attribut("Stabilit"," Grâce à sa corpulence, un nain possède  +5% au test de Puissance et de Vigueur pour un jet d’oppositio",5,["Puissance","Vigueur"]))
                this.ajout_attribut(new attribut("Nemesis","Le nain choisit un peuple qui sera considéré  comme son ennemi juré. Il gagne un bonus de +5% à ses tests contre les protagonistes de cette nation.",5,this.characteristics))
                this.ajout_attribut(new attribut("Robustess"," Encaisse, sans prendre de dégâts, la  première attaque physique reçue par comba",0,[]))
                break;
            
        }
    }
    static ajout_attribut(name,description,point,characteristics_affectes){
        this.attribut.push(new attribut(name,description,point,characteristics_affectes))
    }
}








export const count = writable(0);