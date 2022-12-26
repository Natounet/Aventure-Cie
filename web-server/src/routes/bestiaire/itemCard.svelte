<script>
    import { fly } from "svelte/transition";
    import {goto} from "$app/navigation";

    export let imgSrc;
    export let nom;
    export let mainAttributes;
    export let id;
</script>

<div 
class="sm:w-[300px] h-[20vh] bg-primary-dark rounded-[3vh] p-[3vh] 
flex items-center text-white font-fredoka
cursor-pointer hover:scale-105 transition-transform"
transition:fly={{x: 100, y: 0}}
on:click={() => goto("/bestiaire/" + id)}
on:keydown={() => goto("/bestiaire/" + id)}>
    <img src={imgSrc} alt="" class="w-[14vh] h-[14vh] object-cover rounded-[2vh]">
    <div class="h-[14vh] pl-[5%] flex flex-col">
        <h1 class="text-lg ">{nom}</h1>
        <div class="text-xs flex flex-col justify-end text-boring-gray">
            {#each mainAttributes as attribute}
                <p>{attribute}</p>
            {/each} 
        </div>
    </div>
</div>