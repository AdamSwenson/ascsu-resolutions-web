<template>
    <div class="secretary ">

        <div class=" row top-spacer pt-5"></div>

        <div class="row pt-2">
            <div class="col-lg-4">
            </div>

            <div class="col-lg-6">
                <div class="mb-2">
                    <h2 class="text-light text-center">{{plenaryName}} Plenary</h2>
                </div>

                <div class=" mb-5">
                    <public-folder-creation :plenaryId="plenaryId"></public-folder-creation>

                </div>

                <div class=" mb-5">
                    <enforce-styling></enforce-styling>
                </div>


                <div class=" mb-5">
                    <create-agenda :plenaryId="plenaryId"></create-agenda>
                </div>


                <div class="mb-5">
                    <manager-permissions :plenaryId="plenaryId"></manager-permissions>
                </div>

                <div class="mb-5">
                    <select-plenary></select-plenary>
                </div>
                <create-plenaries></create-plenaries>


            </div>
            <div class="col-lg-4"></div>

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

export default {
    name: "secretary",
    components: {
        EnforceStyling,
        CreateAgenda, SelectPlenary, CreatePlenaries, ManagerPermissions, PublicFolderCreation, PageFooter},
    props: [],
    mixins: [plenaryMixin],


    data: function () {
        return {
            // plenaryId : 1,
            publicUrl : null
        }
    },

    asyncComputed: {

    },

    computed: {},

    methods: {

    }

}
</script>

<style scoped>
/*?*/

</style>
