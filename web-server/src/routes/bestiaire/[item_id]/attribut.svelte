<script>
    export let nomAttribut
    export let contenuAttribut 
</script>

<div class="grow shrink w-full bg-primary-light rounded-full 
border-accent-blue border-[0.5vh] aspect-[5/1] flex justify-between relative">
    <div class="bg-accent-blue rounded-l-full h-full
    text-center px-[10%] -translate-x-[1px] scale-y-[101%]">
        <p class="relative top-1/2 -translate-y-1/2 text-[100%] text-white font-bold">
            {nomAttribut + " : "}
        </p>
    </div>
    <p class="text-[100%] absolute right-[10%] top-1/2 -translate-y-[50%] ">
        {contenuAttribut}
    </p>    
</div>