import { writable } from 'svelte/store';

var denomination
var niveau
var age 
var peuple =""
var peuple_caracteristique=[[false,false,false,false,false,false,false],[false,false,false,false,false,false,false]]
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

const nom_caracterisique=["Puissance","Finesse","Vigueur","Savoir","L'instinct","Social","Stress"]
const indice_cara={"puissance":0,"Finesse":1,"Vigueur":2,"Savoir":3,"L'instinct":4,"Social":5,"Stress":6}
const bonus=0
const malus=1






function peuple_malus_bonus(){
    switch(peuple){
        case "nain":
            pv=21
            psy=8
            a_repartir[bonus]=[{"nb_point":7,}]


            a_repartir[bonus].forEach(element => {
                peuple_caracteristique[bonus][indice_cara[element]]=true
            });
            a_repartir[malus].forEach(element => {
                peuple_caracteristique[malus][indice_cara[element]]=true
            });
        break;


    }

    
    
}



export const count = writable(0);