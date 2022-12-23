<script>
    import { ACCENT_BLUE } from "/src/colors";
    import { fade } from "svelte/transition";
    import { cubicOut } from "svelte/easing";
    import { createEventDispatcher } from "svelte"

    const onCheckDispacher = createEventDispatcher();

    const DURATION = 200;

    export let delay = 1000;

    export let checked = false;
    function toggleCheck() {
        onCheckDispacher("check-toggled", checked)
        checked = !checked
    }

    function enterFromBottom (node) {
		return {
			delay,
			duration: delay + DURATION,
			easing:  cubicOut,
			css: (t, u) => `transform: translateY(${u * 100}px); opacity: ${t}` 
		};
    }
</script>

<div class="min-w-[110px] w-[45vw] sm:w-[30vw] md:w-[13vw] h-[35px] min-h-[30px] rounded-[1.5vh] 
drop-shadow-checkbox relative transition-colors hover:drop-shadow-checkbox-blue 
hover:outline hover:outline-[0.5vh] outline-accent-blue bg-white cursor-pointer"
on:click={toggleCheck}
on:keydown={toggleCheck}
transition:enterFromBottom
style:background-color={checked ? "#6BCDE2" : "white"}>
    <div class="w-[30%] h-full absolute left-0 top-0">
        <div class="w-[2.5vh] absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">
            {#if checked}
                <img src="/checked_dark.svg" alt="">
            {:else} 
                <img src="/uncheck_dark.svg" alt="">
            {/if}
        </div>
    </div>
    <p class="text-primary-dark text-sm sm:text-md font-fredoka font-bold align-middle
    inline w-3/4 absolute right-0 top-1/2 -translate-y-[55%] drop-shadow-checkbox-text">
        <slot></slot>
    </p>
</div>