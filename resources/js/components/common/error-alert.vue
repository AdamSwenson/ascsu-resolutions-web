<template>
<div class="error-alert alert alert-danger d-flex align-items-center"
     role="alert">
        <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:"><use xlink:href="#exclamation-triangle-fill"/></svg>
        <div>
            Something has gone wrong. Please try again.
        </div>
    </div>
</template>

<script>
export default {
    name: "error-alert",

    props: [],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {}

}
</script>

<style scoped>

</style>
