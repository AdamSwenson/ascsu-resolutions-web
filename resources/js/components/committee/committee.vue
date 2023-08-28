<template>

    <div class="committee py-2">
        <div class="row top-spacer"></div>
        <div class="row">
            <div class="col-lg-2"></div>

            <div class="col-lg-8">

                <creation-result :url="url" :title="title"></creation-result>

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
                            <!--                        <label for="sponsor" class="form-label text-light">Sponsoring committee</label>-->
                            <!--                        <select id="sponsor" class="form-select" aria-label="sponsoring committee">-->
                            <!--                            <option value="1">Academic Affairs</option>-->
                            <!--                            <option value="2">One</option>-->
                            <!--                            <option value="3">Two</option>-->
                            <!--                            <option value="4">Three</option>-->
                            <!--                        </select>-->
                        </div>
                        <div class="col-6">
                            <!--                    <div class="mb-3">-->
                            <cosponsors-select
                                :committees="committees"
                                v-on:cosponsor="handleCosponsor"
                            ></cosponsors-select>
                        </div>
                        <!--                        <label for="cosponsors" class="form-label text-light">Cosponsoring committees</label>-->
                        <!--                        <select id="cosponsors" class="form-select" aria-label="cosponsoring committees">-->
                        <!--                            <option value="1">Academic Affairs</option>-->
                        <!--                            <option value="2">One</option>-->
                        <!--                            <option value="3">Two</option>-->
                        <!--                            <option value="4">Three</option>-->
                        <!--                        </select>-->
                    </div>

                    <div class="mt-5">
                        <p class="">
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

        <page-footer></page-footer>
    </div>

</template>

<script>
import PageFooter from "../layout/page-footer";
import SponsorSelect from "./sponsor-select";
import CosponsorsSelect from "./cosponsors-select";
import CreationResult from "./creation-result";

export default {
    name: "committee",
    components: {CreationResult, CosponsorsSelect, PageFooter, SponsorSelect},
    props: [],

    mixins: [],

    data: function () {
        return {
            title: '',
            sponsor: null,
            cosponsors: [],
            // waiver_requested: false,
            waiver: false,
            committees: [
                'Academic Affairs',
                'Academic Preparation EP',
                'Executive Committee',
                'Faculty Affairs',
                'Fiscal and Governmental Affairs',
                'Justice, Equity, Diversity, and Inclusion'
            ],
            url : null
        }
    },

    asyncComputed: {},

    computed: {
        // wavier: {
        //     get: function () {
        //         return this.waiver_requested;
        //     },
        //     set: function (v) {
        //         this.waiver_requested = v;
        //     }
        // }
    },

    methods: {
        createRezzie: function () {
            window.console.log('committee', 'createRezzie', 124,this.$data);
            let url = window.routeRoot + '/committee'
            let me = this;
            Vue.axios.post(url, this.$data).then((response) => {
                window.console.log('committee', 'response', 126,response);
            me.url = response.data.url;
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
            if(idx === -1){
                this.cosponsors.push(v);
            }else{
                this.cosponsors.splice(idx, 1);
            }

        }
    }

}
</script>

<style scoped>
.top-spacer {
    margin-top: 20px;
}
</style>
