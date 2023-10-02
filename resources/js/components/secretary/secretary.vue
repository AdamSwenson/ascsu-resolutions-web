<template>
    <div class="secretary p-5">


        <div class=" row top-spacer pt-5"></div>

        <div class="mb-2">
            <h1 class="text-light text-center">{{ plenaryName }} Plenary</h1>
        </div>

        <div class="row  row-cols-1 row-cols-md-3 g-4 mb-5 mt-5">
            <div class="col">
                <public-folder-creation :plenaryId="plenaryId"></public-folder-creation>
            </div>
            <div class="col">
                <enforce-styling></enforce-styling>
            </div>
            <div class="col">
                <sync-titles :plenary-id="plenaryId"></sync-titles>
            </div>
            <div class="col">
                <create-agenda :plenaryId="plenaryId"></create-agenda>
            </div>
            <div class="col">
                <manager-permissions :plenaryId="plenaryId"></manager-permissions>
            </div>
        </div>

        <div class="resolutions">
            <div class="mb-4">
                <h2 class="text-light text-center">Resolutions</h2>
            </div>

            <div class="row mb-5">
                <div class="col-lg-3"></div>

                <div class="col-lg-6">
                    <div class="">
                        <resolutions-card></resolutions-card>
                    </div>
                </div>

                <div class="col-lg-3"></div>
            </div>
        </div>

        <div class="plenaries">
            <div class="mb-4">
                <h2 class="text-light text-center">Plenaries</h2>
            </div>

            <div class="row">
                <div class="col-lg-3"></div>

                <div class="col-lg-6">

                    <div class="mb-5">
                        <select-plenary></select-plenary>
                    </div>

                    <div class="mb-5">
                        <create-plenaries></create-plenaries>
                    </div>
                </div>

                <div class="col-lg-3"></div>
            </div>

        </div>

        <page-footer></page-footer>
    </div>

</template>

<script>
import PageFooter from "../layout/page-footer";
import PublicFolderCreation from "./public-folder-creation";
import ManagerPermissions from "./resolutions/manager-permissions";
import CreatePlenaries from "./create-plenaries";
import plenaryMixin from "../../mixins/plenaryMixin";
import SelectPlenary from "./select-plenary";
import CreateAgenda from "./create-agenda";
import EnforceStyling from "./enforce-styling";
import SyncTitles from "./sync-titles";
import ResolutionsCard from "./resolutions/resolutions-card";

export default {
    name: "secretary",
    components: {
        ResolutionsCard,
        SyncTitles,
        EnforceStyling,
        CreateAgenda, SelectPlenary, CreatePlenaries, ManagerPermissions, PublicFolderCreation, PageFooter
    },
    props: [],
    mixins: [plenaryMixin],


    data: function () {
        return {
            // plenaryId : 1,
            publicUrl: null
        }
    },

    asyncComputed: {},

    computed: {},

    methods: {},
    mounted() {
        window.console.log('secretary', 'mounted', 97, 'beep');
        this.$store.dispatch('secretaryStartup');
    }

}
</script>

<style scoped>
/*?*/

</style>
