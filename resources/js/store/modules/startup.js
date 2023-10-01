const state = {};
const mutations = {};
const getters = {};

const actions = {

    secretaryStartup({dispatch, commit, getters}){
        return new Promise(((resolve, reject)=>{
            dispatch('setCurrentPlenaryId').then(() => {
                dispatch('loadPlenaries');
                dispatch('loadCurrentPlenaryResolutions')
                dispatch('loadAllResolutions');
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
