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

const idify = (ObjectOrId) => {
// const idify = (ObjectOrId) =>{
    if (_.isNumber(ObjectOrId)) return ObjectOrId;
    // if (ObjectOrId instanceof Number) return ObjectOrId;

    return ObjectOrId.id;
};

/**
 * This holds all information about which
 * routing urls are used for what purposes.
 *
 */
module.exports = {

    committee: {},

    secretary: {
        agenda: {
            createAgenda: (plenary) => {
                let plenary_id = idify(plenary);
                let url = normalizedRouteRoot()
                url += 'secretary/agenda/'
                url += plenary_id;
                return url
            }
        },

        permissions: {
            getPermission: (resolution) => {
                let resolution_id = idify(resolution);
                let url = normalizedRouteRoot()
                url += 'secretary/permissions/one/'
                url += resolution_id;
                return url
            },

            lockAll: (plenary) => {
                let plenary_id = idify(plenary);
                let url = normalizedRouteRoot()
                url += 'secretary/permissions/all/lock/'
                url += plenary_id;
                return url
            },

            unlockAll: (plenary) => {
                let plenary_id = idify(plenary);
                let url = normalizedRouteRoot()
                url += 'secretary/permissions/all/unlock/'
                url += plenary_id;
                return url
            },

            lockOne: (resolution) => {
                let resolution_id = idify(resolution);
                let url = normalizedRouteRoot()
                url += 'secretary/permissions/one/lock/'
                url += resolution_id;
                return url
            },

            unlockOne: (resolution) => {
                let resolution_id = idify(resolution);
                let url = normalizedRouteRoot()
                url += 'secretary/permissions/one/unlock/'
                url += resolution_id;
                return url
            },

        },

        plenaries: {
            loadAll : () => {
            let url = normalizedRouteRoot();
            url += 'plenaries';
            return url;
            }
        },

        resolutions: {
            loadAll: () => {
                let url = normalizedRouteRoot()
                url += 'resolutions'
                return url
            },

            loadForPlenary : (plenary) => {
            let plenaryId = idify(plenary);
            let url = normalizedRouteRoot();
            url += 'plenary/resolutions/';
            url += plenaryId;
            return url;
            },

            enforceStyle: () => {
                let url = normalizedRouteRoot()
                url += 'secretary/styling'
                return url
            },

            syncTitles: () => {
                let url = normalizedRouteRoot();
                url += 'secretary/sync';
                return url;
            },

            approvalStatus : (resolution) => {
                let resolution_id = idify(resolution);
                let url = normalizedRouteRoot();
                url += 'resolution/approval/';
                url += resolution_id;
                return url;

            },

            setAction : (plenary, resolution) => {
                let plenary_id = idify(plenary);
                let resolution_id = idify(resolution);
                let url = normalizedRouteRoot();
                url += 'resolution/action/';
                url += plenary_id + '/'
                url += resolution_id;
                return url;
            }
        }

    }


};
