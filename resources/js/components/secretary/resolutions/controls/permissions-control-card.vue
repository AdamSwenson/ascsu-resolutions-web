<template>
    <div class="permissions-control-card card">
        <div class="card-body">
            <h5 class="card-title text-light">Manage editing permissions</h5>

            <resolution-permission-button
                :resolution-id="resolutionId"
            ></resolution-permission-button>
            <p class="card-text text-light small">[add something which makes it clearer who can currently edit]</p>
        </div>

    </div>

</template>

<script>
import ResolutionPermissionButton from "../resolution-permission-button";
export default {
    name: "permissions-control-card",
    components: {ResolutionPermissionButton},
    props: ['resolutionId'],

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
