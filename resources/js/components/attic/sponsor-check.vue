<template>
    <div class="sponsor-check mb-1 ">
        <input type="radio"
               class="btn-check"
               name="sponsor"
               v-bind:id="inputId"
               autocomplete="off"
        v-model="checked"
        >
        <label class="btn btn-outline-primary"
               v-bind:for="inputId"
        >{{ committee }}</label>
    </div>
</template>

<script>

/**
 * @deprecated
 */
export default {
    name: "sponsor-check",

    props: ['committee'],

    mixins: [],

    data: function () {
        return {
            checked : false
        }
    },

    watch: {
      checked : function(){
          window.console.log('sponsor-check', 'checked', 32,);
          this.$emit('sponsor', this.committee);
      }
    },
    asyncComputed: {},

    computed: {
        inputId: function () {
            return _.camelCase(this.committee)  + 'Sponsor';
        }
    },

    methods: {
        handleClick : function(){

        }
    }

}
</script>

<style scoped>

</style>
