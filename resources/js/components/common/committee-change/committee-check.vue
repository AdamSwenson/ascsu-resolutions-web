<template>
    <div class="committee-check mb-1">

<!--        <input type="checkbox"-->
<!--               class="btn-check"-->
<!--               v-bind:id="inputId"-->
<!--               autocomplete="off"-->
<!--               v-model="isSelected"-->
<!--               v-on:click="handleClick"-->
<!--        >-->
<!--        <label class="btn btn-outline-primary"-->
<!--               v-bind:for="inputId">{{ label }}</label>-->


        <button class="btn "
                v-bind:class="styling"
                v-on:click="handleClick"
        >{{label}}</button>

    </div>


</template>

<script>
import committeeMixin from "../../../mixins/committeeMixin";
import {isReadyToRock} from "../../../utilities/readiness.utilities";


/**
 * Button for selecting or de selecting a committee.
 *
 * dev Not happy about the very similar colors for hover and selected buttons, but
 * using it as a check makes it hard to update state
 *
 */
export default {
    name: "committee-check",

    props: ['committee', 'type'],

    mixins: [committeeMixin],

    data: function () {
        return {
            unselectedStyle: 'btn-outline-primary',
            selectedStyle: 'btn-primary',

            // checked: false
        }
    },

    // watch: {
    //     isSelected: function () {
    //         this.$emit('cosponsor', this.committee);
    //     }
    // },

    asyncComputed: {
        inputId: function () {
            return _.camelCase(this.committee.name) + this.type;
        },

        isSelected: {
            get: function () {
                switch (this.type) {
                    case 'sponsor':
                        return this.isSponsor;
                        break;
                    case 'cosponsor':
                        return this.isCosponsor;
                        break;
                }
            }
        },


        isSponsor: function () {
            if(!isReadyToRock(this.selectedSponsor)) return false;
            return this.selectedSponsor.id === this.committee.id;
        },

        isCosponsor: function () {
            if(!isReadyToRock(this.selectedCosponsors) || !isReadyToRock(this.committee)) return false;
            let me = this;
            let v = _.find(this.selectedCosponsors, function(c){
                return c.id === me.committee.id;
            });

            return ! _.isUndefined(v);
        },

        label : function(){
            return this.committee.name;
        },

        styling : function(){
            if(this.isSelected) return this.selectedStyle;
            return this.unselectedStyle;
        }
    },

    computed: {

    },

    methods: {
        handleClick: function () {
            switch (this.type) {
                case 'sponsor':
                    this.toggleSponsor();
                    break;
                case 'cosponsor':
                    this.toggleCosponsor();
                    break;
            }
        },

        toggleCosponsor: function () {
            if (this.isCosponsor) {
                //The committee has been deselected
                this.$store.commit('removeCosponsor', this.committee);
            } else {
                //the committee has been selected
                this.$store.commit('addCosponsor', this.committee);
            }
        },

        toggleSponsor: function () {
            this.$store.commit('updateSelectedSponsor', this.committee);

        }
    }

}
</script>

<style scoped lang="scss">
.btn-outline-primary {
    //$btn-hover-bg-shade-amount:       1%;
    //$btn-hover-bg-tint-amount:        1%;
    //$btn-hover-border-shade-amount:   2%;
    //$btn-hover-border-tint-amount:    1%;
}
</style>
