<template>
    <div class="plenary-list-item ">

        <li class="list-group-item">
            <a href="#" class="btn btn-sm "
               v-bind:class="styling"
               v-on:click="setAsCurrent"
            >Current</a> {{ plenaryName }}
        </li>

    </div>
</template>

<script>
import {isReadyToRock} from "../../utilities/readiness.utilities";

export default {
    name: "plenary-list-item",

    props: ['plenary'],

    mixins: [],

    data: function () {
        return {}
    },

    asyncComputed: {
        date: function () {
            if (!isReadyToRock(this.plenary)) return ''
            // return new Date(this.plenary.thursday_date)
        },

        plenaryName: function () {
            if (!isReadyToRock(this.plenary)) return ''
            return this.plenary.plenaryName;
        },

        plenaryId: function () {
            if (!isReadyToRock(this.plenary)) return ''

            return this.plenary.id;
        },

        isCurrent: function () {
            if (!isReadyToRock(this.plenary)) return false

            return this.plenary.is_current;
        },
        year: function () {


        },

        styling: function () {
            if (this.isCurrent) {
                return 'btn-primary';
            } else {
                return 'btn-outline-primary';
            }
        }
    },


    computed: {},

    methods: {
        setAsCurrent: function () {
            let url = window.routeRoot + '/plenary/current/' + this.plenaryId;
            Vue.axios.post(url).then((response) => {
                location.reload();
            });


        }
    }

}
</script>

<style scoped>

</style>
