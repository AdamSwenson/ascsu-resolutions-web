window._ = require('lodash');

/**
 * First we will load all of this project's JavaScript dependencies which
 * includes Vue and other libraries.
 */
import Vue from "vue";

require('./bootstrap');

window.Vue = Vue;


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ API ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
/**
 //  * We'll load the axios HTTP library which allows us to easily issue requests
 //  * to our Laravel back-end. This library automatically handles sending the
 //  * CSRF token as a header based on the value of the "XSRF" token cookie.
 //  */

import axios from 'axios';
window.axios = axios;

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

//import axios from 'axios'
import VueAxios from 'vue-axios'

//window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
//
// window.axios.defaults.baseURL = routeRoot;
//
// // This wrapper bind axios to Vue or this if you're using single file component.
Vue.use(VueAxios, axios)


/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ROUTER ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
import VueRouter from 'vue-router'
Vue.use( VueRouter );

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
// import Vuex from 'vuex'
// Vue.use(Vuex)
// import store from './store';


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

// Vue.component('example-component', require('./components/deprecated/ExampleComponent.vue').default);

// Top level components
// Vue.component('location-task', require('./components/deprecated/location-task').default);
Vue.component('secretary', require('./components/secretary/secretary.vue').default);
Vue.component('commitee', require('./components/committee/committee.vue').default);
// Vue.component('page-navbar', require('./components/layout/navbar').default);
/**
 * Next, we will create a fresh Vue application instance and attach it to
 * the page. Then, you may begin adding components to this application
 * or customize the JavaScript scaffolding to fit your unique needs.
 */

const app = new Vue({
    el: '#app',
    // store: store,
    // router : router
});

//
// /**
//  * We'll load the axios HTTP library which allows us to easily issue requests
//  * to our Laravel back-end. This library automatically handles sending the
//  * CSRF token as a header based on the value of the "XSRF" token cookie.
//  */
//
// import axios from 'axios';
// window.axios = axios;
//
// window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
//
// /**
//  * Echo exposes an expressive API for subscribing to channels and listening
//  * for events that are broadcast by Laravel. Echo and event broadcasting
//  * allows your team to easily build robust real-time web applications.
//  */
//
// // import Echo from 'laravel-echo';
//
// // import Pusher from 'pusher-js';
// // window.Pusher = Pusher;
//
// // window.Echo = new Echo({
// //     broadcaster: 'pusher',
// //     key: import.meta.env.VITE_PUSHER_APP_KEY,
// //     cluster: import.meta.env.VITE_PUSHER_APP_CLUSTER ?? 'mt1',
// //     wsHost: import.meta.env.VITE_PUSHER_HOST ? import.meta.env.VITE_PUSHER_HOST : `ws-${import.meta.env.VITE_PUSHER_APP_CLUSTER}.pusher.com`,
// //     wsPort: import.meta.env.VITE_PUSHER_PORT ?? 80,
// //     wssPort: import.meta.env.VITE_PUSHER_PORT ?? 443,
// //     forceTLS: (import.meta.env.VITE_PUSHER_SCHEME ?? 'https') === 'https',
// //     enabledTransports: ['ws', 'wss'],
// // });
