<template>
    <div class="resolution-item ">
        <li class="list-group-item">

            <resolution-permission-button :resolution-id="resolutionId">
            </resolution-permission-button>
            <approved-toggle-button :resolution-id="resolutionId"
                                    :is-approved="isApproved"
            ></approved-toggle-button>  {{ number }} {{ title }}

<!--            <a href="#" class="btn btn-sm "-->
<!--               v-bind:class="styling"-->
<!--               v-on:click="toggleEditing"-->
<!--            >{{ buttonLabel }}</a> {{ number }} {{ title }}-->
        </li>
    </div>
</template>

<script>
import * as routes from "../../../routes";
import ResolutionPermissionButton from "./resolution-permission-button";
import ApprovedToggleButton from "./approved-toggle-button";

export default {
    name: "resolution-item",
    components: {ApprovedToggleButton, ResolutionPermissionButton},
    props: ['resolutionId', 'title', 'number', 'isApproved', 'firstReadingPlenary', 'actionPlenaries'],

    mixins: [],

    data: function () {
        return {
            // isEditable: false
        }
    },

    asyncComputed: {
        // buttonLabel: function () {
        //     if (this.isEditable) {
        //         return 'Lock editing'
        //     }
        //     return 'Allow editing';
        //
        // },
        //
        // styling: function () {
        //     if (this.isEditable) {
        //         return 'btn-primary'
        //     }
        //     return 'btn-outline-primary';
        // }
    },

    computed: {},

    methods: {
        //
        // getPermission: function () {
        //     let url = routes.secretary.permissions.getPermission(this.resolutionId)
        //
        //     window.console.log('permissions', 'get', 124, url);
        //     let me = this;
        //     Vue.axios.get(url).then((response) => {
        //         /*Will receive the following:
        //         {
        //             "id": "anyoneWithLink",
        //             "type": "anyone",
        //             "kind": "drive#permission",
        //             "role": "reader",
        //             "allowFileDiscovery": false
        //         }*/
        //         if (response.data.role === 'reader') {
        //             me.isEditable = false;
        //         } else if (response.data.role === 'writer') {
        //             me.isEditable = true;
        //         }
        //         window.console.log('permissions', 'response', 126, response);
        //     });
        // },
        //
        // lockEditing: function () {
        //     let url = routes.secretary.permissions.lockOne(this.resolutionId)
        //
        //     window.console.log('permissions', 'get', 124, url);
        //     let me = this;
        //     Vue.axios.post(url).then((response) => {
        //         //todo check for success
        //         me.isEditable = false;
        //
        //         window.console.log('permissions', 'response', 126, response);
        //     });
        // },
        //
        // unlockEditing: function () {
        //     let url = routes.secretary.permissions.unlockOne(this.resolutionId)
        //
        //     window.console.log('permissions', 'get', 124, url);
        //     let me = this;
        //     Vue.axios.post(url).then((response) => {
        //         //todo check for success
        //         me.isEditable = true;
        //
        //         window.console.log('permissions', 'response', 126, response);
        //     });
        // },
        //
        // toggleEditing: function () {
        //     if (this.isEditable) {
        //         this.lockEditing();
        //     } else {
        //         this.unlockEditing();
        //     }
        // }
    },
    mounted() {
        // this.getPermission();
    }

}
</script>

<style scoped>

</style>
