<script>
import modalButtonParent from "../../../parents/modal-button-parent";
import resolutionMixin from "../../../../mixins/resolutionMixin";

export default {
    name: "committee-change-button",
    extends: modalButtonParent,
    props: ['resolutionId'],

    mixins: [resolutionMixin],

    data: function () {
        return {
            label: 'Edit committtees',
            ariaDisabled: false,
            styling: ' btn-sm btn-outline-primary'
        }
    },

    asyncComputed: {},

    computed: {
        modalId: function () {
            return 'committeeChangeModal' + this.resolutionId;
        }
    },

    methods: {
        handleClick: function () {
            //when modal opens, we need to populate the
            //selected committees with the ones from the resolution
            this.$store.commit('updateSelectedSponsor', this.resolution.sponsor);
            _.forEach(this.resolution.cosponsors, (c) => {
                this.$store.commit('addCosponsor', c);
            });
        }
    }

}
</script>

<style scoped>

</style>
