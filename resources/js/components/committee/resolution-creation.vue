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

                    <div class="row mb-3">
                        <div class="col-6">
                            <committee-select type="sponsor"
                                              :light-heading="true"
                            ></committee-select>
                        </div>

                        <div class="col-6">
                            <committee-select type="cosponsor"
                                              :light-heading="true"
                            ></committee-select>
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
                </div>
                <div class="col-lg-2"></div>
            </div>
        </div>


    </div>

</template>

<script>
import plenaryMixin from "../../mixins/plenaryMixin";
import committeeMixin from "../../mixins/committeeMixin";
import PageFooter from "../layout/page-footer";
import CreationResult from "./creation-result";
import WorkingSpinner from "../common/working-spinner";
import ErrorAlert from "../common/error-alert";
import CommitteeSelect from "../common/committee-change/committee-select";

export default {
    name: "resolution-creation",
    components: {
        CommitteeSelect,
        ErrorAlert,
        WorkingSpinner,
        CreationResult,
        PageFooter,
    },
    props: [],

    mixins: [plenaryMixin, committeeMixin],

    data: function () {
        return {
            title: '',
            waiver: false,
            isWorking: false,
            showError: false,
            showResult: false,
            url: null
        }
    },

    asyncComputed: {
        sponsor: function () {
            return this.$store.getters.getSelectedSponsor;
        },

        cosponsors : function(){
            return this.$store.getters.getSelectedCosponsorsNames;
        }

    },

    computed: {},

    methods: {
        createRezzie: function () {
            window.console.log('committee', 'createRezzie', 124, this.$data);
            let url = window.routeRoot + '/resolution/' + this.plenaryId;
            let me = this;
            let payload = this.$data;
            payload['sponsor'] = this.sponsor.name;
            payload['cosponsors'] = this.cosponsors;

            this.isWorking = true;
            Vue.axios.post(url, payload)
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

    }

}
</script>

<style scoped>

</style>
