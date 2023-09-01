<template>
    <div class="creation-result ">

        <div class="error-card card" v-if="isError">

            <div class="card-body">
                <p class="card-text text-light">
                    Click the button below to try again.
                </p>
                <p class="card-text">
                    <button class="btn btn-warning" v-on:click="reloadPage">Try again</button>
                </p>
                <p class="card-text text-light">If you see this message multiple times, something has gone terribly wrong. In that case, please
                    create the resoution in drive the old fashioned way and notify the ASCSU secretary immediately.</p>
            </div>
        </div>

        <div class="card" v-else>
            <h4 class="card-title text-light">{{ title }}</h4>

            <div class="card-body">
                <p class="card-text text-light">
                    Your resolution has been created! You can find it here:
                </p>
                <p class="card-text text-light">
                    <a v-bind:href="url" target="_blank">{{ url }}</a>
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

    props: ['title', 'url', 'isError'],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {
        showResult: function () {
            return !_.isNull(this.title) && !_.isNull(this.url)
        },


    },

    computed: {},

    methods: {
        reloadPage: function () {
            location.reload();
        }
    }

}
</script>

<style scoped>

</style>
