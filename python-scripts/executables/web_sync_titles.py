import sys
import os

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")


from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.ResolutionTemplateRespository import ResolutionTemplateRepository
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Models.Committees import Committee
from ResolutionManager.Models.Resolutions import Resolution
from ResolutionManager.DAO.DAO import MySqlDao


from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository



def main(plenary_id=None):
    # if plenary_id is None:
    #     plenary_id = int(sys.argv[1])

        # Load from database
    dao = MySqlDao()
    # committee_repo = CommitteeRepository(dao)
    resolution_repo = ResolutionRepository(dao)
    # plenary_repo = PlenaryRepository(dao)
    # permission_repo = PermissionsRepository()
    # document_repo = DocumentRepository()
    # file_repo = FileRepository()
    #
    # plenary = plenary_repo.load_plenary(plenary_id)

    results = resolution_repo.load_all_resolutions()


    # query = f"select id from ascsu.resolutions"
    # results = resolution_repo.dao.conn.execute(query)
    for r in results:
        # rid = r[0]
        resolution_repo.update_title_from_drive_version(r)


if __name__ == '__main__':
    main()
