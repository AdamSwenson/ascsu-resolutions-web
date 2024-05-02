<template>
<div class="cosponsors-select ">
<!--    <div class="card-header">-->
    <h4 class="text-light">Cosponsors</h4>
<!--    </div>-->
    <cosponsor-check v-for="c in committeeNames"
                     :committee="c"
                     :key="c"
                     v-on:cosponsor="handleCosponsor"></cosponsor-check>
<!--    <div class="form-check">-->
<!--        <input class="form-check-input" type="radio" name="cosponsors" id="exampleRadios1" value="option1" checked>-->
<!--        <label class="form-check-label" for="exampleRadios1">-->
<!--            Default radio-->
<!--        </label>-->
<!--    </div>-->
<!--    <div class="form-check">-->
<!--        <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios2" value="option2">-->
<!--        <label class="form-check-label" for="exampleRadios2">-->
<!--            Second default radio-->
<!--        </label>-->
<!--    </div>-->
<!--    <div class="form-check">-->
<!--        <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios3" value="option3" disabled>-->
<!--        <label class="form-check-label" for="exampleRadios3">-->
<!--            Disabled radio-->
<!--        </label>-->
<!--    </div>-->
    </div>
</template>

<script>
import CosponsorCheck from "./cosponsor-check";
import committeeMixin from "../../mixins/committeeMixin";

/**
 * @deprecated
 */
export default {
    name: "cosponsors-select",
    components: {CosponsorCheck},
    props: ['committees'],

    mixins: [committeeMixin],

    data: function () {
        return {
            // committees: [
            //     'Academic Affairs',
            //     'Academic Preparation EP',
            //     'Executive Committee',
            //     'Faculty Affairs',
            //     'Fiscal and Governmental Affairs',
            //     'Justice, Equity, Diversity, and Inclusion'
            // ]
        }
    },

    asyncComputed: {},

    computed: {},

    methods: {
        handleCosponsor : function(v){
            this.$emit('cosponsor', v);
        }
    }

}
</script>

<style scoped>

</style>
