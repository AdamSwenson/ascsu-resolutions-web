<template>
<span class="committee-changer ">
<committee-change-button :resolution-id="resolutionId"></committee-change-button>
<committee-change-modal :resolution-id="resolutionId">
    <p>beep</p>
</committee-change-modal>
</span>
</template>

<script>
import CommitteeChangeButton from "./committee-change-button";
import CommitteeChangeModal from "./committee-change-modal";
export default {
    name: "committee-changer",
    components: {CommitteeChangeModal, CommitteeChangeButton},
    props: ['resolutionId'],

    mixins: [],

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
