<template>
    <div class="manager-permissions card ">
        <h3 class="card-title text-light">Bulk manage permissions</h3>
        <div class="card-body">
            <toggle-all-resolution-permissions></toggle-all-resolution-permissions>
        </div>

        <!--        <h3 class="card-title text-light">Manage individual permissions</h3>-->
        <!--        <div class="card-body">-->


        <!--            <ul class="list-group list-group-flush">-->
        <!--                <resolution-item :resolution-id="r.id"-->
        <!--                                 :title="r.title"-->
        <!--                                 :number="r.formattedNumber"-->
        <!--                                 :is-approved="r.is_approved"-->
        <!--                                 :key="r.resolutionId"-->
        <!--                                 v-for="r in resolutions"></resolution-item>-->
        <!--            </ul>-->
        <!--        </div>-->

    </div>
</template>

<script>
import plenaryMixin from "../../../mixins/plenaryMixin";
import ToggleAllResolutionPermissions from "./toggle-all-resolution-permissions";
import ResolutionPermissionButton from "./resolution-permission-button";
import ResolutionItem from "./resolution-item";
import * as routes from "../../../routes";
import {isReadyToRock} from "../../../utilities/readiness.utilities";

export default {
    name: "manager-permissions",
    components: {ResolutionItem, ResolutionPermissionButton, ToggleAllResolutionPermissions},
    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {
            rez: []
        }
    },

    asyncComputed: {
        resolutions: {
            get: function () {
                if (!isReadyToRock(this.rez) || this.rez.length === 0) return []
                return this.rez;
                // return [
                //
                //     {resolutionId : 1, title : 'test'}
                // ]
            },
            watch: ['rez']
        }
    },

    computed: {},

    methods: {
        handleToggleWritable: function () {
            window.console.log('manager-permissions', 'handleToggleWritable', 29,);
        },

        loadResolutions: function () {
            //todo Need some way to restrict these to active ones

            let url = routes.secretary.resolutions.loadAll();

            window.console.log('resolutions', 'get', 124, url);
            let me = this;
            Vue.axios.get(url).then((response) => {
                me.rez = response.data;
            });

        }

    }, mounted() {
        this.loadResolutions()
    }

}
</script>

<style scoped>

</style>
