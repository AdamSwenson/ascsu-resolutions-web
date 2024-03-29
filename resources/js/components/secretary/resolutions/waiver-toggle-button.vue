<template>
    <a v-if="isVisible"
       class="waiver-toggle-button  btn btn-sm"
       href="#"
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
    name: "waiver-toggle-button",

    props: ['resolutionId'],

    mixins: [ResolutionMixin],

    data: function () {
        return {
            unwaiverLabel: 'Set waiver',
            waiverLabel: 'Remove waiver',
            waiverStyle: 'btn-warning',
            unwaiverStyle: 'btn-outline-warning'
        }
    },

    asyncComputed: {
        /**
         * Should not show the button on action items
         * @returns {boolean|(function(): boolean)|*}
         */
        isVisible: function(){
           // return true;
            if (!isReadyToRock(this.resolution)) return false;
            return this.isFirstReading || this.isWaiver;
        },

        label: function () {
            if (!isReadyToRock(this.resolution)) return this.unwaiverLabel;
            if (this.isWaiver) return this.waiverLabel;
            return this.unwaiverLabel;
        },

        styling: function () {
            if (!isReadyToRock(this.resolution)) return this.unwaiverStyle;
            if (this.isWaiver) return this.waiverStyle;
            return this.unwaiverStyle;
        }
    },


    computed: {},

    methods: {

        handleClick: function () {
            this.$store.dispatch('toggleIsWaiver', this.resolution);
        },

    },



}
</script>

<style scoped>

</style>
