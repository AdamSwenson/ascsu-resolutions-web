<template>
    <div class="toggle-all-resolution-permissions ">
        <div class="row">
            <div class="col-6">
                <button class="btn btn-primary" v-on:click="handleUnlockAll">Allow editing</button>
            </div>

            <div class="col-6">
                <button class="btn btn-primary" v-on:click="handleLockAll">Lock editing</button>
            </div>
        </div>

    </div>
</template>

<script>

import * as routes from "../../../routes";
import plenaryMixin from "../../../mixins/plenaryMixin";

export default {
    name: "toggle-all-resolution-permissions",

    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {

        handleLockAll: function () {
            let url = routes.secretary.permissions.lockAll(this.plenaryId)

            window.console.log('permissions', 'lock all', 124, url);
            let me = this;
            Vue.axios.post(url).then((response) => {
                window.console.log('permissions', 'response', 126, response);
            });
        },

        handleUnlockAll: function () {
            let url = routes.secretary.permissions.unlockAll(this.plenaryId)
            window.console.log('permissions', 'lock all', 124, url);
            let me = this;
            Vue.axios.post(url).then((response) => {
                window.console.log('permissions', 'response', 126, response);
            });
        }


    }

}
</script>

<style scoped>

</style>
