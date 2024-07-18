<template>
    <div class="resolution-item-card card border-secondary mb-4">
        <div class="card-header h3 text-light">
            {{ resolutionNumber }} {{ title }}
        </div>
        <div class="card-body">
            <!--                <h5 class="card-title">Special title treatment</h5>-->
            <div class="row mb-3">
                <div class="col">
                    <p class="card-text text-light"><span class="bold">Sponsor:</span> {{ sponsorName }}</p>

                    <p class="card-text text-light"
                       v-if="showCosponsors"><span class="fw-bold">Cosponsors:</span> {{ cosponsorNames }}</p>

                </div>

                <div class="col">
                    <p class="card-text text-light">First reading: {{ firstReadingName }}</p>

                    <p class="card-text text-light"
                       v-for="p in secondReadingNames"
                       :key="p"
                    >Action item: {{ p }}</p>

                </div>
            </div>

            <p class="card-text text-light">
                <a v-bind:href="url" target="_blank">{{ url }}</a>
            </p>

            <p class="card-text">
                <status-badge :resolution-id="resolutionId"></status-badge>&nbsp;&nbsp;
                <reading-type-badge :resolution-id="resolutionId"></reading-type-badge>
            </p>

        </div>

        <div class="card-body" v-if="isSecretary">
            <div class="row">
                <div class="col">
                    <permissions-control-card :resolution-id="resolutionId"></permissions-control-card>

                </div>

                <div class="col">
                    <approval-control-card :resolution-id="resolutionId"></approval-control-card>
                </div>

                <div class="col">
                    <committee-control-card :resolution-id="resolutionId"></committee-control-card>
                </div>
            </div>
        </div>


        <div class="card-footer">
            <p class="text-light">Manage resolution status </p>

            <working-spinner v-show="showWorking"></working-spinner>
            <status-toggle v-show="! showWorking"
                           :resolutionId="resolutionId"
                           v-on:reading-working="handleWorking"
                           v-on:reading-done="handleDone"
            ></status-toggle>
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
import CommitteeChanger from "../../common/committee-change/committee-changer";
import CommitteeChangeButton from "../../common/committee-change/committee-change-button";
import CommitteeChangeModal from "../../common/committee-change/committee-change-modal";
import StatusToggle from "../../committee/management/status-toggle";
import resolutionMixin from "../../../mixins/resolutionMixin";
import WorkingSpinner from "../../common/working-spinner";
import PermissionsControlCard from "./controls/permissions-control-card";
import ApprovalControlCard from "./controls/approval-control-card";
import CommitteeControlCard from "./controls/committee-control-card";

export default {
    name: "resolution-item-card",
    components: {
        CommitteeControlCard,
        ApprovalControlCard,
        PermissionsControlCard,
        WorkingSpinner,
        StatusToggle,
        CommitteeChangeModal,
        CommitteeChangeButton,
        CommitteeChanger,
        SecondReadingToggleButton,
        WaiverToggleButton,
        ReadingTypeBadge,
        StatusBadge,
        FailedToggleButton,
        ApprovedToggleButton,
        ResolutionPermissionButton
    },

    props: [
        'resolutionId',

        // whether the approved/failed buttons and permissions show
        'isSecretary'
    ],


    mixins: [resolutionMixin],

    data: function () {
        return {
            isReadingTypeWorking: false
        }
    },

    asyncComputed: {
        showWorking: function () {
            return this.isReadingTypeWorking;
        },
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
            return this.isWaiver;
            // if (!isReadyToRock(this.waiver)) return false;
            // return this.waiver === 1;
        },

        /**
         * name of the sponsoring committee
         * @returns {string}
         */
        sponsorName: function () {
            if (!isReadyToRock(this.resolution)) return '';
            return this.resolution.sponsor.abbreviation;

        },

        /**
         * Comma separated list of cosponsoring committee names
         * @returns {string}
         */
        cosponsorNames: function () {
            if (!isReadyToRock(this.resolution)) return '';
            if (this.resolution.cosponsors.length === 0) return '';

            let cosponsors = [];
            _.forEach(this.resolution.cosponsors, (c) => {
                cosponsors.push(c.abbreviation);
            });
            return _.join(cosponsors, ', ');
        },

        /**
         * Whether to display the list of cosponsors
         * @returns {boolean}
         */
        showCosponsors: function () {
            if (!isReadyToRock(this.resolution)) return false;
            return this.resolution.cosponsors.length !== 0;
        }

    },

    computed: {},

    methods: {
        handleWorking: function () {
            this.isReadingTypeWorking = true;
            window.console.log('resolution-item-card', 'toggleIsReadingTypeWorking', 184, this.isReadingTypeWorking);
        },

        handleDone: function () {
            this.isReadingTypeWorking = false;
            window.console.log('resolution-item-card', 'handleDone', 189, this.isReadingTypeWorking);

        }
    }

}
</script>

<style scoped>

</style>
