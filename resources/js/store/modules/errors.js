const state = {
    currentError : null
    //things: []
};

const mutations = {

    addError: (state, error) => {
    state.currentError = error;
    },
    resetError : (state) =>{ state.currentError = null;}
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

    showError({dispatch, commit, getters}, error){
        return new Promise(((resolve, reject) => {
            window.console.log('errors', 'error', 31, error);
            commit('addError', error);
            return resolve();
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

    getCurrentError : (state) => {
        return state.currentError;
    }
};

export default {
    actions,
    getters,
    mutations,
    state,
}
