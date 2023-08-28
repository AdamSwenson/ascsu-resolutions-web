<template>
<div class="creation-result " v-show="showResult">

    <div class="card">
        <div class="card-header">
            <h4>{{title}}</h4>
        </div>

        <div class="card-body">
            <p class="card-text">
                Your resolution has been created! You can find it here:
            </p>
            <p class="card-text">
                <a v-bind:href="url" target="_blank">{{url}}</a>
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

    methods: {}

}
</script>

<style scoped>

</style>
