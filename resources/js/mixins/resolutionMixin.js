/**
 *
 */
const {isReadyToRock} = require("../utilities/readiness.utilities");
module.exports = {

    asyncComputed: {
        isApproved: function () {
            if (!isReadyToRock(this.resolution)) return false;
            return this.resolution.status === 'approved';
        },

        isFailed: function () {
            if (!isReadyToRock(this.resolution)) return false;
            return this.resolution.status === 'failed';
        },

        isFirstReading: function () {
            if (!isReadyToRock(this.resolution)) return false;
            // return this.resolution.actionpivot.is_first_reading === 1;
            return this.resolution.readingType === 'first';
        },

        isActionItem: function () {
            if (!isReadyToRock(this.resolution)) return false;
            return this.resolution.readingType === 'action';
        },

        isWorking: function () {
            if (!isReadyToRock(this.resolution)) return false;
            // window.console.log('resolutionMixin', 'isWorking', 31, this.resolution);
            return this.resolution.readingType === 'working';
        },

        isWaiver: function () {
            if (!isReadyToRock(this.resolution)) return false;
            return this.resolution.readingType === 'waiver';
// return this.isFirstReading && this.resolution.pivot.is_waiver === 1;
        },

        resolution: function () {
            return this.$store.getters.getResolution(this.resolutionId);
        },

        // ============= Plenaries
        firstReadingPlenary: function () {
            if (!isReadyToRock(this.resolution)) return '';
            return this.resolution.firstReadingPlenary;
        },

        actionPlenaries: function () {
            if (!isReadyToRock(this.resolution)) return [];
            return this.resolution.actionPlenaries;
        },

        workingPlenaries: function(){
            if(!isReadyToRock(this.resolution)) return [];
            return this.resolution.workingPlenaries;
        },

        /**
         * Returns the name of the plenary in which it was a first reading
         * @returns {string|*}
         */
        firstReadingName: function () {
            if (!isReadyToRock(this.firstReadingPlenary)) return '';
            return this.firstReadingPlenary.plenaryName;
        },

        /**
         * Returns list of names of plenaries in which it was an action
         * item
         * @returns {*[]}
         */
        secondReadingNames: function () {
            if (!isReadyToRock(this.actionPlenaries)) return [];
            let n = [];
            _.forEach(this.actionPlenaries, (p) => {
                n.push(p.plenaryName)
            });
            return n;
        },

        /**
         * Returns list of names of plenaries in whose working drafts
         * folder it has been located
         * @returns {*[]}
         */
        workingPlenaryNames : function(){
            if (!isReadyToRock(this.workingPlenaries)) return [];
            let n = [];
            _.forEach(this.workingPlenaries, (p) => {
                n.push(p.plenaryName)
            });
            return n;
        },


        // ============= intrinsic properties
        title: function () {
            if (!isReadyToRock(this.resolution)) return '';
            return this.resolution.title;
        },

        resolutionNumber: function () {
            if (!isReadyToRock(this.resolution)) return '';
            return this.resolution.formattedNumber;
        },

        url: function () {
            if (!isReadyToRock(this.resolution)) return '';
            return this.resolution.url;
        },

        currentLocation: function(){
            if (!isReadyToRock(this.resolution)) return '';
            return this.resolution.currentLocation;
        },

        currentLocationUrl: function(){
            if (!isReadyToRock(this.resolution)) return '';
            return this.resolution.currentLocationUrl;
        }



    },

    computed: {},

    methods: {}

};
