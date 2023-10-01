import * as routes from "../../routes";
import {getById} from "../../../../public/js/app";

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
        state.currentPlenaryResolutionIds.push(resolutionId);
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

    // initializeResolutions({dispatch, commit, getters}) {
    //     return new Promise(((resolve, reject) => {
    //         dispatch('loadAllResolutions').then(() => {
    //             dispatch('loadCurrentPlenaryResolutions').then(() => {
    //                 return resolve();
    //             });
    //         })
    //
    //     }));
    //
    // },


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
        _.forEach(state.currentPlenaryResolutionIds, (rid) => {
            rez.push(getById(state.resolutions, rid));
        })
        return rez;
    }

};

export default {
    actions,
    getters,
    mutations,
    state,
}
