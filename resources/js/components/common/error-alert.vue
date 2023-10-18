<template>
    <div class="error-alert alert alert-danger d-flex align-items-center"
         role="alert"
         v-if="showError"
    >
        <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Danger:">
            <use xlink:href="#exclamation-triangle-fill"/>
        </svg>
        <div>
            {{ errorMessage }}
        </div>
    </div>
</template>

<script>
import {isReadyToRock} from "../../utilities/readiness.utilities";

export default {
    name: "error-alert",

    props: [],

    mixins: [],

    data: function () {
        return {
            defaultMessage: 'Something has gone wrong. Please try again.'
        }
    },

    asyncComputed: {
        showError: function () {
            return isReadyToRock(this.currentError);
        },

        currentError: function () {
            return this.$store.getters.getCurrentError;
        },

        errorMessage: function () {
            if (!this.showError || !isReadyToRock(this.currentError)) return this.defaultMessage;

            return this.currentError.message;
        }

    },

    computed: {},

    methods: {}

}
</script>

<style scoped>

</style>
