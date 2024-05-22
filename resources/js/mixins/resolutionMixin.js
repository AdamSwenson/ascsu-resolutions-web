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

        isWorking : function(){
            if(! isReadyToRock(this.resolution)) return false;
            return this.resolution.readingType === 'working';
        },

        isWaiver: function(){
            if(! isReadyToRock(this.resolution)) return false;
            return this.resolution.readingType === 'waiver';
// return this.isFirstReading && this.resolution.pivot.is_waiver === 1;
        },

        resolution : function(){
            return this.$store.getters.getResolution(this.resolutionId);
        },

        // ============= Plenaries
        firstReadingPlenary : function(){
            if(! isReadyToRock(this.resolution)) return '';
            return this.resolution.firstReadingPlenary;
        },

        actionPlenaries : function(){
            if(! isReadyToRock(this.resolution)) return [];
            return this.resolution.actionPlenaries;
        },


        // ============= intrinsic properties
        title : function(){
            if(! isReadyToRock(this.resolution)) return '';
            return this.resolution.title;
        },

        resolutionNumber : function(){
            if(! isReadyToRock(this.resolution)) return '';
            return this.resolution.formattedNumber;
        }



    },

    computed: {},

    methods: {}

};
