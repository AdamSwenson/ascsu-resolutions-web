/**
 *
 */
module.exports = {

    asyncComputed: {
        plenaryId : function(){
            return _.toInteger(window.plenaryId);
        },

        /**
         * Object of the current plenary
         * @returns {any}
         */
        plenary: function(){
            return JSON.parse(window.plenary);
        },

        /**
         * The display name of the currently selected plenary
         */
        plenaryName : function(){
            if(_.isNull(this.plenary)) return ''
            return this.plenary.plenaryName;
        },

        publicFolderUrl: function(){
            if(_.isNull(this.plenary)) return ''
            return this.plenary.publicUrl;
        },

        plenaryUrl : function(){
            if(_.isNull(this.plenary)) return ''
            return this.plenary.plenaryUrl;
        },

        resolutionListUrl : function(){
            if(_.isNull(this.plenary)) return ''
            return this.plenary.resolutionListUrl;
        }

    },

    computed: {},

    methods: {}

};
