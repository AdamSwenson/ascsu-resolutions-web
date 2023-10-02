const state = {
    isReady : false
};
const mutations = {
    toggleIsReady: (state) => {
        state.isReady = ! state.isReady;
    }
};
const getters = {
    getIsReady: (state) => {
        return state.isReady;
    }
};

const actions = {

    secretaryStartup({dispatch, commit, getters}){
        return new Promise(((resolve, reject)=>{
            dispatch('setCurrentPlenaryId').then(() => {
                dispatch('loadPlenaries');
                dispatch('loadAllResolutions').then(() => {
                    dispatch('loadCurrentPlenaryResolutions').then(() => {
                        commit('toggleIsReady');
                        return resolve();
                    });
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
