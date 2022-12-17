import { init } from 'svelte/internal';
import { writable } from 'svelte/store';
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
    constructor(name,description) {
        this.name_atribut=name;
        this.name_atribut=description;
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
        
    }
    static ajout_attribut(name,description,point,characteristics_affectes){
        this.attribut.push(new attribut(name,description,point,characteristics_affectes))
    }
}








export const count = writable(0);