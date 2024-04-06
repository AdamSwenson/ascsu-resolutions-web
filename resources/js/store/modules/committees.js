import * as routes from "../../routes";
import {getById, idify} from "../../utilities/object.utilities";
import {isReadyToRock} from "../../utilities/readiness.utilities";

const state = {
    committees: []

};

const mutations = {
    /**
     * Adds a committee object to the store
     * @param state
     * @param committee
     */
    addCommittee: (state, committee) => {
        state.committees.push(committee)
    }

};


const actions = {

    loadCommittees({dispatch, commit, getters}) {
        window.console.log('committees', 'loadCommittees', 26);
        return new Promise(((resolve, reject) => {
            let url = routes.all.loadCommittees();
            window.console.log('committees', 'url', 29, url);
            Vue.axios.get(url).then((response) => {
                window.console.log('committees', 'response', 31, response);
                _.forEach(response.data, (c) => {
                    commit('addCommittee', c);
                });
                return resolve();
            });
        }));
    }
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
    getCommittees: (state) => {
        return state.committees;
    }
};

export default {
    actions,
    getters,
    mutations,
    state,
}
