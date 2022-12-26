<script>
    import Checkbox from "./checkbox.svelte";
    import { cubicOut } from "svelte/easing";
    import { fade } from "svelte/transition";
    import {Arme, Armure, Don, FichePersonnage, ObjetMagique, ObjetDivers} from "/src/typesAnnuaire.js"
    import {PlageNumeraire} from "./filtre.js"
    import DoubleSlider from "./DoubleSlider.svelte";
    import ItemCard from "./itemCard.svelte";
    import { slide } from 'svelte/transition';
    import { goto } from "$app/navigation";

    export let data;

    let researchMade = false

    $: filtres = {
        Arme: {
            prix: new PlageNumeraire(false, "Prix", 0, 100),
            poids: new PlageNumeraire(false, "Poids (kg)", 0, 100),
            portee: new PlageNumeraire(false, "Portée (m)", 0, 4),
            armure: new PlageNumeraire(false, "Armure", 0, 10)
        },
        Armure: {},
        Don: {},
        FichePersonnage: {},
        ObjetMagique: {}
    }   

    function passeFiltre(filtres, item) {
        for (let attribut in filtres[item.constructor.name]) { 
            //item.constructor.name c'est le nom de la classe dont item est une
            //instance
            const filtre = filtres[item.constructor.name][attribut]
            console.log(filtre.actif)
            if (filtre.actif && !filtre.tester(item[attribut])) return false;
        }
        return true;
    }

    function filtrerItems(items, filtres) {
        let result = items.filter(item => {
            return passeFiltre(filtres, item)
        })
        return result
    }

    let itemTypes = {
        Arme: {
            filterThisType: false,
            typeName: Arme.name
        },
        Armure:{
            filterThisType: false,
            typeName: Armure.name
        },
        Don: {
            filterThisType: false,
            typeName: Don.name
        },
        FichePersonnage :{
            filterThisType: false,
            typeName: FichePersonnage.name
        },
        ObjetMagique : {
            filterThisType: false,
            typeName: ObjetMagique.name
        },
        ObjetDivers : {
            filterThisType: false,
            typeName: ObjetDivers.name
        }
    }                      

    let toutLesItems = data.toutLesItems;
    $: itemFiltree = filtrerItems(toutLesItems, filtres);

    function focusSearchBar(e) {
        researchMade = true;
        if (window.innerWidth < 640) {
            e.target.scrollIntoView({behavior: "smooth", block: "start", inline: "nearest"})        
        }

        if (e.keyCode == 13) {
            e.target.scrollIntoView({behavior: "smooth", block: "start", inline: "nearest"})
        }
    }
</script>

<main>
    <section class="bg-primary-dark w-[100vw] h-[100vh] relative">
        <img src="/titre_bestiaire.svg" 
        class="absolute w-[90vw] sm:w-1/2 top-1/2 left-1/2 -translate-y-full -translate-x-1/2" 
        alt="bestiaire">

        <div class="w-[90vw] h-[8vh] border-none rounded-[8vh] 
        absolute bottom-[7vh] left-1/2 -translate-x-1/2 -translate-y-1/2">
            <input type="text" class="w-full h-full rounded-[8vh] px-[4vh] font-fredoka 
            focus:outline-accent-blue outline outline-1 outline-offset-2 outline-[1px]
            text-primary-dark scroll-mt-[10vh] sm:text-xl text-md"
            placeholder="Partez à la recherche de créatures..."
            on:click={focusSearchBar}
            on:keydown={focusSearchBar}>
            <div class="w-[7.25vh] h-[7.25vh] bg-accent-blue rounded-[7.25vh] absolute top-[0.375vh] right-[0.5vh]">
                <img src="/loupe.svg"
                class="w-1/2 absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2"
                alt="loupe">
            </div>
        </div>
    </section>

    {#if researchMade}
        <section class="py-[2vh] bg-primary-light">
            <div 
            class="w-full [&>*]:my-[2vh] grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 justify-items-center">
                {#each Object.keys(itemTypes) as itemType, index}
                    <Checkbox delay={index *100 + 500} bind:checked={itemTypes[itemType].filterThisType}>
                        {itemTypes[itemType].typeName}
                    </Checkbox>
                {/each}
            </div>
            <div>
                {#each Object.keys(filtres) as itemType, index}
                    {#if itemTypes[itemType].filterThisType}
                        <div class="bg-white w-[96vw] rounded-[3vh] p-[3vh] mx-auto my-[3vh]"
                        transition:slide="{{duration: 100, easing: cubicOut}}">
                            <h1 class="font-fredoka text-xl bg-primary-dark text-white rounded-[3vh] text-center mb-[3vh]">
                                {itemTypes[itemType].typeName}
                            </h1>

                            {#each Object.keys(filtres[itemType]) as attribute_name}
                                <div class="w-full flex items-center justify-between"
                                style:filter={
                                    filtres[itemType][attribute_name].actif ? 
                                    "saturate(1) opacity(1)" 
                                    : "saturate(0) opacity(0.5)"
                                }>
                                    
                                    <div class="flex items-center cursor-pointer"
                                    on:click={() => filtres[itemType][attribute_name].actif = !filtres[itemType][attribute_name].actif}
                                    on:keydown={() => filtres[itemType][attribute_name].actif = !filtres[itemType][attribute_name].actif}>
                                        {#if filtres[itemType][attribute_name].actif}
                                            <img src="/checked_dark.svg" 
                                            alt=""
                                            class="w-[3vh] h-[3vh] mr-[2vh]">
                                        {:else} 
                                            <img src="/uncheck_dark.svg" 
                                            alt=""
                                            class="w-[3vh] h-[3vh] mr-[2vh]">
                                        {/if}
                                        <p 
                                        class="bg-white z-10 relative mr-[3vh] font-fredoka">
                                            {filtres[itemType][attribute_name].name + " : "}
                                        </p>
                                    </div>
                                    {#if filtres[itemType][attribute_name] instanceof PlageNumeraire}
                                        <DoubleSlider 
                                            min={filtres[itemType][attribute_name].min} 
                                            max={filtres[itemType][attribute_name].max}
                                            bind:borneInfVal={filtres[itemType][attribute_name].borneInf}
                                            bind:borneSupVal={filtres[itemType][attribute_name].borneSup}
                                            on:change={() => {
                                                if (!filtres[itemType][attribute_name].actif) filtres[itemType][attribute_name].actif = true
                                                window.getSelection().empty();
                                                window.getSelection().removeAllRanges();
                                            }}
                                        ></DoubleSlider>
                                    {/if}

                                    
                                </div>  
                            {/each}
                        </div>
                    {/if}
                {/each} 
            </div>
        </section>
        <section class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 justify-items-center py-[2vh]">
            {#each itemFiltree as item}
                <div class="mb-[2vh]">
                    <ItemCard 
                    id={item.id}
                    imgSrc="/épée.png" 
                    nom={item.nom} 
                    mainAttributes={Object.keys(filtres[item.constructor.name]).slice(0, 3).map(filt => filtres[item.constructor.name][filt].name + " : " + item[filt])} 
                    >
                    </ItemCard>
                </div>
                
            {/each}
        </section>
    
    {/if}

    
</main>