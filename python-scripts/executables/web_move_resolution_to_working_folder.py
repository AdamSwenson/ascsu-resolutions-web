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


def main(plenary_id=None, resolution_id=None):
    """Moves the indicated resolution to the working drafts folder for
    the indicated plenary
    Added in AR-89
    """
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:

        if plenary_id is None:
            plenary_id = int(sys.argv[1])

        if resolution_id is None:
            resolution_id = int(sys.argv[2])

        dao = MySqlDao()

        file_repo = FileRepository()
        plenary_repo = PlenaryRepository(dao)
        resolution_repo = ResolutionRepository(dao)

        plenary = plenary_repo.load_plenary(plenary_id)
        resolution = resolution_repo.load_resolution(resolution_id)

        file_repo.move_file_to_folder(resolution.document_id, plenary.working_drafts_folder_id)

        return resolution

    except Exception as e:
        logger.warning(e)


if __name__ == '__main__':
    main()
