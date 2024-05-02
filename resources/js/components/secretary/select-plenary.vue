<template>
<div class="select-plenary card">

    <h3 class="card-header text-light">Select current plenary</h3>

    <ul class="list-group list-group-flush">
        <plenary-list-item :plenary="p" v-for="p in plenaries" :key="p.id"></plenary-list-item>
<!--        <li class="list-group-item" v-for="p in plenaries">{{p.thursday_date}}</li>-->

    </ul>



    </div>
</template>

<script>
import PlenaryListItem from "./plenary-list-item";
import {isReadyToRock} from "../../utilities/readiness.utilities";
export default {
    name: "select-plenary",
    components: {PlenaryListItem},
    props: [],

    mixins: [],

    data: function () {
        return {
            _plenaries : []
        }
    },

    asyncComputed: {
        plenaries : function(){
            //
            let p = this.$store.getters.getPlenaries;
            p = _.sortBy(p, function(o){ return o.thursday_date });
            if(isReadyToRock(p)) return p;
            return []
        }
    },

    computed: {},

    methods: {

        setPlenaryAsCurrent : function(plenaryId){

        },
        // loadPlenaries : function(){
        //     let me = this;
        //     let url = window.routeRoot + '/plenaries';
        //     return Vue.axios.get(url).then((response) => {
        //         me._plenaries = response.data;
        //         return response.data;
        //     });
        // }

    },

    // mounted() {this.loadPlenaries();
    // }

}
</script>

<style scoped>

</style>
