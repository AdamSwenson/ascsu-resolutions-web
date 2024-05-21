<template>
    <li class="nav-item committee-router-tab">
        <a class="nav-link text-light"
           v-bind:class="styling"
           v-bind:aria-current="ariaCurrent"
           aria-current="page"
           href="#"
           v-on:click="selectCommittee"
        >{{name}}</a>
    </li>

<!--<div class="committee-router-tab ">-->
<!--    <router-link-->
<!--        v-bind:to="path"-->
<!--        v-slot="{ href, route, navigate, isActive, isExactActive }"-->
<!--    >-->
<!--        <li class="nav-item mt-1"-->
<!--            :class="[isActive && 'router-link-active', isExactActive && 'router-link-exact-active']"-->
<!--        >-->
<!--            <a class="nav-link"-->
<!--               :class="[isActive && activeClass, isExactActive && activeClass]"-->
<!--               :href="href" @click="navigate">{{ label }}</a>-->
<!--        </li>-->
<!--    </router-link>-->

<!--    </div>-->
</template>

<script>
import {isReadyToRock} from "../../../utilities/readiness.utilities";

export default {
    name: "committee-router-tab",

    /**
     * Committee object
     */
    props: ['committee'],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {
        styling : function(){
            if(! isReadyToRock(this.selectedCommittee)) return ''
            if(! isReadyToRock(this.committee)) return ''
            if(this.committee.id === this.selectedCommittee.id) return "active"
        },

        ariaCurrent : function(){
            if(! isReadyToRock(this.selectedCommittee)) return ''
            if(! isReadyToRock(this.committee)) return ''

            if(this.committee.id === this.selectedCommittee.id) return "page"
        },

    },

    computed: {

            name: function () {
                return this.committee.name;
            },
            label: function () {
                this.committee.abbreviation
//                return this.route.label;
            },
            path: function () {
                return "/" . this.committee.abbreviation;
            },



    },

    methods: {
        selectCommittee : function(){
            window.console.log('committee-router-tab', 'selectCommittee', 81, this.committee);
            this.$store.commit('setCurrentCommittee', this.committee);
        }
    }

}
</script>

<style scoped>

</style>

