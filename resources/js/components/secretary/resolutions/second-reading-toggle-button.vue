<template>
    <button
        class="btn btn-sm second-reading-toggle-button"
        v-bind:class="styling"
        v-on:click="handleClick"
    >{{ label }}</button>

</template>

<script>
import * as routes from "../../../routes";
import plenaryMixin from "../../../mixins/plenaryMixin";
import {isReadyToRock} from "../../../utilities/readiness.utilities";
import ResolutionMixin from "../../../mixins/resolutionMixin";

export default {
    name: "second-reading-toggle-button",

    props: ['resolutionId'],

    mixins: [plenaryMixin, ResolutionMixin],

    data: function () {
        return {

            unactionLabel: 'Set action',
            actionLabel: 'Set first reading',
            actionStyle: ' btn-warning ',
            unactionStyle: ' btn-outline-warning '

        }
    },

    asyncComputed: {
        label: function () {
            if (!isReadyToRock(this.resolution)) return this.unactionLabel;
            if (this.isActionItem) return this.actionLabel;
            return this.unactionLabel;
        },

        styling: function () {
            if (!isReadyToRock(this.resolution)) return this.unactionStyle;
            if (this.isActionItem) return this.actionStyle;
            return this.unactionStyle;
        }
    },

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
