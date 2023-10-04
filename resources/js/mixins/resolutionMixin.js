/**
 *
 */
const {isReadyToRock} = require("../utilities/readiness.utilities");
module.exports = {

    asyncComputed: {
        isApproved : function(){
            if(! isReadyToRock(this.resolution)) return false;
            return this.resolution.status === 'approved';
        },

        isFailed : function(){
            if(! isReadyToRock(this.resolution)) return false;
            return this.resolution.status === 'failed';
        },

        isFirstReading : function(){
            if(! isReadyToRock(this.resolution)) return false;
            // return this.resolution.actionpivot.is_first_reading === 1;
            return this.resolution.readingType === 'first';
        },

        isActionItem: function(){
            if(! isReadyToRock(this.resolution)) return false;
            return this.resolution.readingType === 'action';
        },

        isWaiver: function(){
            if(! isReadyToRock(this.resolution)) return false;
            return this.resolution.readingType === 'waiver';
// return this.isFirstReading && this.resolution.pivot.is_waiver === 1;
        },

        resolution : function(){
            return this.$store.getters.getResolution(this.resolutionId);
        },
    },

    computed: {},

    methods: {}

};
