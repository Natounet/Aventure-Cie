import { init } from 'svelte/internal';
import { writable } from 'svelte/store';

var denomination
var niveau
var age 
var peuple =""
var peuple_caracteristique=[]
var caracteristique=[0,0,0,0,0,0,0]
var langues
var heritage
var taille
var poid
var pv  //7 pts a repartir entre pv et psy  
var psy
var magie
var arme
var position
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




function peuple_malus_bonus(){
    switch(peuple){
        case "nain":
            pv=21
            psy=8
            a_repartir=[new modification_people(-10,["Puissance","Finesse","Savoir","Social"]),new modification_people(20,["Savoir","Social"])]


            
                    
        break;


    }

    
    
}



export const count = writable(0);