<script>
    export let min = 0
    export let max = 100

    const LARGEUR_RELATIVE = 0.3;
    let largeurPixel = window.innerWidth * LARGEUR_RELATIVE;
    function quandRedimensionnement() {
        let largeurPixel = window.innerWidth * LARGEUR_RELATIVE
    }
    
    $:poigneeLargeurPourcent = (window.innerWidth / 100 * 4) /largeurPixel

    let test= 0

    export let borneInfVal = min
    export let borneSupVal = max

    let borneInfBouge = false
    let borneSupBouge = false
    function commenceMouvementBorneInf () {
        borneInfBouge = true
    }

    function commenceMouvementBorneSup () {
        borneSupBouge = true
    }

    function arreterToutMouvement () {
        borneInfBouge = false
        borneSupBouge = false
    }

    function quandSourisBouge (e) {
        if (borneInfBouge) {
            borneInfVal += e.movementX * max / largeurPixel
            enfermerBorneInf()
        }
        if (borneSupBouge) {
            borneSupVal += e.movementX * max / largeurPixel
            enfermerBorneSup()
        }
    }

    function enfermerBorneInf (){
        if (borneInfVal >= borneSupVal) {
            borneInfVal = borneSupVal 
        }
        else if (borneInfVal <= min) {
            borneInfVal = min
        }
    }

    function enfermerBorneSup() {
        if (borneSupVal <= borneInfVal) {
            borneSupVal = borneInfVal
        }
        else if (borneSupVal >= max) {
            borneSupVal = max
        }
    }

</script>

<svelte:window 
    on:mousemove={quandSourisBouge}
    on:mouseup={arreterToutMouvement}
    on:resize={quandRedimensionnement}
></svelte:window>


<div class="flex flex-row justify-center w-[360px] items-center">
    <input type="number" bind:value={borneInfVal} on:change={enfermerBorneInf} 
    class="w-[25%] px-[3%] py-[1%] rounded-[1vh] border-primary-dark border-[1px]">

    <div class="h-[1.5vh] bg-boring-gray relative rounded-full m-[3vh]" style:width={largeurPixel + "px"}>
        <div on:mousedown={commenceMouvementBorneInf} 
        class="w-[4vh] h-[4vh] rounded-[100%] bg-accent-blue top-1/2 -translate-y-1/2 absolute cursor-move -translate-x-1/2"
        style:left={(borneInfVal - min) / max * 100 + "%"}>
        </div>
        <div on:mousedown={commenceMouvementBorneSup}
        class="w-[4vh] h-[4vh] rounded-[100%] bg-accent-blue top-1/2 -translate-y-1/2 absolute cursor-move -translate-x-1/2"
        style:left={(borneSupVal - min) / max * 96 + "%"}>
        </div>
        <div class="bg-accent-blue h-[1.5vh] absolute z-10" 
        style:width={(borneSupVal - borneInfVal) / (max-min) * 100 + "%"}
        style:left={borneInfVal / (max-min) * 100 + "%"}>
        </div>
    </div>
    
    <input type="number" bind:value={borneSupVal} 
    class="w-[25%] px-[3%] py-[1%] rounded-[1vh] border-primary-dark border-[1px]">
</div>

