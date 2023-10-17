// import './bootstrap.js';

/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries.
 */
import Vue from "vue";
window.Vue = Vue;

require('./bootstrap');



/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
/**
 //  * We'll load the axios HTTP library which allows us to easily issue requests
 //  * to our Laravel back-end. This library automatically handles sending the
 //  * CSRF token as a header based on the value of the "XSRF" token cookie.
 //  */

import axios from 'axios';
window.axios = axios;
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
// window.axios.defaults.baseURL = routeRoot;

import VueAxios from 'vue-axios'
//This wrapper bind axios to Vue or this if you're using single file component.
Vue.use(VueAxios, axios)


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ROUTER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
// import VueRouter from 'vue-router'
// Vue.use( VueRouter );

// Define some routes
// Each route should map to a component. The "component" can
// either be an actual component constructor created via
// Vue.extend(), or just a component options object.
// import { routes } from './routes.client';

// Create the router instance and pass the `routes` option
// const router = new VueRouter( {
//     routes, // short for routes: routes
//     base: window.routeRoot
// } );



/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ STORE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
import Vuex from 'vuex'
Vue.use(Vuex)
import Store from './store';


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OTHER VUE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
import AsyncComputed from 'vue-async-computed'
Vue.use(AsyncComputed)

import Multiselect from 'vue-multiselect'
// register globally
Vue.component('multiselect', Multiselect)


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ GLOBAL REG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
/**
 * The following block of code may be used to automatically register your
 * Vue components. It will recursively scan this directory for the Vue
 * components and automatically register them with their "basename".
 *
 * Eg. ./components/ExampleComponent.vue -> <example-component></example-component>
 */


// const files = require.context('./', true, /\.vue$/i)
// files.keys().map(key => Vue.component(key.split('/').pop().split('.')[0], files(key).default))


// Top level components
Vue.component('secretary', require('./components/secretary/secretary.vue').default);
Vue.component('commitee', require('./components/committee/committee.vue').default);

// Vue.component('home-page-footer', require('./components/layout/page-footer.vue').default);

// Vue.component('page-navbar', require('./components/layout/navbar').default);

/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

const app = new Vue({
    el: '#app',
    store: Store,
    // router : router
});
