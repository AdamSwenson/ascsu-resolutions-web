<template>
<div class="create-agenda card ">
        <h3 class="card-title text-light">Create agenda </h3>

    <div class="card-body">
        <button class="btn btn-primary" v-on:click="handleCreateAgenda">Create agenda</button>
    </div>


</div>
</template>

<script>
import plenaryMixin from "../../mixins/plenaryMixin";
import * as routes from "../../routes";

export default {
    name: "create-agenda",

    props: ['plenaryId'],


    data: function () {
        return {
            url : null

        }
    },
    asyncComputed: {
        showUrl : function(){
            return ! _.isNull(this.url);
        }
    },

    computed: {},

    methods: {
        handleCreateAgenda : function(){
            window.console.log('secretary', 'createAgenda');
            let url = routes.secretary.agenda.createAgenda(this.plenaryId);
            let me = this;
            Vue.axios.post(url,).then((response) => {
                window.console.log('secretary', 'response', 126, response);
                // me.url = response.data.agendaUrl;
            });

        },
    }

}
</script>

<style scoped>

</style>
