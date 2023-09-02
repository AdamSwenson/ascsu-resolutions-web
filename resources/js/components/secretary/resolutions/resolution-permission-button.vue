<template>
<div class="resolution-permission-button ">
<button class="btn btn-info" v-on:click="getPermission">Permission</button>
    </div>
</template>

<script>

import * as routes from "../../../routes";
// import plenaryMixin from "../../../mixins/plenaryMixin";

export default {
    name: "resolution-permission-button",

    props: ['resolutionId'],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {
        getPermission : function(){
            let url = routes.secretary.permissions.getPermission(this.resolutionId)

            window.console.log('permissions', 'get', 124, url);
            let me = this;
            Vue.axios.get(url).then((response) => {
                window.console.log('permissions', 'response', 126, response);
            });

        }
    }

}
</script>

<style scoped>

</style>
