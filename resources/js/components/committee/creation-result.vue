<template>
<div class="creation-result ">

    <div class="card">
            <h4 class="card-title text-light" >{{title}}</h4>

        <div class="card-body">
            <p class="card-text text-light">
                Your resolution has been created! You can find it here:
            </p>
            <p class="card-text text-light">
                <a v-bind:href="url" target="_blank">{{url}}</a>
            </p>

        </div>
        <div class="card-body">
            <p class="card-text">
                <button class="btn btn-success" v-on:click="reloadPage">Create a new resolution</button>
            </p>
        </div>
    </div>


    </div>
</template>

<script>
export default {
    name: "creation-result",

    props: ['title', 'url'],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {
        showResult : function(){
            return !_.isNull(this.title) && !_.isNull(this.url)
        }
    },

    computed: {},

    methods: {
        reloadPage: function(){
            location.reload();
        }
    }

}
</script>

<style scoped>

</style>
