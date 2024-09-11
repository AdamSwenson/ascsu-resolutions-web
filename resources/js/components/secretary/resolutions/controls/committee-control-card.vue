<template>
    <div class="committee-control-card card">
        <div class="card-body">
            <h5 class="card-title text-light">Manage sponsors and cosponsors</h5>
            <!--            <committee-change-button :resolution-id="resolutionId"></committee-change-button> <committee-change-modal :resolution-id="resolutionId"></committee-change-modal>-->

            <committee-changer :resolution-id="resolutionId"></committee-changer>
        </div>

    </div>
</template>

<script>
import CommitteeChanger from "../../../common/committee-change/committee-changer";

export default {
    name: "committee-control-card",
    components: {CommitteeChanger},
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
