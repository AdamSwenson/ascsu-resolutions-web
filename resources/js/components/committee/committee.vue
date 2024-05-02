<template>
    <div class="committee py-2">

        <resolution-creation></resolution-creation>

        <page-footer></page-footer>

    </div>

</template>

<script>
import PageFooter from "../layout/page-footer";
import ResolutionCreation from "./resolution-creation";
// import {isReadyToRock} from "../../utilities/readiness.utilities";

export default {
    name: "committee",
    components: {
        ResolutionCreation,
        PageFooter,
    },
    props: [],

    mixins: [],

    data: function () {
        return {
        }
    },

    asyncComputed: {
    },

    computed: {
    },

    methods: {
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
