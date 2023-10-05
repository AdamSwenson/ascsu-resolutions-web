<template>
    <div class="public-folder-creation card">
        <h3 class="card-title text-light">Public version</h3>


        <div class="card-body">
            <working-spinner v-if="isWorking"></working-spinner>
            <button v-else
                    class="btn btn-primary" v-on:click="handleCreatePublic">Create public version</button>

        </div>
        <div class="card-body " v-show="showUrl">
            <p class="card-text text-light">
                Link to public versions of first reading documents:<br>
                <a v-bind:href="publicUrl" target="_blank">{{ publicUrl }}</a>
            </p>
        </div>


    </div>
</template>

<script>
import WorkingSpinner from "../common/working-spinner";
export default {
    name: "public-folder-creation",
    components: {WorkingSpinner},
    props: ['plenaryId'],

    mixins: [],

    data: function () {
        return {
            // plenary_id: 1,
            publicUrl: null,
            isWorking : false
        }
    },

    asyncComputed: {
        showUrl: function () {
            return !_.isNull(this.url);
        }
    },

    computed: {},

    methods: {
        handleCreatePublic: function () {

            let url = window.routeRoot + '/secretary/public/' + this.plenaryId;
            window.console.log('committee', 'createPlenaries', 124, url);
            let me = this;
            this.isWorking = true;
            Vue.axios.post(url).then((response) => {
                window.console.log('committee', 'response', 126, response);
                me.url = response.data.publicUrl;
                me.isWorking = false;
            });


        }
    }

}
</script>

<style scoped>

</style>
