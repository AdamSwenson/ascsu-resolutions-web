import logging
import sys


sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.config.Configuration import Configuration
from ResolutionManager.Repositories.SyncRepository import SyncRepository


def main(plenary_id=None):
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:
        if plenary_id is None:
            plenary_id = int(sys.argv[1])

        dao = MySqlDao()
        plenary_repo = PlenaryRepository(dao)
        sync_repo = SyncRepository(dao)

        plenary = plenary_repo.load_plenary(plenary_id)

        sync_repo.sync(plenary)


    except Exception as e:
        logger.error(e)


if __name__ == '__main__':
    main()
