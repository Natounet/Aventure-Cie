import { writable } from 'svelte/store';

var denomination
var niveau
var age 
var peuple =""
var peuple_caracteristique=[[0,0,0,0,0,0],[0,0,0,0,0,0]]
var peuple_caracteristique_bonus=[0,0,0,0,0,0]
var langues
var heritage
var taille
var poid
var pv  //7 pts a repartir entre pv et psy  
var psy
var magie
var arme
var caracteristique=[0,0,0,0,0,0]
var position




function peuple_malus_bonus(){
    switch(peuple){
        case "nain":
            []
        
        
        break;


    }

    
    
}



export const count = writable(0);