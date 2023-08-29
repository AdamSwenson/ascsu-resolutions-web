<template>
    <div class="public-folder-creation card">
        <h3 class="card-title text-light">Public version</h3>


        <div class="card-body">
            <button class="btn btn-primary" v-on:click="handleCreatePublic">Create public version</button>

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
export default {
    name: "public-folder-creation",

    props: ['plenaryId'],

    mixins: [],

    data: function () {
        return {
            // plenary_id: 1,
            publicUrl: null
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
            Vue.axios.post(url).then((response) => {
                window.console.log('committee', 'response', 126, response);
                me.url = response.data.publicUrl;
            });


        }
    }

}
</script>

<style scoped>

</style>
