<template>
    <div class="single-move-dialog card ">
        <h5 class="card-title text-light">Move to plenary</h5>

        <div class="card-body" v-show="destination.plenaryName">
            <p class="card-text text-light ">{{ destination.plenaryName }}</p>
        </div>

        <div class="card-body">
            <ul class="list-group list-group-flush">
                <li class="list-group-item" v-for="p in destinationPlenaries" :key="p.thursday_date">
                    <a href="#"
                       class="btn btn-sm "
                       v-bind:class="p.plenaryName === destination.plenaryName ? 'btn-primary' : 'btn-outline-primary' "
                       v-on:click="setAsDestination(p)"
                    >Select</a> {{ p.plenaryName }}
                </li>
            </ul>

            <p class="text-light small">Moves the resolution file to the selected plenary's working drafts folder. </p>

        </div>
        <div class="card-footer" v-show="showButton">
            <working-spinner v-if="isWorking"></working-spinner>

            <button class="btn btn-warning" v-else
                    v-on:click="handleMove"
            >Move
            </button>
        </div>

    </div>
</template>

<script>
import {isReadyToRock} from "../../../utilities/readiness.utilities";
import WorkingSpinner from "../../common/working-spinner";
import plenaryMixin from "../../../mixins/plenaryMixin";

export default {
    name: "single-move-dialog",
    components: {WorkingSpinner},
    props: ['resolutionId'],

    mixins: [plenaryMixin,],

    data: function () {
        return {
            destination: '',
            isWorking: false
        }
    },

    asyncComputed: {
        destinationPlenaries: function () {
            return this.academicYearPlenaries;
        },
        showButton: function () {

            return isReadyToRock(this.destination.id);
        }
    },

    computed: {},

    methods: {
        setAsDestination: function (v) {
            this.destination = v;
        },

        handleMove: function () {
            let me = this;
            let payload = {destinationPlenary: this.destination, resolution: this.resolutionId};
            me.isWorking = true;
            this.$store.dispatch('moveResolutionToPlenary', payload).then((r) => {
                me.isWorking = false;
            });

        }
    }

}
</script>

<style scoped>

</style>
