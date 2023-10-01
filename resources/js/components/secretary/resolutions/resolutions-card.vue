<template>
<div class="resolution-card card">
    <h3 class="card-title text-light">Manage individual resolutions</h3>

    <div class="card-body">
        <resolution-item-card :resolution-id="r.id"
                         :title="r.title"
                         :number="r.formattedNumber"
                         :is-approved="r.is_approved"
                         :first-reading-plenary="r.firstReadingPlenary"
                         :action-plenaries="r.actionPlenaries"
                              :waiver="r.waiver"
                         :key="r.resolutionId"
                         v-for="r in resolutions"
        ></resolution-item-card>

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
import ResolutionItem from "./resolution-item";

import {isReadyToRock} from "../../../utilities/readiness.utilities";
import ResolutionItemCard from "./resolution-item-card";

export default {
    name: "resolutions-card",

    components: {ResolutionItemCard, ResolutionItem},
    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {
            rez: []
        }
    },

    asyncComputed: {
        resolutions: {
            get: function () {
                // let r = this.$store.getters.getCurrentPlenaryResolutions;
                // if(!isReadyToRock(r)) return [];
                // return r;
                // // if (!isReadyToRock(this.rez) || this.rez.length === 0) return []
                // return this.rez;
            },
            // watch: ['rez']
        }
    },

    watch: {
        // 'plenaryId': function(){this.loadResolutions();}
    },

    computed: {},

    methods: {
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
        if(isReadyToRock(this.plenaryId)){
            // this.loadResolutions();
        }
    }

}
</script>

<style scoped>

</style>
