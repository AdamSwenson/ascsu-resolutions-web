import * as routes from "../../routes";

const state = {

};
const mutations = {

};
const getters = {

};

const actions = {

    startPlenary({dispatch, commit, getters}, plenary){
        return new Promise(((resolve, reject) => {
            let url = routes.secretary.singleControl.startPlenary(plenary);
            return Vue.axios.post(url).then((response) => {
                return resolve();
            });
        }));
    },

    stopPlenary({dispatch, commit, getters}, plenary){
        return new Promise(((resolve, reject) => {
            let url = routes.secretary.singleControl.stopPlenary(plenary);
            return Vue.axios.post(url).then((response) => {
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


export default {
    actions,
    state,
    getters,
    mutations
}
