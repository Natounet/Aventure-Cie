<script>
    import { page } from '$app/stores';
    import { Arme, Armure, Don, FichePersonnage, ObjetDivers, ObjetMagique } from '/src/typesAnnuaire.js';
    import Attribut from './attribut.svelte';
    import AttributCarte from './attributCarte.svelte';

    export let data;

    $: item = data.toutLesItems.find(item => item.id == $page.params.item_id)
    
    function joindreAvecVirgules(tab) {
        return tab.reduce((tot, val) => tot + ", " + val)
    }
</script>
 
<main class="bg-primary-light w-[100vw] h-[100vh] font-fredoka 
text-[10pt] print:text-[20pt]">
    <div class="w-1/3 h-full bg-primary-dark absolute left-0 top-0 
    flex flex-col items-center print:hidden">
        <img src="/épée.png" alt="" 
        class="w-[80%] rounded-[4vh] mt-[5vh]">
        <p class="text-lg text-primary-light underline
        mt-[5vh]">
            {item.nom + " - " + item.nomType}
        </p>

        <button class="text-white text-lg bg-accent-blue 
        rounded-[2vw] px-[2vw] py-[5px] font-fredoka cursor-pointer
        mt-[30vh]"
        on:click={() => window.print()}>
            Imprimer
        </button>
    </div>
    <div class="w-2/3 print:w-full h-full absolute right-0 top-0 print:block
     flex items-center justify-center">
        <div 
        class=" flex flex-col justify-between h-full
        bg-white p-[5%] aspect-A4 print:aspect-auto h-[90%] 
        print:w-full print:h-full drop-shadow-page">
            {#if item instanceof Arme}
                <div class="flex  h-1/3 justify-between">
                    <img src="/épée.png" alt="" 
                    class="w-[48%] border-[3px] border-accent-blue rounded-[4vh]">
                    <div class="flex flex-col justify-between w-[48%] h-full">
                        <h1 class=" h-[25%] flex items-center box-border">
                            <p 
                            class="bg-accent-blue text-white text-[100%]
                            w-[45%] h-full px-[5%] rounded-[3vh] 
                            box-border flex items-center
                            font-bold">
                                Nom : 
                            </p>
                            <p class="text-primary-dark text-[100%] ml-[0.2cm]">
                                {item.nom}  
                            </p>
                        </h1>
                        <AttributCarte titre="Description" contenu={item.description}></AttributCarte>
                    </div>
                    
                </div>
               <div class="grid grid-cols-2 grid-rows gap-[2vh]">
                    <Attribut nomAttribut="Prix" contenuAttribut={item.prix}></Attribut>
                    <Attribut nomAttribut="Critique" contenuAttribut={item.critique}></Attribut>
                    <Attribut nomAttribut="Portée" contenuAttribut={item.portee}></Attribut>
                    <Attribut nomAttribut="Dégats" contenuAttribut={item.degats}></Attribut>
                    <Attribut nomAttribut="Poids" contenuAttribut={item.poids}></Attribut>
                    <Attribut nomAttribut="Armure" contenuAttribut={item.armure}></Attribut>
                    <AttributCarte 
                    titre="Caractéristique" 
                    contenu={item.caracteristique}></AttributCarte>
                    <AttributCarte 
                    titre="Catégorie(s)" 
                    contenu={joindreAvecVirgules(item.categories)}></AttributCarte>
                </div>
            {:else if item instanceof Armure}
                <div>

                </div>
            {:else if item instanceof Don}
                <div>
                    
                </div>
            {:else if item instanceof FichePersonnage}
                <div>

                </div>
            {:else if item instanceof ObjetMagique}
                <div>

                </div>
            {:else if item instanceof ObjetDivers}
                <div>

                </div>
            {/if}
        </div>
    </div>
</main> 


<style>
    :global(body) {
        -webkit-print-color-adjust:exact !important;
        print-color-adjust:exact !important;
    }
</style>