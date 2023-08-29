<template>
        <div class="committee py-2">

    <resolution-creation></resolution-creation>

        <page-footer></page-footer>
    </div>

</template>

<script>
import PageFooter from "../layout/page-footer";
import SponsorSelect from "./sponsor-select";
import CosponsorsSelect from "./cosponsors-select";
import CreationResult from "./creation-result";
import ResolutionCreation from "./resolution-creation";

export default {
    name: "committee",
    components: {ResolutionCreation, CreationResult, CosponsorsSelect, PageFooter, SponsorSelect},
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
        // createRezzie: function () {
        //     window.console.log('committee', 'createRezzie', 124,this.$data);
        //     let url = window.routeRoot + '/committee'
        //     let me = this;
        //     Vue.axios.post(url, this.$data).then((response) => {
        //         window.console.log('committee', 'response', 126,response);
        //     me.url = response.data.url;
        //     });
        // },
        // handleSponsor: function (v) {
        //     window.console.log('committee', 'handleSponsor', 220, v);
        //     this.sponsor = v;
        // },
        // handleCosponsor: function (v) {
        //     //if already in, remove
        //     let idx = this.cosponsors.indexOf(v);
        //     window.console.log('committee', 'handleCosponsor', 229, idx);
        //     if(idx === -1){
        //         this.cosponsors.push(v);
        //     }else{
        //         this.cosponsors.splice(idx, 1);
        //     }
        //
        // }
    }

}
</script>

<style scoped>
/*.top-spacer {*/
/*    margin-top: 20px;*/
/*}*/
</style>
