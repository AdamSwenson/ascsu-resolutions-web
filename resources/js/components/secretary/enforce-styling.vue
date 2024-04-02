<template>
<div class="enforce-styling card">
    <h3 class="card-title text-light">Enforce styling</h3>

    <div class="card-body">
        <working-spinner v-if="isWorking"></working-spinner>

        <button v-else
                class="btn btn-primary"
                v-on:click="handleEnforceStyle">Enforce styling</button>

    </div>


</div>
</template>

<script>
import * as routes from "../../routes";
import WorkingSpinner from "../common/working-spinner";
import plenaryMixin from "../../mixins/plenaryMixin";

export default {
    name: "enforce-styling",
    components: {WorkingSpinner},
    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {
            isWorking : false
        }
    },

    asyncComputed: {},

    computed: {},

    methods: {
        handleEnforceStyle : function(){
            window.console.log('secretary', 'createAgenda');
            let url = routes.secretary.resolutions.enforceStyle(this.plenary);
            let me = this;
            this.isWorking = true;
            Vue.axios.post(url,).then((response) => {
                window.console.log('secretary', 'response', 126, response);
                me.isWorking = false;
                // me.url = response.data.agendaUrl;
            });

        },


    }

}
</script>

<style scoped>

</style>
