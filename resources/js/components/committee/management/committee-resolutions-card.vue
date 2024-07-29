<template xmlns="http://www.w3.org/1999/html">
    <div class="resolution-card card">
<!--        <h3 class="card-title text-light">Manage individual resolutions</h3>-->

        <div class="card-body text-center">

            <button class="btn btn-small "
                    v-bind:class="currentButtonStyle"
                    v-on:click="setSelected('current')"
            >Current plenary
            </button>

            <button class="btn btn-small "
                    v-bind:class="unapprovedButtonStyle"
                    v-on:click="setSelected('unapproved')"
            >Unapproved
            </button>

            <button class="btn btn-small "
                    v-bind:class="allButtonStyle"
                    v-on:click="setSelected('all')"
            >All
            </button>

        </div>

        <div class="card-body">

            <resolution-item-card
                :is-secretary="false"
                :resolution-id="r.id"

                :key="r.id"
                v-for="r in resolutions"
            ></resolution-item-card>

<!--            <resolution-item-card-->
<!--                :is-secretary="false"-->
<!--                :resolution-id="r.id"-->
<!--                :title="r.title"-->
<!--                :number="r.formattedNumber"-->
<!--                :is-approved="r.is_approved"-->
<!--                :first-reading-plenary="r.firstReadingPlenary"-->
<!--                :action-plenaries="r.actionPlenaries"-->
<!--                :waiver="r.waiver"-->
<!--                :key="r.id"-->
<!--                v-for="r in resolutions"-->
<!--            ></resolution-item-card>-->
            <!--        <ul class="list-group list-group-flush">-->
            <!--            <resolution-item :resolution-id="r.id"-->
            <!--                             :title="r.title"-->
            <!--                             :number="r.formattedNumber"-->
            <!--                             :is-approved="r.is_approved"-->
            <!--                             :first-reading-plenary="r.firstReadingPlenary"-->
            <!--                             :action-plenaries="r.actionPlenaries"-->
            <!--                             :key="r.resolutionId"-->
            <!--                             v-for="r in resolutions"-->
            <!--            ></resolution-item>-->
            <!--        </ul>-->
        </div>

    </div>

</template>

<script>
import * as routes from "../../../routes";
import plenaryMixin from "../../../mixins/plenaryMixin";
// import ResolutionItem from "./resolution-item";

import {isReadyToRock} from "../../../utilities/readiness.utilities";
import ResolutionItemCard from "../../secretary/resolutions/resolution-item-card";

export default {
    name: "committee-resolutions-card",

    components: {ResolutionItemCard},

    /**
     * Committee object
     */
    props: ['committee'],

    mixins: [plenaryMixin],

    data: function () {
        return {
            selected: 'current',

            styles: {
                unselected: 'btn-outline-primary',
                selected: 'btn-primary'
            }
        }
    },

    asyncComputed: {
        allButtonStyle: function () {
            if (this.selected === 'all') {
                return this.styles.selected;
            }
            return this.styles.unselected;

        },
        currentButtonStyle: function () {
            if (this.selected === 'current') {
                return this.styles.selected;
            }
            return this.styles.unselected;
        },
        unapprovedButtonStyle: function () {
            if (this.selected === 'unapproved') {
                return this.styles.selected;
            }
            return this.styles.unselected;
        },

        // isReady : function(){
        //   return this.$store.getters.getIsReady;
        // },

        committeeResolutions: function () {
            let rez = [];

            if (isReadyToRock(this.committee)) {
                _.forEach( this.$store.getters.getCommitteeResolutions(this.committee), (r) => {
                    if (r.status !== 'approved') {
                        rez.push(r);
                    }
                });

                // return this.$store.getters.getCommitteeResolutions(this.committee);
            }
            return rez

        },

        resolutions: {
            get: function ()
            {
                return this.committeeResolutions;

                let r;

                switch (this.selected) {
                    case "all":
                        r = this.committeeResolutions;
                        break;
                    case "current":
                        r = this.$store.getters.getCurrentPlenaryResolutions;
                        break;
                    case "unapproved":
                        r = this.$store.getters.getUnapprovedResolutions;
                        break;
                }

                if (isReadyToRock(r)) return r;
                return [];

            },
            // watch: ['isReady']
        }
    },

    watch: {
        // 'plenaryId': function(){this.loadResolutions();}
    },

    computed: {},

    methods: {
        setSelected: function (v) {
            this.selected = v;
        }


        //
        // loadResolutions: function () {
        //     //todo Need some way to restrict these to active ones
        //
        //     let url = routes.secretary.resolutions.loadForPlenary(this.plenaryId);
        //
        //     window.console.log('resolutions', 'get', 124, url);
        //     let me = this;
        //     Vue.axios.get(url).then((response) => {
        //         me.rez = response.data;
        //     });
        //
        // }

    }, mounted() {
        // if (isReadyToRock(this.plenaryId)) {
        //     // this.loadResolutions();
        // }
    }

}
</script>

<style scoped>

</style>
