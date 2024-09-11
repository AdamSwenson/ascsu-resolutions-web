<template>
    <nav id="pageNav"
         class=" committee-navbar navbar navbar-expand-md navbar-dark shadow-sm ">

        <!--    <nav class="navbar navbar-expand-md navbar-light bg-white shadow-sm">-->
        <div class="container-fluid  ">
            <!--                <span class="navbar-brand  mb-0 ms-lg-5 ms-1 h1">{{ meetingName }}</span>-->

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <!-- Left Side Of Navbar -->
                <ul class="navbar-nav ms-auto "></ul>

                <!-- Right Side Of Navbar -->

                <form class="d-flex me-3">
                    <button
                        class="btn btn-outline-success"
                        v-on:click="openCreation"
                        v-if="shownPage === 'management'"
                    >Create resolution
                    </button>
                </form>

                <form class="d-flex me-3">
                    <button
                        class="btn btn-outline-success"
                        v-on:click="openManagement"
                        v-if="shownPage === 'creation'"
                    >Manage resolutions
                    </button>
                </form>


            </div>
        </div>
    </nav>

</template>

<script>
export default {
    name: "committee-navbar",

    props: ['shownPage'],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {

        openManagement: function () {
            this.$emit('open-management');
        },

        openCreation: function () {
            this.$emit('open-creation');
        }
    }

}
</script>

<style scoped>

</style>
