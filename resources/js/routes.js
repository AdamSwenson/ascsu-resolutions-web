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
    all : {
      loadCommittees: () => {
          let url = normalizedRouteRoot();
          url += 'committees/all';
          return url;
      }
    },

    committee: {
        updateCommittees : (resolution) => {
            let resolutionId = idify(resolution);
            let url = normalizedRouteRoot();
            url += 'committees/update/' + resolutionId;
            return url;
        }
    },

    secretary: {

        singleControl: {
            startPlenary : (plenary) => {
                let plenary_id = idify(plenary);
                let url = normalizedRouteRoot()
                url += 'secretary/plenary/'
                url += plenary_id;
                url += '/start'
                return url
            },

            stopPlenary : (plenary) => {
                let plenary_id = idify(plenary);
                let url = normalizedRouteRoot()
                url += 'secretary/plenary/'
                url += plenary_id;
                url += '/stop'
                return url
            }
        },

        agenda: {
            createAgenda: (plenary) => {
                let plenary_id = idify(plenary);
                let url = normalizedRouteRoot()
                url += 'secretary/agenda/'
                url += plenary_id;
                return url
            },

            lockAgenda: (plenary) => {
                let plenary_id = idify(plenary);
                let url = normalizedRouteRoot()
                url += 'agenda/lock/'
                url += plenary_id;
                return url
            },
            unlockAgenda: (plenary) => {
                let plenary_id = idify(plenary);
                let url = normalizedRouteRoot()
                url += 'agenda/unlock/'
                url += plenary_id;
                return url
            },
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

            enforceStyle: (plenary) => {
                let plenaryId = idify(plenary);
                let url = normalizedRouteRoot();
                url += 'secretary/styling/';
                url += plenaryId;
                return url
            },

            syncTitles: (plenary) => {
                let plenaryId = idify(plenary);
                let url = normalizedRouteRoot();
                url += 'secretary/sync/';
                url += plenaryId;
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
            },

            toggleWaiver : (resolution) => {
                let resolution_id = idify(resolution);
                let url = normalizedRouteRoot();
                url += 'resolution/waiver/toggle/';
                url += resolution_id;
                return url;
            }
        },


        working : {
            bulk : (sourcePlenary, destinationPlenary) => {
                let sourceId = idify(sourcePlenary);
                let destinationId = idify(destinationPlenary);
                let url = normalizedRouteRoot();
                url += 'resolution/working/bulk/';
                url += sourceId;
                url += '/';
                url += destinationId;
                return url;
            },

            single : (plenary, resolution) => {
                let plenary_id = idify(plenary);
                let resolution_id = idify(resolution);
                let url = normalizedRouteRoot();
                url += 'resolution/working/';
                url += plenary_id;
                url += '/'
                url += resolution_id
                return url;
            }
        },


    },

    resolutions : {
        setReadingType: (plenary, resolution) => {
            let plenary_id = idify(plenary);
            let resolution_id = idify(resolution);
            let url = normalizedRouteRoot();
            url += 'resolution/reading/';
            url += plenary_id + '/'
            url += resolution_id;
            return url;
        }

    }
};
