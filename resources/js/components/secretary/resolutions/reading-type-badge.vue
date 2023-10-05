<template>
    <span class="reading-type-badge badge rounded-pill text-dark "
          v-if="show"
          v-bind:class="styling"
    >{{ displayText }}</span>

</template>

<script>

import {isReadyToRock} from "../../../utilities/readiness.utilities";
import ResolutionMixin from "../../../mixins/resolutionMixin";

export default {
    name: "reading-type-badge",

    props: ['resolutionId'],

    mixins: [ResolutionMixin],

    data: function () {
        return {
                first: {
                    text: 'First reading',
                    style: 'bg-info'
                },

            waiver:{
                text: 'First reading -- Waiver',
                style: 'bg-warning'

            },
                action: {
                    text: 'Action item',
                    style: 'bg-warning'
                },


        }
    },

    asyncComputed: {
        show: function () {
            return isReadyToRock(this.isActionItem) || isReadyToRock(this.isWaiver) || isReadyToRock(this.isFirstReading);
        },

        styling : function(){
            //waiver checks if first reading too
            if(this.isWaiver){
                return this.waiver.style;
            }else if(this.isFirstReading){
                return this.first.style;
            }else if (this.isActionItem){
                return this.action.style;
            }
        },

        displayText: function () {
            //waiver checks if first reading too
            if(this.isWaiver){
                return this.waiver.text;
            }else if(this.isFirstReading){
                return this.first.text;
            }else if (this.isActionItem){
                return this.action.text;
            }
            //
            //
            // if(this.isApproved){
            //     return this.statuses.approved.text;
            // }else if(this.isFailed){
            //     return this.statuses.failed.text;
            // }


            // return this.statuses[this.status]['text'];
            // switch (this.status) {
            //     case 'approved':
            //         return 'Approved';
            //         break;
            //     case 'failed':
            //         return 'Failed';
            //         break;
            //     case 'first':
            //         return 'First reading';
            //         break
            //     case 'action':
            //         return 'Action';
            //         break;
            // }
        }
    },

    computed: {}
    ,

    methods: {}

}
</script>

<style scoped>

</style>
