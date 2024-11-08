<template>
    <div class="start-plenary-button ">


        <working-spinner v-if="isWorking"></working-spinner>
        <button v-else
                class="btn btn-success" v-on:click="handleClick">Start plenary
        </button>


    </div>
</template>

<script>
import WorkingSpinner from "../../common/working-spinner";
import plenaryMixin from "../../../mixins/plenaryMixin";

export default {
    name: "start-plenary-button",
    components: {WorkingSpinner},
    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {
            isWorking: false
        }
    },

    asyncComputed: {},

    computed: {},

    methods: {
        handleClick: function () {
            this.isWorking = true;
            let me = this;
            this.$store.dispatch('startPlenary', this.plenary).then(() => {
                me.isWorking = false;
            });
        }

    }

}
</script>

<style scoped>

</style>
