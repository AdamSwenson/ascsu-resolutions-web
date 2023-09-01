import json
import sys
sys.path.append("/Users/ars62917/Dropbox/ResolutionManager")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
# from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
# from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository

def main(resolution_id=None):
    if resolution_id is None:
        resolution_id = int(sys.argv[1])

    dao = MySqlDao()
    resolution_repo = ResolutionRepository(dao)
    permission_repo = PermissionsRepository()
    # file_repo = FileRepository()
    resolution = resolution_repo.load_resolution(resolution_id)

    result = permission_repo.get_permission(resolution.document_id)
    result = json.dumps(result)
    sys.stdout.write(result)
    # sys.stdout.write(f"{result}")
    return result

if __name__ == '__main__':
    main()