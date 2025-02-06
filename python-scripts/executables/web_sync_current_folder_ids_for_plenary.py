import logging
import sys


sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
from ResolutionManager.config.Configuration import Configuration

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.config.Templates import Templates


def main(plenary_id=None):
    """Updates the current folder location of all resolutions for the plenary
    Added in AR-139

    """
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:

        if plenary_id is None:
            plenary_id = int(sys.argv[1])

        dao = MySqlDao()

        file_repo = FileRepository()
        plenary_repo = PlenaryRepository(dao)
        resolution_repo = ResolutionRepository(dao)

        plenary = plenary_repo.load_plenary(plenary_id)
        resolutions = resolution_repo.load_all_resolutions_for_plenary(plenary)

        for r in resolutions:
            current_folder_id = file_repo.get_resolution_folder_id(r)
            resolution_repo.update_resolution_current_folder_id(r,
                                                                current_folder_id)

    except Exception as e:
        logger.warning(e)


if __name__ == '__main__':
    main()
