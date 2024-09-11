<template>
<div class="approval-control-card card">
        <div class="card-body">
            <h5 class="card-title text-light">Manage approval status</h5>

            <approved-toggle-button :resolution-id="resolutionId"
            ></approved-toggle-button>&nbsp;

            <failed-toggle-button :resolution-id="resolutionId"
            ></failed-toggle-button>

            <p class="card-text text-light small">These record the resolution as approved or failed and adds the word 'Approved' to the document when approved</p>
        </div>
    </div>

</template>

<script>
import ApprovedToggleButton from "../approved-toggle-button";
import FailedToggleButton from "../failed-toggle-button";
export default {
    name: "approval-control-card",
    components: {FailedToggleButton, ApprovedToggleButton},
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
