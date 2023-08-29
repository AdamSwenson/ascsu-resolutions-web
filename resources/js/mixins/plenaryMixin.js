/**
 *
 */
module.exports = {

    asyncComputed: {
        plenaryId : function(){
            return _.toInteger(window.plenaryId);
        },

        plenary: function(){
            return JSON.parse(window.plenary);
        },
        plenaryName : function(){
            if(_.isNull(this.plenary)) return ''
            return this.plenary.plenaryName;
        }
    },

    computed: {},

    methods: {}

};
