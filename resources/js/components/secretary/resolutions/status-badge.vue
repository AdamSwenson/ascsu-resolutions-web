<template>
    <span class="status-badge badge rounded-pill text-dark"
          v-if="show"
          v-bind:class="styling"
    >{{ displayText }}</span>

</template>

<script>

import {isReadyToRock} from "../../../utilities/readiness.utilities";
import ResolutionMixin from "../../../mixins/resolutionMixin";

export default {
    name: "status-badge",

    props: ['resolutionId'],

    mixins: [ResolutionMixin],

    data: function () {
        return {
            statuses: {
                approved: {
                    text: 'Approved',
                    style: 'bg-success'
                },
                failed: {
                    text: 'Failed',
                    style: 'bg-danger'
                },
            }
        }
    },

    asyncComputed: {
        show: function () {
            return isReadyToRock(this.isApproved) || isReadyToRock(this.isFailed);
        },

        styling : function(){
            if(this.isApproved){
                return this.statuses.approved.style;
            }else if(this.isFailed){
                return this.statuses.failed.style;
            }
        },
        displayText: function () {
            if(this.isApproved){
                return this.statuses.approved.text;
            }else if(this.isFailed){
                return this.statuses.failed.text;
            }


        }
    },

    computed: {}
    ,

    methods: {}

}
</script>

<style scoped>

</style>
