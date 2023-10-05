import sys

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository


def main(resolution_id=None):
    if resolution_id is None:
        resolution_id = int(sys.argv[1])

    dao = MySqlDao()
    resolution_repo = ResolutionRepository(dao)
    permission_repo = PermissionsRepository()

    resolution = resolution_repo.load_resolution(resolution_id)

    permission_repo.make_world_readable(resolution.document_id)

    return resolution


if __name__ == '__main__':
    main()
