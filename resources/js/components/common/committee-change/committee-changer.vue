<template>
<span class="committee-changer ">
<committee-change-button :resolution-id="resolutionId"></committee-change-button>
<committee-change-modal :resolution-id="resolutionId">
    <div class="selectors">
        <committee-select type="sponsor"></committee-select>
        <committee-select type="cosponsor"></committee-select>
    </div>
</committee-change-modal>
</span>
</template>

<script>
import CommitteeChangeButton from "./committee-change-button";
import CommitteeChangeModal from "./committee-change-modal";
import CommitteeSelect from "./committee-select";

export default {
    name: "committee-changer",
    components: {CommitteeSelect, CommitteeChangeModal, CommitteeChangeButton},
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
