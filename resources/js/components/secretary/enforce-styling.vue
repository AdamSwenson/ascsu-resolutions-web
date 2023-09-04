<template>
<div class="enforce-styling card">
    <h3 class="card-title text-light">Enforce styling</h3>

    <div class="card-body">
        <button class="btn btn-primary"
                v-on:click="handleEnforceStyle">Enforce styling</button>

    </div>


</div>
</template>

<script>
import * as routes from "../../routes";

export default {
    name: "enforce-styling",

    props: [],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {
        handleEnforceStyle : function(){
            window.console.log('secretary', 'createAgenda');
            let url = routes.secretary.resolutions.enforceStyle();
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
