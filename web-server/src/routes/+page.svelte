<script>
    import Card from "./card.svelte";
    import { navigate } from '@svelte-kit/router';
</script>

<main>
    <section class="bg-primary-dark w-full h-[103vh] relative top-0 left-0 rounded-br-[3vh] rounded-bl-[3vh]">
        <img
        class="absolute top-[50vh] left-1/2 -translate-x-1/2 -translate-y-1/2" 
        src="/title-aventure-compagnie.svg" 
        alt="Aventure et Compagnie">
    </section>
    
    <section class="w-full relative bg-primary-light sm:h-[100vh] h-[200vh] flex sm:flex-row flex-col justify-around items-center z-10">
        <Card title="Bestiaire" on:click={navigate("/bestiaire")}>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Error tenetur voluptatibus laudantium repellat exercitationem! Fuga porro esse rerum praesentium ut?
        </Card>
        <Card title="Créateur de personnage">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Error tenetur voluptatibus laudantium repellat exercitationem! Fuga porro esse rerum praesentium ut?
        </Card>
        <Card title="Annuaire">
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Error tenetur voluptatibus laudantium repellat exercitationem! Fuga porro esse rerum praesentium ut?
        </Card>
       
    </section>
</main>


<style>
    .clip-path {
        clip-path: path("M 0 100 \ L 0 0 \ L 100 0 \ L 100 100 \ C 100 0 0 0 0 100 ");
    }
</style>
