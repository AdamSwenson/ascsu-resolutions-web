import * as routes from "../../routes";
import {getById} from "../../utilities/object.utilities";
import {isReadyToRock} from "../../utilities/readiness.utilities";


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
                _.forEach(response.data, (d) => {
                    commit('addPlenary', d)
                });
                return resolve(response);
            });

        }));
    },

    lockAgenda({dispatch, commit, getters}, plenary) {
        return new Promise(((resolve, reject) => {
            let url = routes.secretary.agenda.lockAgenda(plenary);
            return Vue.axios.post(url).then((response) => {
                return resolve(response);
            });

        }));
    },

    unlockAgenda({dispatch, commit, getters}, plenary) {
        return new Promise(((resolve, reject) => {
            let url = routes.secretary.agenda.unlockAgenda(plenary);
            return Vue.axios.post(url).then((response) => {
                return resolve(response);
            });

        }));
    },
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
    /**
     * Returns only plenaries for the academic year
     */
    getAcademicYearPlenaries: (state, getters) => {
        let plenary = getters.getCurrentPlenary;
        if (!isReadyToRock(plenary)) return [];

        let plenaryDate = new Date(plenary.thursday_date);
        //NB, January is 0
        let month = plenaryDate.getMonth();
        let year = plenaryDate.getFullYear();
        // window.console.log('plenaries', '', 91, month, year);
        let out = [];
        _.forEach(state.plenaries, (p) => {
            //dev we actually do want the current plenary to be an option
            // if (p.id !== plenary.id) {
            let date = new Date(p.thursday_date);

            if (month >= 7) {
                //we are in the fall semester, so return the next spring also
                if ((date.getFullYear() === year && date.getMonth() >= 7) ||
                    (date.getFullYear() === year + 1 && date.getMonth() < 7)) {
                    out.push(p);
                }

            } else {
                //we are in spring so return previous fall
                if ((date.getFullYear() === year && date.getMonth() < 7) ||
                    (date.getFullYear() === year - 1 && date.getMonth() >= 7)) {
                    out.push(p);
                    // window.console.log('plenaries', 'c', 105, date.getFullYear() - 1);
                }

            }
            // }
        });

        return out;

    },


    getPlenaries: (state) => {
        return state.plenaries;
    },

    getCurrentPlenary: (state) => {
        return getById(state.plenaries, state.currentPlenaryId);
    },

    getCurrentPlenaryId: (state) => {
        return state.currentPlenaryId;
    }

};

export default {
    actions,
    getters,
    mutations,
    state,
}
