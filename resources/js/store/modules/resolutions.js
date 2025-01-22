import * as routes from "../../routes";
import {getById, idify} from "../../utilities/object.utilities";
import {isReadyToRock} from "../../utilities/readiness.utilities";
// import {deepMerge} from "vue";

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
        if (state.currentPlenaryResolutionIds.indexOf(resolutionId) === -1) {
            state.currentPlenaryResolutionIds.push(resolutionId);
        }
    },

    updateResolution: (state, resolution) => {
        let idx = state.resolutions.findIndex((o) => {
            return o.id === resolution.id;
        });
        Vue.set(state.resolutions, idx, resolution);
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
                    commit('addResolution', r);

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

    /**
     * Sets the resolution as approved
     * @param dispatch
     * @param commit
     * @param getters
     * @param resolution
     */
    markResolutionApproved({dispatch, commit, getters}, resolution) {
        let resolutionId = idify(resolution);
        let url = routes.secretary.resolutions.approvalStatus(resolutionId)

        window.console.log('set approvad', 'post', 63, url);
        let me = this;
        let data = {status: 'approved'};
        Vue.axios.post(url, data).then((response) => {
            //todo Actually update the object
            dispatch('forceReload');
            // me.approvalStatus = response.data.is_approved;
            // window.console.log('permissions', 'response', 126, response, me);
        });
    },

    markResolutionFailed({dispatch, commit, getters}, resolution) {
        let resolutionId = idify(resolution);
        let url = routes.secretary.resolutions.approvalStatus(resolutionId)

        window.console.log('set failed', 'post', 63, url);
        let me = this;
        let data = {status: 'failed'};
        Vue.axios.post(url, data).then((response) => {
            //todo Actually update the object
            dispatch('forceReload');
            // me.approvalStatus = response.data.is_approved;
            // window.console.log('permissions', 'response', 126, response, me);
        });

    },

    markResolutionUnvoted({dispatch, commit, getters}, resolution) {
        let resolutionId = idify(resolution);
        let url = routes.secretary.resolutions.approvalStatus(resolutionId)

        window.console.log('set unvoted', 'post', url);
        let me = this;
        let data = {status: null};
        Vue.axios.post(url, data).then((response) => {
            //todo Actually update the object
            dispatch('forceReload');
        });

    },

    moveResolutionsBetweenPlenaries({dispatch, commit, getters}, payload) {
        let {sourcePlenary, destinationPlenary} = payload;
        return new Promise(((resolve, reject) => {
            window.console.log('resolutions', 'action', 124,sourcePlenary, destinationPlenary );
            let url = routes.secretary.working.bulk(sourcePlenary, destinationPlenary);
            return Vue.axios.post(url).then((response) => {
                window.console.log('resolutions', 'response', 126, response);
            return resolve();
            })
        }));

    },


    initializeResolutions({dispatch, commit, getters}) {
        return new Promise(((resolve, reject) => {
            dispatch('loadAllResolutions').then(() => {
                dispatch('loadCurrentPlenaryResolutions').then(() => {
                    return resolve();
                });
            })

        }));

    },


    /**
     * @deprecated As of AR-92
     * @param dispatch
     * @param commit
     * @param getters
     * @param resolution
     * @returns {Promise<unknown>}
     */
    toggleIsWaiver({dispatch, commit, getters}, resolution) {
        return new Promise(((resolve, reject) => {
            let url = routes.secretary.resolutions.toggleWaiver(resolution)

            window.console.log('toggle waiver', 'post', url);
            let me = this;
            let data = {status: null};
            Vue.axios.post(url, data).then((response) => {
                //todo Actually update the object
                dispatch('forceReload');
            });

        }));

    },

    /**
     * Marks the resolution as a first reading and requests
     * to move it to the corresponding folder
     * Added in AR-92
     * @param dispatch
     * @param commit
     * @param getters
     * @param resolution
     * @returns {Promise<unknown>}
     */
    setFirstReading({dispatch, commit, getters}, resolution) {

        return new Promise(((resolve, reject) => {
            let plenaryId = getters.getCurrentPlenaryId;
            let resolutionId = idify(resolution);
            let me = this;
            let data = {readingType: 'first'};
            let url = routes.resolutions.setReadingType(plenaryId, resolution);
            return Vue.axios.post(url, data)
                .then((response) => {
                    window.console.log('resolutions', 'first reading', 168, response);
                    commit('updateResolution', response.data);
                    return resolve();
                }).catch(function (error) {
                    // error handling
                    if (error.response) {
                        me.$store.dispatch('showError', error.response.data);
                    }
                    return reject();
                });
        }));
    },

    /**
     * Marks the resolution as a first reading waiver  and
     * requests to move it to the corresponding folder
     * NEW VERSION
     * Added in AR-92
     * @param dispatch
     * @param commit
     * @param getters
     * @param resolution
     * @returns {Promise<unknown>}
     */
    setWaiver({dispatch, commit, getters}, resolution) {

        return new Promise(((resolve, reject) => {
            let plenaryId = getters.getCurrentPlenaryId;
            let resolutionId = idify(resolution);
            let me = this;
            let data = {readingType: 'waiver'};
            let url = routes.resolutions.setReadingType(plenaryId, resolution);
            return Vue.axios.post(url, data)
                .then((response) => {
                    window.console.log('resolutions', 'waiver', 168, response);
                    commit('updateResolution', response.data);
                    return resolve();
                }).catch(function (error) {
                    // error handling
                    if (error.response) {
                        me.$store.dispatch('showError', error.response.data);
                    }
                    return reject();
                });
        }));
    },

    /**
     * Marks the resolution as a working draft and
     * requests to move it to the corresponding folder
     * Added in AR-92
     * @param dispatch
     * @param commit
     * @param getters
     * @param resolution
     * @returns {Promise<unknown>}
     */
    setWorkingDraft({dispatch, commit, getters}, resolution) {

        return new Promise(((resolve, reject) => {
            let plenaryId = getters.getCurrentPlenaryId;
            let resolutionId = idify(resolution);
            let me = this;
            let data = {readingType: 'working'};
            let url = routes.resolutions.setReadingType(plenaryId, resolution);
            return Vue.axios.post(url, data)
                .then((response) => {
                    window.console.log('resolutions', 'working', 168, response);
                    commit('updateResolution', response.data);
                    return resolve();
                }).catch(function (error) {
                    // error handling
                    if (error.response) {
                        me.$store.dispatch('showError', error.response.data);
                    }
                    return reject();
                });

        }));
    },

    /**
     * Marks the resolution as an action item and
     * requests to move it to the corresponding folder
     * Added in AR-92
     * @param dispatch
     * @param commit
     * @param getters
     * @param resolution
     * @returns {Promise<unknown>}
     */
    setActionItem({dispatch, commit, getters}, resolution) {
        return new Promise(((resolve, reject) => {
            let plenaryId = getters.getCurrentPlenaryId;
            let resolutionId = idify(resolution);
            let me = this;
            let data = {readingType: 'action'};
            let url = routes.resolutions.setReadingType(plenaryId, resolution);
            return Vue.axios.post(url, data)
                .then((response) => {
                    window.console.log('resolutions', 'action', 240, response);
                    commit('updateResolution', response.data);
                    return resolve();
                }).catch(function (error) {
                    // error handling
                    if (error.response) {
                        me.$store.dispatch('showError', error.response.data);
                    }
                    return reject();
                });

        }));
    },

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
        let resolutions = getters.getResolutions;
        _.forEach(state.currentPlenaryResolutionIds, (rid) => {
            let r = getById(resolutions, rid)
            if (isReadyToRock(r)) {
                // window.console.log('resolutions', 'rid', 98, rid, r);
                rez.push(r);
            }

        })
        return rez;
    },

    /**
     * Returns the unapproved resolutions for the committee
     * @param state
     * @param getters
     * @returns {(function(*))|*}
     */
    getCommitteeResolutions: (state, getters) => (committee) => {
        let committeeId = idify(committee);
        let rez = [];
        _.forEach(getters.getUnapprovedResolutions, (r) => {
            if (!_.isNull(r.sponsor) && r.sponsor.id === committeeId) {
                rez.push(r);
            }
        })
        return rez;
    },

    getUnapprovedResolutions: (state, getters) => {
        let rez = [];
        let resolutions = getters.getResolutions;
        _.forEach(resolutions, (r) => {
            if (r.status !== 'approved') {
                rez.push(r);
            }

        })
        return rez;
    },

    getResolution: (state, getters) => (resolutionId) => {
        return getById(state.resolutions, resolutionId);
    }

};

export default {
    actions,
    getters,
    mutations,
    state,
}
