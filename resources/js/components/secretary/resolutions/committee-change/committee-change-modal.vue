<script>
import modalParent from "../../../parents/modal-parent";
import resolutionMixin from "../../../../mixins/resolutionMixin";

export default {
    name: "committee-change-modal",

    extends: modalParent,

    props: ['resolutionId'],

    mixins: [resolutionMixin],

    data: function () {
        return {

            modalTitle: "Update sponsors or cosponsors",
            buttonLabel: 'Update',

            styling: ' committee-change-modal ',
            // modalText: 'Probably not this text',
            modalSecondaryText: 'secondary text'
        }
    },

    asyncComputed: {
        modalText: function () {
            return "this one is #" + this.resolutionId;
        }
    },

    computed: {
        modalId: function () {
            return 'committeeChangeModal' + this.resolutionId;
        }
    },

    methods: {
        handleClick: function () {
            window.console.log('committee-change-modal', 'handleClick', 31, 'boop', this.resolution);
            //Ask the server to make the changes. Then reset selected committees
            this.$store.dispatch('updateResolutionCommittees', this.resolution);
        },

        handleCancel: function () {
            //Need to clear the selected committees
            window.console.log('committee-change-modal', 'handleCancel', 42, 'beep');
            this.$store.commit('resetSelectedCommittees');
        }
    }

}
</script>

<style scoped>

</style>
