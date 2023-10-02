<template>
    <button class="btn btn-sm btn-outline-warning set-second-reading-button"
    v-on:click="handleClick">Set second reading</button>
</template>

<script>
import * as routes from "../../../routes";
import plenaryMixin from "../../../mixins/plenaryMixin";

export default {
    name: "set-second-reading-button",

    props: ['resolutionId'],

    mixins: [plenaryMixin],


    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {

        handleClick: function () {
            let url = routes.secretary.resolutions.setAction(this.plenaryId, this.resolutionId)

            let me = this;
            Vue.axios.post(url).then((response) => {
                window.console.log('set action ', 'post', 32, response.data);
                location.reload();

                // me.approvalStatus = response.data.is_approved;
                window.console.log('permissions', 'response', 126, response, me);
            });

        },


    }

}
</script>

<style scoped>

</style>
