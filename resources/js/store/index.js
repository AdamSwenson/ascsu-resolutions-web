/**
 * Created by adam on 2020-07-13.
 */


import Vue from 'vue'
import Vuex from 'vuex'

//global stuff
import * as actions from './actions'
import * as getters from './getters';
import * as mutations from './mutations'
import * as state from './state'

//modules
import committees from "./modules/committees";
import errors from "./modules/errors";
import plenaries from "./modules/plenaries";
import resolutions from "./modules/resolutions";
import startup from "./modules/startup";
import singleControl from "./modules/singleControl";

Vue.use(Vuex);

/**
 * This subscribes the api package which
 * handles data exchange with the server
 * to mutations in the store.
 */
// import apiPlugin from '../api/apiPlugin';
// import websocketPlugin from '../api/websocketPlugin';


// const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({

    // strict: debug, //letting check determine whether to turn on or off. should be off for production to avoid performance hit

    /**
     * From instances and components where store has been
     * injected, actions are called
     * like so: store.dispatch( 'string-action-name' )
     */
    actions,
    getters,
    mutations,
    state,

    plugins: [], //[ apiPlugin, websocketPlugin ],

    modules: {
        committees,
        errors,
        plenaries,
        resolutions,
        singleControl,
        startup
    }

    // plugins: debug ? [createLogger()] : []
});
