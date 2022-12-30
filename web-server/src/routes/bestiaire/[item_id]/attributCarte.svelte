<script>
    export let titre;
    export let contenu; 
</script>

<div class="h-[70%] w-full flex flex-col">
    <div class="bg-accent-blue rounded-t-[3vh] px-[5%] py-[3%]
    text-white font-bold text-[100%]">
        {titre}
    </div>
    <p class="px-[5%] pb-[3vh] bg-primary-light rounded-b-[3vh] h-full text-[100%]">
        {contenu}
    </p>
</div>