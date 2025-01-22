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


def main(source_plenary_id=None, destination_plenary_id=None):
    """Moves resolutions in the working folder and non waiver first readings
    to the working folder of the indicated plenary
    Added in AR-136
    """
    config = Configuration()
    logger = logging.getLogger(__name__)

    dao = MySqlDao()

    file_repo = FileRepository()
    plenary_repo = PlenaryRepository(dao)
    resolution_repo = ResolutionRepository(dao)

    try:

        if source_plenary_id is None:
            source_plenary_id = int(sys.argv[1])

        if destination_plenary_id is None:
            destination_plenary_id = int(sys.argv[2])

        source_plenary = plenary_repo.load_plenary(source_plenary_id)
        destination_plenary = plenary_repo.load_plenary(destination_plenary_id)
        print(destination_plenary.id)

        resolutions = resolution_repo.load_all_resolutions_for_plenary(source_plenary)

        in_source_working = [r for r in resolutions if r.reading_type == 'working']

        # dev Eventually won't need to filter out on waiver since reading type first and waiver are exclusive
        in_source_first = [r for r in resolutions if r.reading_type == 'first' and r.waiver is not True]
        # print(in_source_first)

        to_move = in_source_working + in_source_first
        print(f"this many {len(to_move)}")
        print(to_move)

        for resolution in to_move:
            file_repo.move_file_to_folder(resolution.document_id, destination_plenary.working_drafts_folder_id)
            print(resolution.id, destination_plenary.working_drafts_folder_id)
            # Set resolution status to working
            # Doing this here rather than in php so that don't have to reload in php
            resolution_repo.set_as_working_item(destination_plenary, resolution)

    except Exception as e:
        print(e)
        logger.warning(e)


if __name__ == '__main__':
    main()
