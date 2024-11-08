<template>
    <div class="single-control-card card">

        <h3 class="card-title text-light">One-stop shop for plenaries</h3>

        <div class="card-body">
            <div class="row">

                <div class="col">
                    <start-plenary-button></start-plenary-button>
                    <p class="card-text text-info">This will run all tasks for the beginning of the plenary. </p>
                </div>

                <div class="col">
                    <stop-plenary-button></stop-plenary-button>
                    <p class="card-text text-info">This will run all tasks for the end of the plenary. </p>
                </div>

            </div>
        </div>
    </div>
</template>

<script>
import StartPlenaryButton from "./start-plenary-button";
import StopPlenaryButton from "./stop-plenary-button";

export default {
    name: "single-control-card",
    components: {StopPlenaryButton, StartPlenaryButton},
    props: [],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {}

}
</script>

<style scoped>

</style>
