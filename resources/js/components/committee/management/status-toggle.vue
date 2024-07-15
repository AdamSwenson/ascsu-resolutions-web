<template>
    <!--<div class="status-toggle btn-group"-->
    <!--     role="group"-->
    <!--     aria-label="resolution status toggle button group">-->
    <!--        <input type="radio"-->
    <!--               class="btn-check"-->
    <!--               name="statusradio"-->
    <!--               id="statusradio1"-->
    <!--               autocomplete="off" >-->
    <!--        <label class="btn btn-outline-primary" for="btnradio1">Radio 1</label>-->

    <!--        <input type="radio" class="btn-check" name="statusradio" id="statusradio2" autocomplete="off">-->
    <!--        <label class="btn btn-outline-primary" for="btnradio2">Radio 2</label>-->

    <!--        <input type="radio" class="btn-check" name="statusradio" id="statusradio3" autocomplete="off">-->
    <!--        <label class="btn btn-outline-primary" for="btnradio3">Radio 3</label>-->

    <!--    </div>-->

    <div class="status-toggle">
        <p class="text-light">Manage resolution status </p>
        <div class=" btn-group"
             role="group"
             aria-label="resolution status toggle button group"
        >
            <button type="button"
                    class="btn "
                    v-bind:class="firstStyling"
                    v-on:click="setFirstReading"
            >First reading (regular)
            </button>

            <button type="button"
                    class="btn "
                    v-bind:class="waiverStyling"
                    v-on:click="setWaiver"
            >First reading waiver
            </button>

            <button type="button"
                    class="btn "
                    v-bind:class="workingStyling"
                    v-on:click="setWorking"
            >Working draft
            </button>

            <button type="button"
                    class="btn "
                    v-bind:class="actionStyling"
                    v-on:click="setAction"
            >Action item
            </button>
        </div>
        <p class="text-light small">These buttons move the resolution to the corresponding folder for the
            {{ plenaryName }} plenary</p>
    </div>
</template>

<script>
import resolutionMixin from "../../../mixins/resolutionMixin";
import plenaryMixin from "../../../mixins/plenaryMixin";
import {isReadyToRock} from "../../../utilities/readiness.utilities";

export default {
    name: "status-toggle",

    /**
     * Resolution object
     */
    props: ['resolutionId'],

    mixins: [resolutionMixin, plenaryMixin],

    data: function () {
        return {
            styles: {
                unselected: "btn-outline-primary ",
                selected: "btn-primary"
            }
        }
    },

    asyncComputed: {

        plenaryName: function () {
            if(! isReadyToRock(this.plenary)) return ""
            return this.plenary.plenaryName;
        },

        firstStyling: function () {
            // if(isReadyToRock(this.resolution) && this.resolution.status === 'first'){
            if (this.isFirstReading) {
                return this.styles.selected;
            }
            return this.styles.unselected;
        },

        workingStyling: function () {
            if (this.isWorking) {
                // if(isReadyToRock(this.resolution) && this.resolution.status === 'working'){
                return this.styles.selected;
            }
            return this.styles.unselected;
        },

        actionStyling: function () {
            if (this.isActionItem) {
                // if(isReadyToRock(this.resolution) && this.resolution.status === 'action'){
                return this.styles.selected;
            }
            return this.styles.unselected;
        },

        waiverStyling: function(){
            if (this.isWaiver) {
                return this.styles.selected;
            }
            return this.styles.unselected;

        }

    },

    computed: {},

    methods: {
        setFirstReading: function () {
            window.console.log('status-toggle', 'setFirstReading', 95);
            this.$store.dispatch('setFirstReading', this.resolution);
            //todo display the link afterwards
        },
        setWorking: function () {
            window.console.log('status-toggle', 'setWorking', 98,);
            this.$store.dispatch('setWorkingDraft', this.resolution);
            //todo display the link afterwards
        },
        setAction: function () {
            window.console.log('status-toggle', 'setAction', 101,);
            this.$store.dispatch('setActionItem', this.resolution);
            //todo display the link afterwards
        },
        setWaiver: function () {
            window.console.log('status-toggle', 'setWaiver', 101,);
            this.$store.dispatch('setWaiver', this.resolution);
            //todo display the link afterwards
        },

    }

}
</script>

<style scoped>

</style>
