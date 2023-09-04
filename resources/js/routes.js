const _ = require("lodash");


/**
 * Ensure that the base url ends with a '/'
 * as expected by all the route methods.
 *
 * If no routeRoot url is passed, it will use the
 * value stored on window
 *
 * @param url
 */
const normalizedRouteRoot = (url = null) => {
    if (_.isNull(url)) {
        url = window.routeRoot;
    }
    if (url[url.length] === '/') return url;

    return url + '/';
};

const idify = (ObjectOrId) =>{
// const idify = (ObjectOrId) =>{
    if(_.isNumber(ObjectOrId)) return ObjectOrId;
    // if (ObjectOrId instanceof Number) return ObjectOrId;

    return ObjectOrId.id;
};

/**
 * This holds all information about which
 * routing urls are used for what purposes.
 *
 */
module.exports = {

    committee : {

    },

    secretary : {
        agenda : {
         createAgenda : (plenary) => {
             plenary_id = idify(plenary);
             url = normalizedRouteRoot()
             url += 'secretary/agenda/'
             url += plenary_id;
             return url
         }
        },

        permissions : {
            getPermission: (resolution) => {
                resolution_id = idify(resolution);
                url = normalizedRouteRoot()
                url += 'secretary/permissions/one/'
                url += resolution_id;
                return url
                },

            lockAll : (plenary) => {
                plenary_id = idify(plenary);
                url = normalizedRouteRoot()
                url += 'secretary/permissions/all/lock/'
                url += plenary_id;
                return url
            },

            unlockAll : (plenary) => {
                plenary_id = idify(plenary);
                url = normalizedRouteRoot()
                url += 'secretary/permissions/all/unlock/'
                url += plenary_id;
                return url
            },

            lockOne : (resolution) => {
                resolution_id = idify(resolution);
                url = normalizedRouteRoot()
                url += 'secretary/permissions/one/lock/'
                url += resolution_id;
                return url
            },

            unlockOne : (resolution) => {
                resolution_id = idify(resolution);
                url = normalizedRouteRoot()
                url += 'secretary/permissions/one/unlock/'
                url += resolution_id;
                return url
            },

        },

        resolutions : {
            loadAll : () => {
                url = normalizedRouteRoot()
                url += 'resolutions'
                return url
            },

            enforceStyle : () => {
                url = normalizedRouteRoot()
                url += 'secretary/styling'
                return url
            }
        }

    }


};
