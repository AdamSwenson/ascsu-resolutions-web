
<script>
import modalButtonParent from "../../../parents/modal-button-parent";

export default {
    name: "committee-change-button",
extends: modalButtonParent,
    props: ['resolutionId'],

    mixins: [],

    data: function () {
        return {
            label : 'Edit committtees',
            ariaDisabled: false,
            styling: ' btn-sm btn-primary'

        }
    },

    asyncComputed: {

    },

    computed: {
        modalId : function(){
            return 'committeeChangeModal' + this.resolutionId;
        }
    },

    methods: {}

}
</script>

<style scoped>

</style>
