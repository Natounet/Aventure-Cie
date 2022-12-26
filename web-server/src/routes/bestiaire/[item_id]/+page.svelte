<script>
    import { page } from '$app/stores';
    import {attributesNames} from "/src/typesAnnuaire.js"

    export let data;

    $: item = data.toutLesItems.find(item => item.id == $page.params.item_id);
    
    function parseAttributName(name) {
        if (attributesNames[name]) return attributesNames[name]
        else return name[0].toUpperCase() + name.toLowerCase().slice(1)
    }
    function parseAttributValue(value) {
        console.log(value)
        if (typeof(value) == "string" || typeof(value) == "number" ) {
            return value
        }
        else if (value instanceof Array) {
            return value.reduce((tot, val) => tot + ", " + val)
        }
        else return value
    }
</script>

<main>
    {#each Object.keys(item) as itemAttribute}
        <p>{parseAttributName(itemAttribute) + " : " + parseAttributValue(item[itemAttribute])}</p>
    {/each}
</main>