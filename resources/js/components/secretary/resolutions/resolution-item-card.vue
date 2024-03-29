<template>
    <div class="resolution-item-card card mb-3">
        <div class="card-header h3 text-light">
            {{ number }} {{ title }}
        </div>
        <div class="card-body">
            <!--                <h5 class="card-title">Special title treatment</h5>-->

            <p class="card-text text-light">First reading: {{ firstReadingName }}</p>

            <p class="card-text text-light"
               v-for="p in secondReadingNames"
               :key="p"
            >Action item: {{ p }}</p>

            <p class="card-text">
                <status-badge :resolution-id="resolutionId"></status-badge>&nbsp;&nbsp;
                <reading-type-badge :resolution-id="resolutionId"></reading-type-badge>
            </p>

            <!--            <p class="card-text text-light" v-if="isApproved || showWaiverIndicator"-->
            <!--            ><span-->
            <!--                class="badge rounded-pill bg-success"-->
            <!--                v-if="isApproved"-->
            <!--            >Approved</span> <span-->
            <!--                class="badge rounded-pill bg-warning"-->
            <!--                v-if="showWaiverIndicator"-->
            <!--            >Waiver</span>-->

            <!--            </p>-->

        </div>
        <div class="card-footer">
            <resolution-permission-button :resolution-id="resolutionId"></resolution-permission-button>&nbsp;&nbsp;&nbsp;&nbsp;
            <approved-toggle-button :resolution-id="resolutionId"></approved-toggle-button>&nbsp;
            <failed-toggle-button :resolution-id="resolutionId"></failed-toggle-button>&nbsp;&nbsp;&nbsp;&nbsp;
            <second-reading-toggle-button :resolution-id="resolutionId"></second-reading-toggle-button>
            <waiver-toggle-button :resolution-id="resolutionId"></waiver-toggle-button>
        </div>
    </div>
</template>

<script>
import ResolutionPermissionButton from "./resolution-permission-button";
import ApprovedToggleButton from "./approved-toggle-button";
import {isReadyToRock} from "../../../utilities/readiness.utilities";
import FailedToggleButton from "./failed-toggle-button";
import StatusBadge from "./status-badge";
import ReadingTypeBadge from "./reading-type-badge";
import WaiverToggleButton from "./waiver-toggle-button";
import SecondReadingToggleButton from "./second-reading-toggle-button";

export default {
    name: "resolution-item-card",
    components: {
        SecondReadingToggleButton,
        WaiverToggleButton,
        ReadingTypeBadge,
        StatusBadge,
        FailedToggleButton,
        ApprovedToggleButton,
        ResolutionPermissionButton
    },

    props: ['resolutionId', 'title', 'number', 'isApproved', 'firstReadingPlenary',
        'actionPlenaries', 'waiver'],


    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {
        resolution: function () {
            return this.$store.getters.getResolution(this.resolutionId);
        },

        firstReadingName: function () {
            if (!isReadyToRock(this.firstReadingPlenary)) return '';

            return this.firstReadingPlenary.plenaryName;

        },
        secondReadingNames: function () {
            if (!isReadyToRock(this.actionPlenaries)) return [];
            let n = [];
            _.forEach(this.actionPlenaries, (p) => {
                n.push(p.plenaryName)
            });
            return n;
        },

        showWaiverIndicator: function () {
            if (!isReadyToRock(this.waiver)) return false;
            return this.waiver === 1;
        }
    },

    computed: {},

    methods: {}

}
</script>

<style scoped>

</style>
