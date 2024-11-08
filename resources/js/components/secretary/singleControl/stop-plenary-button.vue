<template>
    <div class="stop-plenary-button ">

        <working-spinner v-if="isWorking"></working-spinner>
        <button v-else
                class="btn btn-danger" v-on:click="handleClick">Stop plenary
        </button>


    </div>
</template>

<script>
import WorkingSpinner from "../../common/working-spinner";
import plenaryMixin from "../../../mixins/plenaryMixin";

export default {
    name: "stop-plenary-button",
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
            this.$store.dispatch('stopPlenary', this.plenary).then(() => {
                me.isWorking = false;
            });
        }

    }
}

</script>

<style scoped>

</style>
