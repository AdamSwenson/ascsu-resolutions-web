<template>
    <div class="toggle-all-resolution-permissions ">
        <div class="row">
            <div class="col-6">
                <working-spinner v-if="isUnlockWorking"></working-spinner>
                <button v-else
                        class="btn btn-primary" v-on:click="handleUnlockAll">Allow editing</button>
            </div>

            <div class="col-6">
                <working-spinner v-if="isLockWorking"></working-spinner>
                <button
                    v-else
                    class="btn btn-primary" v-on:click="handleLockAll">Lock editing</button>
            </div>
        </div>

    </div>
</template>

<script>

import * as routes from "../../../routes";
import plenaryMixin from "../../../mixins/plenaryMixin";
import WorkingSpinner from "../../common/working-spinner";

export default {
    name: "toggle-all-resolution-permissions",
    components: {WorkingSpinner},
    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {
            isLockWorking : false,
            isUnlockWorking : false
        }
    },

    asyncComputed: {},

    computed: {},

    methods: {

        handleLockAll: function () {
            let url = routes.secretary.permissions.lockAll(this.plenaryId)

            window.console.log('permissions', 'lock all', 124, url);
            let me = this;
            this.isLockWorking = true;
            Vue.axios.post(url).then((response) => {
                window.console.log('permissions', 'response', 126, response);
                me.isLockWorking = false;
            });
        },

        handleUnlockAll: function () {
            let url = routes.secretary.permissions.unlockAll(this.plenaryId)
            window.console.log('permissions', 'lock all', 124, url);
            let me = this;
            this.isUnlockWorking = true;
            Vue.axios.post(url).then((response) => {
                window.console.log('permissions', 'response', 126, response);
                this.isUnlockWorking = false;
            });
        }


    }

}
</script>

<style scoped>

</style>
