<template>
    <div class="manager-permissions card ">
        <h3 class="card-title text-light">Manage permissions</h3>
        <div class="card-body">
            <button class="btn btn-primary">Allow editing</button>
            <button class="btn btn-primary">Lock editing</button>
        </div>
    </div>
</template>

<script>
import plenaryMixin from "../../mixins/plenaryMixin";

export default {
    name: "manager-permissions",

    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {}
    },

    asyncComputed: {},

    computed: {},

    methods: {
        handleToggleWritable : function(){
            window.console.log('manager-permissions', 'handleToggleWritable', 29,);
        },

    }

}
</script>

<style scoped>

</style>
