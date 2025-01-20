<template>
    <div class="bulk-move-dialog card">
        <div class="card-title text-light">Move first readings and working drafts</div>

        <div class="row">
            <div class="col-sm-6">
                <div class="card">
                    <div class="card-title text-light">From plenary</div>
                    <div class="card-body" v-show="source.plenaryName">
                        <div class="card-text text-light">{{ source.plenaryName }}</div>
                    </div>
                    <div class="card-body">
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item" v-for="p in sourcePlenaries" :key="p.thursday_date">
                                <a href="#" class="btn btn-sm btn-outline-primary"
                                   v-on:click="setAsSource(p)"
                                >Select</a> {{ p.plenaryName }}
                            </li>
                        </ul>

                    </div>
                </div>
            </div>

            <div class="col-sm-6">
                <div class="card">
                    <div class="card-title text-light">To plenary</div>
                    <div class="card-body" v-show="destination.plenaryName">
                        <div class="card-text text-light">{{ destination.plenaryName }}</div>
                    </div>
                    <div class="card-body">
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item" v-for="p in destinationPlenaries" :key="p.thursday_date">
                                <a href="#" class="btn btn-sm btn-outline-primary"
                                   v-on:click="setAsDestination(p)"
                                >Select</a> {{ p.plenaryName }}
                            </li>
                        </ul>

                    </div>
                    <!--                    <li class="list-group-item">-->
                    <!--                        <a href="#" class="btn btn-sm "-->
                    <!--                           v-bind:class="styling"-->
                    <!--                           v-on:click="setAsSource"-->
                    <!--                        >Select</a> {{ plenaryName }}-->
                    <!--                    </li>-->
                    <!--                    <div class="card-body">-->
                    <!--                    </div>-->
                </div>
            </div>
            .
        </div>
        <div class="card-footer" v-show="showButton">
            <button class="btn btn-warning" v-on:click="handleMove">Move</button>
        </div>

    </div>

</template>

<script>
import plenaryMixin from "../../../mixins/plenaryMixin";
import {isReadyToRock} from "../../../utilities/readiness.utilities";

export default {
    name: "bulk-move-dialog",

    props: [],

    mixins: [plenaryMixin,],

    data: function () {
        return {
            source: '',
            destination: ''
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
            window.console.log('bulk-move-dialog', 'handleMove', 100, this.source, this.destination);
        }
    }

}
</script>

<style scoped>

</style>
