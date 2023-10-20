import sys
sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.FileRepository import FileRepository


def main(plenary_id=None):
    if plenary_id is None:
        plenary_id = int(sys.argv[1])

    dao = MySqlDao()
    plenary_repo = PlenaryRepository(dao)
    resolution_repo = ResolutionRepository(dao)
    file_repo = FileRepository()

    plenary = plenary_repo.load_plenary(plenary_id)

    # Get information about what resolutions are in the action items
    # folder from the google drive
    files = file_repo.list_files(plenary.second_reading_folder_id)

    # Load models
    rez = resolution_repo.load_all_resolutions_for_plenary(plenary)

    # identify action items based on if in action items folder
    action_item_ids = [f['id'] for f in files]
    action_items = [r for r in rez if r.document_id in action_item_ids]
    # need these in case something got moved from action items folder
    non_action_items = [r for r in rez if r not in action_items]

    for r in action_items:
        resolution_repo.set_as_action_item(plenary, r)

    for r in non_action_items:
        resolution_repo.set_as_first_reading_item(plenary, r)


if __name__ == '__main__':
    main()
