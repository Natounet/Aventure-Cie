<script>
    import { fade } from "svelte/transition";
    import { cubicOut } from 'svelte/easing';
    import { inview } from 'svelte-inview';
    import { goto } from "$app/navigation";
    export let title;
    export let link;

    let isInView;

    function test (node, params) {
        const existingTransform = getComputedStyle(node).transform.replace('none', '');

		return {
			delay: params.delay || 100,
			duration: params.duration || 400,
			easing: params.easing || cubicOut,
			css: (t, u) => `transform: translateY(${u * 100}px); opacity: ${t}` 
		};
    }

</script>

<div
use:inview={{ unobserveOnEnter: true, rootMargin: '0%' }}
on:change={({ detail }) => {
    isInView = detail.inView;
}}>
    {#if isInView}
        <div
        transition:test
        on:click={() => goto(link)}
        on:keydown={() => goto(link)}
        class="w-[50vw] sm:w-[30vw] md:w-[25vw] bg-white rounded-[6vh] text-center
        font-fredoka justify-between drop-shadow-card flex flex-col
        hover:scale-110 hover:-rotate-6 transition-all
        cursor-pointer 
        ">
            <div class="text-center w-full min-h-[8vh] rounded-tl-[6vh] rounded-tr-[6vh] border-b-[1px] 
            border-boring-gray border-dashed relative transition-colors">
                <h1 class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 font-extrabold">{title}</h1>
            </div>
            <div class="text-boring-gray p-[10%]">
                <slot></slot>
            </div>
            <button class="w-full h-[8vh] bg-accent-blue  rounded-bl-[6vh] 
            rounded-br-[6vh] text-primary-light text-lg font-bold">Go !</button>
        </div>
    {/if}
</div>

