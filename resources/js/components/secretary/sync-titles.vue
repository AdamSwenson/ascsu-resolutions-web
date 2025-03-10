<template>
<div class="sync-titles card ">
        <h3 class="card-title text-light">Sync titles</h3>

    <div class="card-body">
        <working-spinner v-if="isWorking"></working-spinner>

        <button v-else class="btn btn-primary" v-on:click="handleSyncTitles">Sync titles</button>

        <p class="card-text text-light">This pulls the current titles from documents in drive and update the database with them</p>
    </div>

</div>
</template>

<script>
import plenaryMixin from "../../mixins/plenaryMixin";
import * as routes from "../../routes";
import WorkingSpinner from "../common/working-spinner";

export default {
    name: "sync-titles",
    components: {WorkingSpinner},
    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {
            url : null,
            isWorking: false
        }
    },
    asyncComputed: {
        showUrl : function(){
            return ! _.isNull(this.url);
        }
    },

    computed: {},

    methods: {
        handleSyncTitles : function(){
            window.console.log('secretary', 'sync titles');
            let url = routes.secretary.resolutions.syncTitles(this.plenary);
            let me = this;
            this.isWorking = true;
            Vue.axios.post(url,).then((response) => {
                window.console.log('secretary', 'response', 126, response);
                me.isWorking = false;
                //todo Actually update the object
                me.$store.dispatch('forceReload');
                // me.url = response.data.agendaUrl;
            });

        },
    }

}
</script>

<style scoped>

</style>
