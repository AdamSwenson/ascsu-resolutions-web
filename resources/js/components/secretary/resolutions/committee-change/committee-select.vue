<template>
    <div class="committee-select ">
        <h4 class="">{{ heading }}</h4>

        <committee-check v-for="c in committeeObjects"
                         :committee="c"
                         :key="c.id"
                         :type="type"
        ></committee-check>

    </div>
</template>

<script>
import committeeMixin from "../../../../mixins/committeeMixin";
import CommitteeCheck from "./committee-check";

export default {
    name: "committee-select",

    components: {CommitteeCheck},
    /**
     * type should be either:
     *      sponsor
     *      cosponsor
     */
    props: ['type'],

    mixins: [committeeMixin],

    data: function () {
        return {
        }
    },

    asyncComputed: {},

    computed: {
        heading: function () {
            switch (this.type) {
                case 'sponsor':
                    return "Sponsor";
                    break;
                case 'cosponsor':
                    return "Cosponsors";
                    break;
            }
        }
    },

    methods: {
        handleCosponsor: function (v) {
            // this.$emit('cosponsor', v);
        }
    }

}
</script>

<style scoped>

</style>
