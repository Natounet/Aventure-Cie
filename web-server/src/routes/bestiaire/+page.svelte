<script>
 function focusSearchBar(e) {
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

    <section class="h-[100vh]">

    </section>
</main>