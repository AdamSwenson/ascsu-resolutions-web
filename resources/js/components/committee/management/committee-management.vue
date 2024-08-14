<template>
    <div class="committee-management card">
        <div class="card-body">
            <!--    tabs -->
            <ul class="nav nav-tabs">
                <committee-router-tab
                    v-for="c in committeeObjects"
                    :key="c.abbreviation"
                    :committee="c"
                ></committee-router-tab>


                <!--            <li class="nav-item" v-for="c in committeeObjects">-->
                <!--                <a class="nav-link active" aria-current="page"-->
                <!--                   href="#">Active</a>-->
                <!--            </li>-->
                <!--            <li class="nav-item">-->
                <!--                <a class="nav-link" href="#">Link</a>-->
                <!--            </li>-->
                <!--            <li class="nav-item">-->
                <!--                <a class="nav-link" href="#">Link</a>-->
                <!--            </li>-->
                <!--            <li class="nav-item">-->
                <!--                <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>-->
                <!--            </li>-->
            </ul>
        </div>

        <div class="card-body">
            <committee-resolutions-card :committee="selectedCommittee"></committee-resolutions-card>
        </div>
        <!--    </div>-->


        <!--    body-->

    </div>
</template>

<script>
import plenaryMixin from "../../../mixins/plenaryMixin";
import committeeMixin from "../../../mixins/committeeMixin";
import CommitteeRouterTab from "./committee-router-tab";
import CommitteeResolutionsCard from "./committee-resolutions-card";

/**
 * This is the root page for committee resolution managment
 *
 * Created in AR-91
 */
export default {
    name: "committee-management",
    components: {CommitteeResolutionsCard, CommitteeRouterTab},
    props: [],

    mixins: [plenaryMixin, committeeMixin],

    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {}

}
</script>

<style scoped>

</style>
