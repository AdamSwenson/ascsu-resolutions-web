<template>
    <div class="committee py-2">

        <committee-navbar
            v-on:open-creation="handleOpenCreation"
            v-on:open-management="handleOpenManagement"
            :shownPage="shownPage"
        ></committee-navbar>

        <resolution-creation v-if="shownPage === 'creation'"></resolution-creation>

        <committee-management v-if="shownPage === 'management'"></committee-management>

        <page-footer></page-footer>

    </div>

</template>
,
<script>
import PageFooter from "../layout/page-footer";
import ResolutionCreation from "./resolution-creation";
import CommitteeManagement from "./management/committee-management";
import CommitteeNavbar from "./committee-navbar";
// import {isReadyToRock} from "../../utilities/readiness.utilities";

export default {
    name: "committee",
    components: {
        CommitteeNavbar,
        CommitteeManagement,
        ResolutionCreation,
        PageFooter,
    },
    props: [],

    mixins: [],

    data: function () {
        return {
            shownPage: 'creation'
        }
    },

    asyncComputed: {},

    computed: {},

    methods: {
        handleOpenCreation: function () {
            window.console.log('committee', 'handleOpenCreation', 52,);
            this.shownPage = 'creation';
        },
        handleOpenManagement: function () {
            window.console.log('committee', 'handleOpenManagement', 56,);
            this.shownPage = 'management';
        }
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
