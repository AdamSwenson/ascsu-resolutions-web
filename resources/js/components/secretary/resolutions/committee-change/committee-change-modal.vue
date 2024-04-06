<script>
import modalParent from "../../../parents/modal-parent";

export default {
    name: "committee-change-modal",

    extends: modalParent,

    props: ['resolutionId'],

    mixins: [],

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
modalText : function(){
    return "this one is #" + this.resolutionId;
}
    },

    computed: {
        modalId : function(){
            return 'committeeChangeModal' + this.resolutionId;
        }
    },

    methods: {
        handleClick: function () {
            window.console.log('committee-change-modal', 'handleClick', 31,);
        }
    }

}
</script>

<style scoped>

</style>
