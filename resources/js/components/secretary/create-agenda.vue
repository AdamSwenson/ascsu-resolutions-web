<template>
    <div class="create-agenda card ">
        <h3 class="card-title text-light">Resolution list </h3>

        <div class="card-body">
            <div class="row">

            <div class="col update-list" v-if="showUpdate">
                <working-spinner v-if="isUpdateWorking"></working-spinner>

                <button v-else
                        class="btn btn-primary"
                        v-on:click="handleCreateAgenda"
                >Update resolution list
                </button>
            </div>

            <div class="col lock-list">
                <working-spinner v-if="isLockWorking"></working-spinner>

                <button class="btn ms-3"
                        v-if="!isLockWorking"
                        v-bind:class="lockButtonStyling"
                        v-on:click="handleAgendaLock"
                >{{ lockButtonText }}
                </button>

                <p class="card-text text-light">Locking the list prevents it from being automatically overwritten</p>
            </div>
            </div>
        </div>

        <div class="card-body " v-show="showUrl">
            <p class="card-text text-light">
                Link to list of resolutions:<br>
                <a v-bind:href="resolutionListUrl" target="_blank">{{ resolutionListUrl }}</a>
            </p>
        </div>


    </div>
</template>

<script>
import plenaryMixin from "../../mixins/plenaryMixin";
import * as routes from "../../routes";
import WorkingSpinner from "../common/working-spinner";
import PlenaryMixin from "../../mixins/plenaryMixin";
import {isReadyToRock} from "../../utilities/readiness.utilities";

export default {
    name: "create-agenda",
    components: {WorkingSpinner},

    props: [],

    mixins: [PlenaryMixin],


    data: function () {
        return {
            isUpdateWorking: false,
            isLockWorking: false
        }
    },
    asyncComputed: {
        showUrl: function () {
            return !_.isNull(this.resolutionListUrl);
        },

        showUpdate: function(){
            if (!isReadyToRock(this.plenary)) return true;

            if(this.plenary.is_agenda_locked === true) return false;

            return true;
        },

        lockButtonText: function () {
            if (!isReadyToRock(this.plenary)) return '';

            if (this.plenary.is_agenda_locked === true) return 'Unlock resolution list'

            return 'Lock resolution list';
        },

        lockButtonStyling: function () {
            if (!isReadyToRock(this.plenary)) return '';

            if (this.plenary.is_agenda_locked === true) return 'btn-outline-primary'

            return 'btn-primary';
        }
    },

    computed: {},

    methods: {
        handleCreateAgenda: function () {
            window.console.log('secretary', 'createAgenda');
            let url = routes.secretary.agenda.createAgenda(this.plenaryId);
            let me = this;
            this.isUpdateWorking = true;
            Vue.axios.post(url,).then((response) => {
                window.console.log('secretary', 'response', 126, response);
                me.isWorking = false;
                // me.url = response.data.agendaUrl;
            });

        },

        handleAgendaLock: function () {
            this.isLockWorking = true;
            if (this.plenary.is_agenda_locked === true) {
                this.unlockAgenda();
            } else {
                this.lockAgenda();
            }
        },

        lockAgenda: function () {
            let me = this;
            this.$store.dispatch('lockAgenda', this.plenary).then((response) => {
                me.plenary.is_agenda_locked = true;
                me.isLockWorking = false;
            });
        },

        unlockAgenda: function () {
            let me = this;
            this.$store.dispatch('unlockAgenda', this.plenary).then((response) => {
                me.plenary.is_agenda_locked = false;
                me.isLockWorking = false;
            });
        }
    }

}
</script>

<style scoped>

</style>
