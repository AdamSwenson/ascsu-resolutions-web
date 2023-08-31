<template>
<div class="resolution-permission-item ">
    <li class="list-group-item">

        <a href="#" class="btn btn-sm "
           v-bind:class="styling"
           v-on:click="toggleEditing"
        >{{buttonLabel}}</a> {{number}} {{ title }}
    </li>
    </div>
</template>

<script>
import * as routes from "../../../routes";

export default {
    name: "resolution-permission-item",

    props: ['resolutionId', 'title', 'number'],

    mixins: [],

    data: function () {
        return {
            isEditable : false
        }
    },

    asyncComputed: {
        buttonLabel : function (){
            if(this.isEditable){
                return 'Lock editing'
            }
            return 'Allow editing';

        } ,

        styling : function(){
            if(this.isEditable){
                return 'btn-primary'
            }
            return 'btn-outline-primary';
        }
    },

    computed: {},

    methods: {

        getPermission : function(){
            let url = routes.secretary.permissions.getPermission(this.resolutionId)

            window.console.log('permissions', 'get', 124, url);
            let me = this;
            Vue.axios.get(url).then((response) => {
                /*Will receive the following:
                {
                    "id": "anyoneWithLink",
                    "type": "anyone",
                    "kind": "drive#permission",
                    "role": "reader",
                    "allowFileDiscovery": false
                }*/
                if(response.data.role === 'reader'){
                    me.isEditable = false;
                }else if(response.data.role === 'writer'){
                    me.isEditable = true;
                }
                window.console.log('permissions', 'response', 126, response);
            });
        },

        lockEditing: function (){
            let url = routes.secretary.permissions.lockOne(this.resolutionId)

            window.console.log('permissions', 'get', 124, url);
            let me = this;
            Vue.axios.post(url).then((response) => {
                //todo check for success
                me.isEditable = false;

                window.console.log('permissions', 'response', 126, response);
            });
        },

        unlockEditing : function(){
            let url = routes.secretary.permissions.unlockOne(this.resolutionId)

            window.console.log('permissions', 'get', 124, url);
            let me = this;
            Vue.axios.post(url).then((response) => {
                //todo check for success
                me.isEditable = true;

                window.console.log('permissions', 'response', 126, response);
            });
        },

        toggleEditing : function() {
            if(this.isEditable){
                this.lockEditing();
            }else{
                this.unlockEditing();
            }
        }
    },
    mounted() {
        this.getPermission();
    }

}
</script>

<style scoped>

</style>
