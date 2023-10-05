<template>
    <a href="#"
       class="approved-toggle-button  btn btn-sm"
       v-bind:class="styling"
       v-on:click="handleClick"
    >{{ label }}</a>
</template>

<script>

import {isReadyToRock} from "../../../utilities/readiness.utilities";
import * as routes from "../../../routes";
import ResolutionMixin from "../../../mixins/resolutionMixin";

/**
 * This handles the approval status of the resolution.
 * Todo Currently refreshes the page. Should update property
 */
export default {
    name: "approved-toggle-button",

    props: ['resolutionId'],

    mixins: [ResolutionMixin],

    data: function () {
        return {
            unapprovedLabel: 'Mark approved',
            approvedLabel: 'Remove approved',
            approvedStyle: 'btn-primary',
            unapprovedStyle: 'btn-outline-primary'
        }
    },

    asyncComputed: {
        label: function () {
            if (!isReadyToRock(this.resolution)) return this.unapprovedLabel;
            if (this.isApproved) return this.approvedLabel;
            return this.unapprovedLabel;
        },

        styling: function () {
            if (!isReadyToRock(this.resolution)) return this.unapprovedStyle;
            if (this.isApproved) return this.approvedStyle;
            return this.unapprovedStyle;
        }
    },


    computed: {},

    methods: {

        handleClick: function () {
            //Click when approved so un mark
            if(this.isApproved){
                this.$store.dispatch('markResolutionUnvoted', this.resolution)
            }

            if(! this.isApproved){
                this.$store.dispatch('markResolutionApproved', this.resolution);
            }

        },

    },



}
</script>

<style scoped>

</style>
