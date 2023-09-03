import sys
sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

# sys.path.append("/Users/ars62917/Dropbox/ResolutionManager")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.FileRepository import FileRepository

def main(plenary_id=None):
    if plenary_id is None:
        plenary_id = int(sys.argv[1])

    dao = MySqlDao()
    plenary_repo = PlenaryRepository(dao)
    permission_repo = PermissionsRepository()
    file_repo = FileRepository()

    plenary = plenary_repo.load_plenary(plenary_id)

    for f in file_repo.list_files(folder_id=plenary.first_reading_folder_id):
        permission_repo.make_world_writeable(f['id'])

    return plenary

if __name__ == '__main__':
    main()
