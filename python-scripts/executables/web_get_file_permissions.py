import logging
import sys


sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

import json
from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.config.Configuration import Configuration


def main(resolution_id=None):
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:
        if resolution_id is None:
            resolution_id = int(sys.argv[1])

        dao = MySqlDao()
        resolution_repo = ResolutionRepository(dao)
        permission_repo = PermissionsRepository()

        resolution = resolution_repo.load_resolution(resolution_id)

        result = permission_repo.get_permission(resolution.document_id)
        result = json.dumps(result)
        sys.stdout.write(result)

        return result
    except Exception as e:
        logger.warning(e)


if __name__ == '__main__':
    main()
