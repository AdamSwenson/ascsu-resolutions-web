import logging
import sys
sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.Repositories.FileRepository import FileRepository
# import ResolutionManager.environment as env
from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
from ResolutionManager.config.Configuration import Configuration
from ResolutionManager.config.Templates import Templates


def main(plenary_id=None):
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:
        if plenary_id is None:
            plenary_id = int(sys.argv[1])

        config = Configuration()
        dao = MySqlDao()
        plenary_repo = PlenaryRepository(dao)
        plenary = plenary_repo.load_plenary(plenary_id)
        permissions_repo = PermissionsRepository()
        file_repo = FileRepository()

        # todo Check if folder already exists
        plenary_folder_name = plenary.plenary_folder_name
        plenary_folder_id = file_repo.create_folder(plenary_folder_name)
        plenary = plenary_repo.update_plenary_folder(plenary, plenary_folder_id)
        file_repo.move_file_to_folder(plenary.plenary_folder_id, config.GOOGLE_DRIVE_ROOT_FOLDER_ID)

        # make readable
        permissions_repo.make_world_readable(plenary_folder_id)

        # ============ Make subfolders
        # -------- first reading
        first_reading_folder_id = file_repo.create_folder(Templates.FIRST_READING_FOLDER_NAME)
        plenary = plenary_repo.update_plenary_first_reading_folder(plenary, first_reading_folder_id)
        file_repo.move_file_to_folder(plenary.first_reading_folder_id, plenary.plenary_folder_id)
        # make readable
        permissions_repo.make_world_readable(first_reading_folder_id)

        # -------- Second reading
        second_reading_folder_id = file_repo.create_folder(Templates.ACTION_FOLDER_NAME)
        plenary = plenary_repo.update_plenary_second_reading_folder(plenary, second_reading_folder_id)
        file_repo.move_file_to_folder(plenary.second_reading_folder_id, plenary.plenary_folder_id)
        # make readable
        permissions_repo.make_world_readable(second_reading_folder_id)

        # -------- Working drafts
        working_drafts_folder_id = file_repo.create_folder(Templates.WORKING_DRAFTS_FOLDER_NAME)
        plenary = plenary_repo.update_working_drafts_folder(plenary, working_drafts_folder_id)
        file_repo.move_file_to_folder(plenary.working_drafts_folder_id, plenary.plenary_folder_id)
        # make readable
        permissions_repo.make_world_readable(working_drafts_folder_id)

        print("created folders ")
        print(f"Plenary folder id : {plenary.plenary_folder_id} \n First readings folder id : {plenary.first_reading_folder_id} \n Second reading folder id : {plenary.second_reading_folder_id}")
        return plenary
    except Exception as e:
        logger.warning(e)


if __name__ == '__main__':
    main()
