<template>

    <div class="cosponsor-check mb-1">
        <input type="checkbox"
               class="btn-check"
               v-bind:id="inputId"
               autocomplete="off"
        v-model="checked"
        >
        <label class="btn btn-outline-primary" v-bind:for="inputId">{{ committee }}</label>

        <!--    <div class="form-check text-light">-->
        <!--        <input class="form-check-input"-->
        <!--               type="checkbox"-->
        <!--               v-bind:name="inputId"-->
        <!--               v-bind:value="committee"-->
        <!--               v-bind:id="inputId">-->
        <!--        <label class="form-check-label text-light"-->
        <!--               v-bind:for="inputId">-->
        <!--            {{committee}}-->
        <!--        </label>-->
        <!--    </div>-->
    </div>
    <!--    <div class="form-check">-->
    <!--        <input class="form-check-input"-->
    <!--               type="radio"-->
    <!--               name="cosponsors"-->
    <!--               v-bind:id="inputId"-->
    <!--               value="" >-->
    <!--        <label class="form-check-label" for="exampleRadios1">-->
    <!--            Default radio-->
    <!--        </label>-->
    <!--    </div>-->
    <!--    </div>-->
</template>

<script>
import committeeMixin from "../../mixins/committeeMixin";

export default {
    name: "cosponsor-check",

    props: ['committee'],

    mixins: [committeeMixin],

    data: function () {
        return {
            checked: false
        }
    },

    watch: {
        checked : function(){
            this.$emit('cosponsor', this.committee);
        }
    },

    asyncComputed: {

        label : function(){

        }
    },

    computed: {
        inputId: function () {
            return _.camelCase(this.committee) + 'Cosponsor';
        }
    },

    methods: {

    }

}
</script>

<style scoped>

</style>
