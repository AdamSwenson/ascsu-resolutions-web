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

        resolution : function(){
            return this.$store.getters.getResolution(this.resolutionId);
        }
    },

    computed: {},

    methods: {}

};
