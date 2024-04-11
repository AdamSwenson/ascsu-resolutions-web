<template>
    <div class="committee py-2">

        <resolution-creation></resolution-creation>

        <page-footer></page-footer>
    </div>

</template>

<script>
import PageFooter from "../layout/page-footer";
// import SponsorSelect from "./sponsor-select";
// import CosponsorsSelect from "../attic/cosponsors-select";
// import CreationResult from "./creation-result";
import ResolutionCreation from "./resolution-creation";
import {isReadyToRock} from "../../utilities/readiness.utilities";
// import CommitteeSelect from "../secretary/resolutions/committee-change/committee-select";
// import CommitteeChanger from "../secretary/resolutions/committee-change/committee-changer";

export default {
    name: "committee",
    components: {
        // CommitteeChanger,
        // CommitteeSelect,
        ResolutionCreation,
        // CreationResult,
        // CosponsorsSelect,
        PageFooter,
        // SponsorSelect
    },
    props: [],

    mixins: [],

    data: function () {
        return {
            title: '',
            sponsor: null,
            cosponsors: [],
            // waiver_requested: false,
            waiver: false,
             url: null
        }
    },

    asyncComputed: {
        committeeObjects : function (){
            return this.$store.getters.getCommittees;
        },

        committees : function (){
            if(!isReadyToRock(this.committeeObjects)) return [];

            let names = [];
            _.forEach(this.committeeObjects, (c) => {
               names.push(c.name);
            });
            names.sort();
            return names;
        }
    },

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
    },
    mounted() {
        window.console.log('committee', 'mounted', 97, 'beep');
        this.$store.dispatch('committeeStartup');
    }


}
</script>

<style scoped>
/*.top-spacer {*/
/*    margin-top: 20px;*/
/*}*/
</style>
