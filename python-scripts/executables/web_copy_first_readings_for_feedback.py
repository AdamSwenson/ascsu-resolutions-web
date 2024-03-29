import logging
import sys


sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.config.Templates import Templates
from ResolutionManager.config.Configuration import Configuration


def main(plenary_id=None):
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:

        if plenary_id is None:
            plenary_id = int(sys.argv[1])

        dao = MySqlDao()

        doc_repo = DocumentRepository()
        file_repo = FileRepository()
        plenary_repo = PlenaryRepository(dao)

        plenary = plenary_repo.load_plenary(plenary_id)

        # Create new folder for feedback versions
        # todo This needs to check that the folder doesn't already exist
        feedback_folder_id = file_repo.create_folder(Templates.PUBLIC_FOLDER_NAME)
        plenary = plenary_repo.update_feedback_folder(plenary, feedback_folder_id=feedback_folder_id)
        file_repo.move_file_to_folder(plenary.feedback_folder_id, plenary.plenary_folder_id)

        # Make copies and move to new folder
        files = file_repo.list_files(folder_id=plenary.first_reading_folder_id)

        for f in files:
            new_name = Templates.FILENAME_TEMPLATE.format(f['name'])
            copy_id = file_repo.copy_file(f['id'], new_name)
            file_repo.move_file_to_folder(copy_id, plenary.feedback_folder_id)

        return plenary
    except Exception as e:
        logger.warning(e)

    # todo Return link to sharable folder


if __name__ == '__main__':
    main()
