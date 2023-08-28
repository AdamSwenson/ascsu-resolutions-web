<template>
    <div class="sponsor-select  ">
<!--<div class="card-header">-->
        <h4 class="text-light">Sponsoring committee</h4>
<!--</div>-->
<!--        <div class="card-body">-->
        <sponsor-check v-for="c in committees" :committee="c" :key="c" v-on:sponsor="handleSponsor"></sponsor-check>
<!--    </div>-->
    </div>

<!--        <label for="sponsor" class="form-label text-light">Sponsoring committee</label>-->
<!--        <select id="sponsor" class="form-select" aria-label="sponsoring committee" v-model="selected">-->
<!--            <option value="" selected disabled hidden>Select committee</option>-->
<!--            <option v-for="c in committees" :value="c">-->
<!--                {{ c }}-->
<!--            </option>-->
<!--        </select>-->
<!--    </div>-->

</template>

<script>
import SponsorCheck from "./sponsor-check";
export default {
    name: "sponsor-select",
    components: {SponsorCheck},
    props: ['committees'],

    mixins: [],

    data: function () {
        return {
            selected: '',
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

    methods: {handleSponsor: function(v){
        this.$emit('sponsor', v);
        }}

}
</script>

<style scoped>

</style>
