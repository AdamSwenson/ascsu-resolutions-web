const {isReadyToRock} = require("../utilities/readiness.utilities");
/**
 * Common things for any use of committees
 */
module.exports = {

    asyncComputed: {
        /**
         * All objects representing committees
         * @returns {any}
         */
        committeeObjects: function () {
            return this.$store.getters.getCommittees;
        },

        /**
         * List of names of all committees
         * @returns {*[]}
         */
        committeeNames: function () {
            if (!isReadyToRock(this.committeeObjects)) return [];

            let names = [];
            _.forEach(this.committeeObjects, (c) => {
                names.push(c.name);
            });
            names.sort();
            return names;
        },

        selectedSponsor: {
            set: function (committee) {
                this.$store.commit('updateSelectedSponsor', committee);
            },
            get: function () {
                return this.$store.getters.getSelectedSponsor;
            },
        },

        selectedCosponsors: {
            set: function (committee) {
                this.$store.commit('addCosponsor', committee);

            },
            get: function () {
                return this.$store.getters.getSelectedCosponsors;
            },

        }
    },


};
