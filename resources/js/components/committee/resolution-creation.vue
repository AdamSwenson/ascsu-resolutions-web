<template>
    <div class="resolution-creation ">

        <div class="row top-spacer"></div>

        <error-alert></error-alert>

        <div class="row">
            <div class="col-lg-2">
            </div>

            <div class="col-lg-8">
                <div class="mb-2">
                    <h2 class="text-light text-center">{{ plenaryName }} Plenary</h2>
                </div>

                <creation-result :url="url" :title="title" v-if="showResult" :is-error="showError"></creation-result>

                <div class="resolution-creation-main" v-else>
                    <!--                <form>-->
                    <div class="mb-3">
                        <label for="resolutionTitle" class="form-label text-light h4 ">Resolution title</label>
                        <input type="text"
                               class="form-control"
                               id="resolutionTitle"
                               aria-describedby="resolutionTitleHelp"
                               v-model="title">
                        <div id="resolutionTitleHelp" class="form-text text-light">Enter the initial title of the
                            resolution here
                        </div>
                    </div>

                    <div class="mb-5 form-check">
                        <input type="checkbox" class="form-check-input" id="waiver"
                               v-model="waiver">
                        <label class="form-check-label text-light" for="waiver">Waiver requested?</label>
                    </div>

                    <!--                    <div class="mb-3">-->
                    <div class="row mb-3">
                        <div class="col-6">
                            <sponsor-select
                                v-on:sponsor="handleSponsor"
                                :committees="committees"
                            ></sponsor-select>
                        </div>

                        <div class="col-6">
                            <!--                    <div class="mb-3">-->
                            <cosponsors-select
                                :committees="committees"
                                v-on:cosponsor="handleCosponsor"
                            ></cosponsors-select>
                        </div>
                    </div>

                    <div class="mt-5">
                        <working-spinner v-if="isWorking"></working-spinner>

                        <p v-else class="">
                            <button
                                class="btn btn-primary btn-lg "
                                v-on:click="createRezzie"
                            >Create resolution
                            </button>
                        </p>
                    </div>
                    <!--                </form>-->
                </div>
                <div class="col-lg-2"></div>
            </div>
        </div>


    </div>

</template>

<script>
import PageFooter from "../layout/page-footer";
import SponsorSelect from "./sponsor-select";
import CosponsorsSelect from "./cosponsors-select";
import CreationResult from "./creation-result";
import plenaryMixin from "../../mixins/plenaryMixin";
import WorkingSpinner from "../common/working-spinner";
import ErrorAlert from "../common/error-alert";

export default {
    name: "resolution-creation",
    components: {ErrorAlert, WorkingSpinner, CreationResult, CosponsorsSelect, PageFooter, SponsorSelect},
    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {
            title: '',
            sponsor: null,
            cosponsors: [],
            // waiver_requested: false,
            waiver: false,
            committees: [
                'Academic Affairs',
                'Academic Preparation and Educational Programs',
                'Executive Committee',
                'Faculty Affairs',
                'Fiscal and Governmental Affairs',
                'Justice, Equity, Diversity, and Inclusion'
            ],
            isWorking: false,
            showError: false,
            showResult: false,
            url: null
        }
    },

    asyncComputed: {
    },

    computed: {
    },

    methods: {
        createRezzie: function () {
            window.console.log('committee', 'createRezzie', 124, this.$data);
            let url = window.routeRoot + '/resolution/' + this.plenaryId;
            let me = this;
            this.isWorking = true;
            Vue.axios.post(url, this.$data)
                .then((response) => {
                    window.console.log('committee', 'response', 126, response);
                    //This is needed in case we set error previously
                    me.$store.commit('resetError');
                    me.showResult = true;
                    me.isWorking = false;
                    me.showError = false;
                    me.url = response.data.url;
                }).catch(function (error) {
                // error handling
                if (error.response) {
                    me.showError = true;
                    me.isWorking = false;
                    //don't show the result so that can still retry
                    me.showResult = false;

                    me.$store.dispatch('showError', error.response.data);
                }
            });

        },

        handleSponsor: function (v) {
            window.console.log('committee', 'handleSponsor', 220, v);
            this.sponsor = v;
        },

        handleCosponsor: function (v) {
            //if already in, remove
            let idx = this.cosponsors.indexOf(v);
            window.console.log('committee', 'handleCosponsor', 229, idx);
            if (idx === -1) {
                this.cosponsors.push(v);
            } else {
                this.cosponsors.splice(idx, 1);
            }

        }
    }

}
</script>

<style scoped>

</style>
