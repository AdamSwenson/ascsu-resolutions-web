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

/**
 * This handles the approval status of the resolution
 * It initially takes the value passed in as a prop but updates
 * the value internally when clicked
 */
export default {
    name: "approved-toggle-button",

    props: ['resolutionId', 'isApproved'],

    mixins: [],

    data: function () {
        return {
            approvalStatus: false,
            unapprovedLabel: 'Mark approved',
            approvedLabel: 'Mark unapproved',
            approvedStyle: 'btn-primary',
            unapprovedStyle: 'btn-outline-primary'
        }
    },

    asyncComputed: {
        label: function () {
            if (!isReadyToRock(this.resolutionId)) return this.unapprovedLabel;

            if (this.approvalStatus) return this.approvedLabel;

            return this.unapprovedLabel;
        },

        styling: function () {
            if (!isReadyToRock(this.resolutionId)) return this.unapprovedStyle;
            if (this.approvalStatus) return this.approvedStyle;
            return this.unapprovedStyle;
        }
    },

    watch: {
        'isApproved': function () {
            this.setDefaultApproval();
        }
    },

    computed: {},

    methods: {

        handleClick: function () {
            let url = routes.secretary.resolutions.approvalStatus(this.resolutionId)

            window.console.log('toggle approval', 'get', 124, url);
            let me = this;
            Vue.axios.post(url).then((response) => {
                me.approvalStatus = response.data.is_approved;
                window.console.log('permissions', 'response', 126, response, me);
            });

        },

        setDefaultApproval: function () {
            if (_.isNull(this.isApproved)) {
                this.approvalStatus = false;
            } else {
                this.approvalStatus = this.isApproved;
            }
        }
    },

    mounted() {
        this.setDefaultApproval();
    }


}
</script>

<style scoped>

</style>
