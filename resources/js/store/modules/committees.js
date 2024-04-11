import * as routes from "../../routes";
import {getById, idify} from "../../utilities/object.utilities";
import {isReadyToRock} from "../../utilities/readiness.utilities";

const state = {
    committees: [],

    /**
     * When creating or editing a resolution, this is the
     * committee currently selected as the sponsor
     */
    selectedSponsor: null,

    /**
     * When creating or editing a resolution, these are the
     * committees currently selected as cosponsors
     */
    selectedCosponsors: []

};

const mutations = {
    /**
     * Adds a committee object to the store
     * @param state
     * @param committee
     */
    addCommittee: (state, committee) => {
        state.committees.push(committee)
    },

    /**
     * Changes the committee designated as sponsor
     * @param state
     * @param committee Committee object
     */
    updateSelectedSponsor: (state, committee) => {
        state.selectedSponsor = committee;
    },

    /**
     * Adds a committee object to the list of cosponsors
     * @param state
     * @param committee
     */
    addCosponsor: (state, committee) => {
        state.selectedCosponsors.push(committee);
        state.selectedCosponsors = _.uniq(state.selectedCosponsors);
    },

    /**
     * Removes the cosponsor object
     * @param state
     * @param committee
     */
    removeCosponsor: (state, committee) => {
        // _.remove(state.selectedCosponsors, function (c) {
        //     return c.id === committee.id;
        // });

        let idx = state.selectedCosponsors.indexOf(committee);
        state.selectedCosponsors.splice(idx, 1);
    },

    /**
     * Resets selected sponsor and cosponsor to null /empty
     * Used after making edits
     * @param state
     * @param committee
     */
    resetSelectedCommittees: (state, committee) => {
        state.selectedSponsor = null;
        state.selectedCosponsors = [];
    },

    resetSelectedSponsor: (state, committee) => {
        state.selectedSponsor = null;
    },

    resetSelectedCosponsors: (state, committee) => {
        state.selectedCosponsors = [];
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
    },


    /**
     * Asks the server to figure out which committees needs to be
     * updated and take care of it.
     * This is the main called method
     *
     * @param dispatch
     * @param commit
     * @param getters
     * @param resolution
     * @returns {Promise<unknown>}
     */
    updateResolutionCommittees({dispatch, commit, getters}, resolution) {
        return new Promise(((resolve, reject) => {
            let url = routes.committee.updateCommittees(resolution);

            let data = {
                sponsor : getters.getSelectedSponsor,
                cosponsors : getters.getSelectedCosponsors
            };

            Vue.axios.post(url, data).then((response) => {
                commit('resetSelectedCommittees');
                //dev Consider updating objects on client instead
                dispatch('forceReload');
                return resolve();
            });




            // //dev or just be lazy and do all?
            // if(resolution.sponsor.id !== getters.getSelectedSponsor.id){
            //     //we need to update the sponsor
            //
            // }
            //
            // // if()
            // dispatch('updateResolutionSponsor', resolution).then(() => {
            //     dispatch('updateResolutionCosponsors', resolution).then(() => {
            //         return resolve();
            //     });
            //
            // })

        }));

    },
    // /**
    //  * Updates the resolution's sponsor to use the sponsor
    //  * currently set in selectedSponsor
    //  * @param dispatch
    //  * @param commit
    //  * @param getters
    //  * @param resolution
    //  */
    // updateResolutionSponsor({dispatch, commit, getters}, resolution) {
    //     return new Promise(((resolve, reject) => {
    //
    //         //reset
    //         commit('resetSelectedSponsor');
    //         return resolve();
    //     }));
    //
    // },
    //
    // /**
    //  * Updates the resolution's cosponsors to use the committees currently
    //  * set in selectedCosponsors
    //  * @param dispatch
    //  * @param commit
    //  * @param getters
    //  * @param resolution
    //  */
    // updateResolutionCosponsors({dispatch, commit, getters}, resolution) {
    //     return new Promise(((resolve, reject) => {
    //
    //
    //         //reset
    //         commit('resetSelectedCosponsors');
    //         return resolve();
    //     }));
    // }

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
    },

    /**
     * Returns the currently selected sponsor
     * @param state
     * @returns {string}
     */
    getSelectedSponsor: (state) => {
        return state.selectedSponsor;
    },

    /**
     * Returns a list of currently selected cosponsors
     * @param state
     * @returns {[]}
     */
    getSelectedCosponsors: (state) => {
        return state.selectedCosponsors;
    }

};

export default {
    actions,
    getters,
    mutations,
    state,
}
