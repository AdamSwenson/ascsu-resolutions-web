<template>
    <div class="bulk-move-dialog card">
        <h3 class="card-title text-light">Move first readings and working drafts</h3>

        <div class="row">
            <div class="col-md-6">
                <div class="card">

                    <div class="card-header text-light">
                        <h4 class="card-title">From plenary</h4>
                    </div>

                    <div class="card-body" v-show="source.plenaryName">
                        <p class="card-text text-light ">{{ source.plenaryName }}</p>
                    </div>

                    <div class="card-body">
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item" v-for="p in sourcePlenaries" :key="p.thursday_date">
                                <a href="#"
                                   class="btn btn-sm "
                                   v-bind:class="p.plenaryName === source.plenaryName ? 'btn-primary' : 'btn-outline-primary' "
                                   v-on:click="setAsSource(p)"
                                >Select</a> {{ p.plenaryName }}
                            </li>
                        </ul>



                    </div>
                </div>
            </div>

            <div class="col-md-6">
                <div class="card">

                    <div class="card-header text-light">
                        <h4 class="card-title text-light">To plenary</h4>
                    </div>

                    <div class="card-body" v-show="destination.plenaryName">
                        <div class="card-text text-light">{{ destination.plenaryName }}</div>
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

                    </div>

                </div>
            </div>
            <p class="text-light card-text small">Moves the resolution files to the selected plenary's working drafts folder. First reading resolutions will remain listed on the source plenary's agenda. </p>

        </div>
        <div class="card-footer" v-show="showButton">
            <working-spinner v-if="isWorking"></working-spinner>

            <button class="btn btn-warning" v-else
                    v-on:click="handleMove"
            >Move</button>
        </div>

    </div>

</template>

<script>
import plenaryMixin from "../../../mixins/plenaryMixin";
import {isReadyToRock} from "../../../utilities/readiness.utilities";
import WorkingSpinner from "../../common/working-spinner";

export default {
    name: "bulk-move-dialog",
    components: {WorkingSpinner},
    props: [],

    mixins: [plenaryMixin,],

    data: function () {
        return {
            source: '',
            destination: '',
            isWorking : false
        }
    },

    asyncComputed: {
        sourcePlenaries: function () {
            return this.academicYearPlenaries;
        },

        destinationPlenaries: function () {
            return this.academicYearPlenaries;
        },
        showButton: function () {

            return isReadyToRock(this.source.id) && isReadyToRock(this.destination.id);
        }
    },

    computed: {},

    methods: {
        setAsSource: function (v) {
            this.source = v;
            window.console.log('bulk-move-dialog', 'setAsSource', 76, v);
        },

        setAsDestination: function (v) {
            this.destination = v;
        },

        handleMove: function () {
            let me = this;
            //dev Check that plenaries aren't the same
            window.console.log('bulk-move-dialog', 'handleMove', 100, this.source, this.destination);
            let payload = {sourcePlenary: this.source, destinationPlenary: this.destination};
            me.isWorking = true;
            this.$store.dispatch('moveResolutionsBetweenPlenaries', payload).then((r) => {
                me.isWorking = false;
            });

        }
    }

}
</script>

<style scoped>

</style>
