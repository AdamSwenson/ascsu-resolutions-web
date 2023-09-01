import sys
sys.path.append("/Users/ars62917/Dropbox/ResolutionManager")


from ResolutionManager.Repositories.FileRepository import FileRepository
import ResolutionManager.config.environment as env
from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository

# PLENARY_FOLDER_TEMPLATE = "{year} {month}"
RESOLUTIONS_ROOT_NAME = 'Resolutions'
FIRST_READING_FOLDER_NAME = 'First reading'
ACTION_FOLDER_NAME = 'Action items'


def main(plenary_id=None):
    if plenary_id is None:
        plenary_id = int(sys.argv[1])

    file_repo = FileRepository()
    # Load from database
    dao = MySqlDao()
    plenary_repo = PlenaryRepository(dao)
    plenary = plenary_repo.load_plenary(plenary_id)

    # todo Check if folder already exists
    plenary_folder_name = plenary.plenary_folder_name
    # plenary_folder_name = PLENARY_FOLDER_TEMPLATE.format(year=2023, month='September')
    plenary_folder_id = file_repo.create_folder(plenary_folder_name)
    plenary = plenary_repo.update_plenary_folder(plenary, plenary_folder_id)
    # plenary_root_folder_id = file_repo.create_folder(plenary_folder_name)
    file_repo.move_file_to_folder(plenary.plenary_folder_id, env.GOOGLE_DRIVE_ROOT_FOLDER_ID)

    # Make subfolders
    first_reading_folder_id = file_repo.create_folder(FIRST_READING_FOLDER_NAME)
    plenary = plenary_repo.update_plenary_first_reading_folder(plenary, first_reading_folder_id)
    # first_reading_folder_id = file_repo.create_folder(FIRST_READING_FOLDER_NAME)

    file_repo.move_file_to_folder(plenary.first_reading_folder_id, plenary.plenary_folder_id)
    second_reading_folder_id = file_repo.create_folder(ACTION_FOLDER_NAME)
    plenary = plenary_repo.update_plenary_second_reading_folder(plenary, second_reading_folder_id)
    file_repo.move_file_to_folder(plenary.second_reading_folder_id, plenary.plenary_folder_id)

    print("created folders ")
    print(f"Plenary folder id : {plenary.plenary_folder_id} \n First readings folder id : {plenary.first_reading_folder_id} \n Second reading folder id : {plenary.second_reading_folder_id}")
    return plenary

if __name__ == '__main__':
    main()
