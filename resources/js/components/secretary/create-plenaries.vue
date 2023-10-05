<template>
<div class="create-plenaries card ">
        <h3 class="card-title text-light">Create plenary </h3>


    <div class="card-body">
        <label class="text-light" for="plenaryDate">Thursday of plenary</label>
        <input type="date" id="plenaryDate" v-model="thursdayDate">
    </div>


    <div class="card-body">
        <p class="card-text text-info">This will create a new plenary meeting with the appropriate folders in the drive</p>
        <working-spinner v-if="isWorking"></working-spinner>
        <button v-else
                class="btn btn-danger" v-on:click="handleCreateFolders">Create folders</button>
        </div>

    <div class="card-body " v-show="showUrl">
        <p class="card-text text-light">
            Link to main plenary folder:<br>
            <a v-bind:href="url"  target="_blank">{{ url }}</a>
        </p>
    </div>

</div>

</template>

<script>
import plenaryMixin from '../../mixins/plenaryMixin'
import WorkingSpinner from "../common/working-spinner";

export default {
    name: "create-plenaries",
    components: {WorkingSpinner},
    props: [],

    mixins: [plenaryMixin],

    data: function () {
        return {
            thursdayDate: null,
            url : null,
            isWorking : false
        }
    },

    asyncComputed: {
        showUrl : function(){
            return ! _.isNull(this.url);
        }
    },

    computed: {},

    methods: {
        handleCreateFolders : function(){
            window.console.log('committee', 'createPlenaries', 124, this.$data);
            let url = window.routeRoot + '/secretary/folders'
            let me = this;
            this.isWorking = true;
            let data = {'thursday_date' : this.thursdayDate};
            Vue.axios.post(url, data).then((response) => {
                window.console.log('committee', 'response', 126, response);
                me.url = response.data.plenaryUrl;
                me.isWorking = false;
            });

        },
    }

}
</script>

<style scoped>

</style>
