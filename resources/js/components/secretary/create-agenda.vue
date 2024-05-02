<template>
<div class="create-agenda card ">
        <h3 class="card-title text-light">Create resolution list </h3>

    <div class="card-body">
        <working-spinner v-if="isWorking"></working-spinner>

        <button v-else class="btn btn-primary" v-on:click="handleCreateAgenda">Create resolution list</button>
    </div>

    <div class="card-body " v-show="showUrl">
        <p class="card-text text-light">
            Link to list of resolutions:<br>
            <a v-bind:href="resolutionListUrl" target="_blank">{{ resolutionListUrl }}</a>
        </p>
    </div>


</div>
</template>

<script>
import plenaryMixin from "../../mixins/plenaryMixin";
import * as routes from "../../routes";
import WorkingSpinner from "../common/working-spinner";
import PlenaryMixin from "../../mixins/plenaryMixin";

export default {
    name: "create-agenda",
    components: {WorkingSpinner},

    props: [],

    mixins: [PlenaryMixin],


    data: function () {
        return {
            // url : null,
            isWorking: false
        }
    },
    asyncComputed: {
        showUrl : function(){
            return ! _.isNull(this.resolutionListUrl);
        }
    },

    computed: {},

    methods: {
        handleCreateAgenda : function(){
            window.console.log('secretary', 'createAgenda');
            let url = routes.secretary.agenda.createAgenda(this.plenaryId);
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
