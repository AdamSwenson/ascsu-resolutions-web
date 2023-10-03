<template>
    <span class="status-badge badge rounded-pill "
          v-if="show"
          v-bind:class="styling"
    >{{ displayText }}</span>

    <!--    ><span-->
    <!--        class="bg-success"-->
    <!--        v-if="isApproved"-->
    <!--    >Approved</span> <span-->
    <!--        class="badge rounded-pill bg-warning"-->
    <!--        v-if="showWaiverIndicator"-->
    <!--    >Waiver</span>-->

</template>

<script>

import {isReadyToRock} from "../../../utilities/readiness.utilities";

export default {
    name: "status-badge",

    props: ['status'],

    mixins: [],

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
                first: {
                    text: 'First reading',
                    style: 'bg-primary'
                },
                action: {
                    text: 'Action item',
                    style: 'bg-warning'
                }
            }
        }
    },

    asyncComputed: {
        show: function () {
            return isReadyToRock(this.status);
        },
        styling : function(){
            return this.statuses[this.status]['style'];
        },
        displayText: function () {
            return this.statuses[this.status]['text'];
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
