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
 * This handles the approval status of the resolution
 * It initially takes the value passed in as a prop but updates
 * the value internally when clicked
 */
export default {
    name: "approved-toggle-button",

    props: ['resolutionId'],

    mixins: [ResolutionMixin],

    data: function () {
        return {
            approvalStatus: false,
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

            // if (this.resolution.status === 'approved') return this.approvedLabel;

            // if (!isReadyToRock(this.resolutionId)) return this.unapprovedLabel;

            // if (this.approvalStatus) return this.approvedLabel;

            return this.unapprovedLabel;
        },

        styling: function () {
            if (!isReadyToRock(this.resolution)) return this.unapprovedLabel;
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
            //
            // let url = routes.secretary.resolutions.approvalStatus(this.resolutionId)
            //
            // window.console.log('toggle approval', 'get', 124, url);
            // let me = this;
            // Vue.axios.post(url).then((response) => {
            //     me.approvalStatus = response.data.is_approved;
            //     window.console.log('permissions', 'response', 126, response, me);
            // });

        },
        //
        // setDefaultApproval: function () {
        //     if (_.isNull(this.isApproved)) {
        //         this.approvalStatus = false;
        //     } else {
        //         this.approvalStatus = this.isApproved;
        //     }
        // }
    },

    mounted() {
        // this.setDefaultApproval();
    }


}
</script>

<style scoped>

</style>
