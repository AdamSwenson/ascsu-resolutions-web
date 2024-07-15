const state = {
    isReady: false
};
const mutations = {
    toggleIsReady: (state) => {
        state.isReady = !state.isReady;
    }
};
const getters = {
    getIsReady: (state) => {
        return state.isReady;
    }
};

const actions = {


    forceReload({dispatch, commit, getters}) {
        location.reload();
    },

    secretaryStartup({dispatch, commit, getters}) {
        return new Promise(((resolve, reject) => {
            dispatch('setCurrentPlenaryId').then(() => {
                dispatch('loadPlenaries');
                dispatch('loadCommittees');
                dispatch('loadAllResolutions').then(() => {
                    dispatch('loadCurrentPlenaryResolutions').then(() => {
                        commit('toggleIsReady');
                        return resolve();
                    });
                });
            });

        }));
    },

    committeeStartup({dispatch, commit, getters}) {
        return new Promise(((resolve, reject) => {
            return dispatch('setCurrentPlenaryId').then(() => {
                dispatch('loadPlenaries');
                dispatch('loadCommittees');
                // return dispatch('loadAllResolutions').then(() => {
                    dispatch('loadCurrentPlenaryResolutions').then(() => {
                    commit('toggleIsReady');
                    return resolve();
                });
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


export default {
    actions,
    state,
    getters,
    mutations
}
