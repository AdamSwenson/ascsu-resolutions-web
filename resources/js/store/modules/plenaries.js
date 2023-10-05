import * as routes from "../../routes";
import {getById} from "../../utilities/object.utilities";


const state = {
    //things:
    plenaries: [],
    currentPlenaryId: null
};

const mutations = {

    addPlenary: (state, plenary) => {
        state.plenaries.push(plenary)
    },

    setCurrentPlenaryId: (state, plenaryId) => {
        state.currentPlenaryId = plenaryId;
    }
    /*
    *   addThing: (state, thing) => {
    *        state.things.push(thing);
    *    }
    */

};


const actions = {
    /*
    *    doThing({dispatch, commit, getters}, thingParam) {
    *        return new Promise(((resolve, reject) => {
    *        }));
    *    },
    */

    setCurrentPlenaryId({dispatch, commit}) {
        return new Promise(((resolve, reject) => {
            let pid = _.toInteger(window.plenaryId);
            commit('setCurrentPlenaryId', pid);
            return resolve();
        }));
    },

    loadPlenaries({dispatch, commit, getters}) {
        return new Promise(((resolve, reject) => {
            let url = routes.secretary.plenaries.loadAll();
            // let url = window.routeRoot + '/plenaries';
            return Vue.axios.get(url).then((response) => {
                _.forEach(response.data, (r) => {
                    commit('addPlenary', r)
                });
                return resolve();
            });

        }));
    }
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
    getPlenaries: (state) => {
        return state.plenaries;
    },

    getCurrentPlenary: (state) => {
        return getById(state.plenaries, state.currentPlenaryId);
    },

    getCurrentPlenaryId : (state) => {
        return state.currentPlenaryId;
    }

};

export default {
    actions,
    getters,
    mutations,
    state,
}
