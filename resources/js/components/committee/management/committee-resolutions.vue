<template>
<div class="committee-resolutions card">

    <div class="card-title">{{committeeName}}</div>

    <div class="card-body">
        <h4>Plenary</h4>

        <p class="card-text">
            {{plenaryName}}
        </p>

        <p class="card-text">
            Change plenary selector goes here
        </p>

    </div>


    <committee-resolutions-card :committee="committee"></committee-resolutions-card>



</div>
</template>

<script>

import plenaryMixin from "../../../mixins/plenaryMixin";
import committeeMixin from "../../../mixins/committeeMixin";
import {isReadyToRock} from "../../../utilities/readiness.utilities";
import CommitteeResolutionsCard from "./committee-resolutions-card";

/**
 * This is the individual committee page for managing resolutions
 *
 * Created AR-91
 */
export default {
    name: "committee-resolutions",
    components: {CommitteeResolutionsCard},


    /**
     * Committee object
     */
    props: ['committee'],

    mixins: [plenaryMixin, committeeMixin],

    data: function () {
        return {}
    },

    asyncComputed: {

        /**
         * Committee that is currently doing the work
         */
        committeeName : function(){
            if(isReadyToRock(this.committee)) return "";
            return this.committee.name;
        },

        committeeResolutions : function(){
            if(isReadyToRock(this.committee)) return [];

            return this.$store.getters.getCommitteeResolutions(this.committee);
        },

        firstReadings : function(){

        },

        actionItems : function(){

        }



    },

    computed: {},

    methods: {}

}
</script>

<style scoped>

</style>
