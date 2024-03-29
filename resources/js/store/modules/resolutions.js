import * as routes from "../../routes";
import {getById, idify} from "../../utilities/object.utilities";
import {isReadyToRock} from "../../utilities/readiness.utilities";

const state = {
    resolutions: [],
    currentPlenaryResolutionIds: []
    //things: []
};

const mutations = {
    addResolution: (state, resolution) => {
        state.resolutions.push(resolution);
    },

    addCurrentResolutionId: (state, resolutionId) => {
        if(state.currentPlenaryResolutionIds.indexOf(resolutionId) === -1){
            state.currentPlenaryResolutionIds.push(resolutionId);
        }
    }
    /*
    *   addThing: (state, thing) => {
    *        state.things.push(thing);
    *    }
    */

};


const actions = {


    loadCurrentPlenaryResolutions({dispatch, commit, getters}) {
        return new Promise(((resolve, reject) => {
            let plenaryId = getters.getCurrentPlenaryId;
            let url = routes.secretary.resolutions.loadForPlenary(plenaryId);
            Vue.axios.get(url).then((response) => {
                _.forEach(response.data, (r) => {
                    commit('addCurrentResolutionId', r.id);
                });
                return resolve();
            });
        }));
    },


    loadAllResolutions({dispatch, commit, getters}) {
        return new Promise(((resolve, reject) => {
            let url = routes.secretary.resolutions.loadAll();
            Vue.axios.get(url).then((response) => {
                _.forEach(response.data, (r) => {
                    commit('addResolution', r);
                });
                return resolve();
            });
        }));
    },

    markResolutionApproved({dispatch, commit, getters}, resolution){
        let resolutionId = idify(resolution);
        let url = routes.secretary.resolutions.approvalStatus(resolutionId)

        window.console.log('set approvad', 'post', 63, url);
        let me = this;
        let data = {status : 'approved'};
        Vue.axios.post(url, data).then((response) => {
            //todo Actually update the object
            dispatch('forceReload');
            // me.approvalStatus = response.data.is_approved;
            // window.console.log('permissions', 'response', 126, response, me);
        });
    },

    markResolutionFailed({dispatch, commit, getters}, resolution){
        let resolutionId = idify(resolution);
        let url = routes.secretary.resolutions.approvalStatus(resolutionId)

        window.console.log('set failed', 'post', 63, url);
        let me = this;
        let data = {status : 'failed'};
        Vue.axios.post(url, data).then((response) => {
            //todo Actually update the object
            dispatch('forceReload');
            // me.approvalStatus = response.data.is_approved;
            // window.console.log('permissions', 'response', 126, response, me);
        });

    },

    markResolutionUnvoted({dispatch, commit, getters}, resolution){
        let resolutionId = idify(resolution);
        let url = routes.secretary.resolutions.approvalStatus(resolutionId)

        window.console.log('set unvoted', 'post', url);
        let me = this;
        let data = {status : null};
        Vue.axios.post(url, data).then((response) => {
            //todo Actually update the object
            dispatch('forceReload');
        });

    },


    initializeResolutions({dispatch, commit, getters}) {
        return new Promise(((resolve, reject) => {
            dispatch('loadAllResolutions').then(() => {
                dispatch('loadCurrentPlenaryResolutions').then(() => {
                    return resolve();
                });
            })

        }));

    },


    toggleIsWaiver({dispatch, commit, getters}, resolution) {
        return new Promise(((resolve, reject) => {
            let url = routes.secretary.resolutions.toggleWaiver(resolution)

            window.console.log('toggle waiver', 'post', url);
            let me = this;
            let data = {status : null};
            Vue.axios.post(url, data).then((response) => {
                //todo Actually update the object
                dispatch('forceReload');
            });

        }));

    },



    /*
    *    doThing({dispatch, commit, getters}, thingParam) {
    *        return new Promise(((resolve, reject) => {
    *        }));
    *    },
    */
};

/**
 *
 *    getThingViaId: (state) => (thingId) => {
 *        return state.things.filter(function (c) {
 *            return c.thing_id === thingId;
 *        })
 *    },
 *
 *
 *    getThing: (state, getters) => {}
 */
const getters = {
    getResolutions: (state) => {
        return state.resolutions;
    },

    getCurrentPlenaryResolutions: (state, getters) => {
        let rez = [];
        let resolutions = getters.getResolutions;
        _.forEach(state.currentPlenaryResolutionIds, (rid) => {
            let r = getById(resolutions, rid)
            if(isReadyToRock(r)){
                // window.console.log('resolutions', 'rid', 98, rid, r);
                rez.push(r);
            }

        })
        return rez;
    },

    getUnapprovedResolutions : (state, getters) => {
        let rez = [];
        let resolutions = getters.getResolutions;
        _.forEach(resolutions, (r) => {
            if(r.status !== 'approved'){
                rez.push(r);
            }

        })
        return rez;
    },

    getResolution : (state, getters) => (resolutionId) => {
        return getById(state.resolutions, resolutionId);
    }

};

export default {
    actions,
    getters,
    mutations,
    state,
}
