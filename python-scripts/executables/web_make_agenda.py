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


def main(resolution_id=None):
    if resolution_id is None:
        resolution_id = int(sys.argv[2])
    # sys.stdout.write(f"{plenary_id} {resolution_id}")

    # Load from database
    dao = MySqlDao()
    committee_repo = CommitteeRepository(dao)
    resolution_repo = ResolutionRepository(dao)
    plenary_repo = PlenaryRepository(dao)
    permission_repo = PermissionsRepository()



    resolution = resolution_repo.load_resolution(30)
    resolution.document_id
    resolution_repo.get_current_title_from_drive(resolution)

docid = "16Bwqhrn38yU1KATbZ1T3B_5ATMMfXiFgKuqXeUKZlwE"
newdoc = doc_repo.get_document(docid)
startIndex = get_named_ranges(newdoc)[0]['startIndex']
get_title(newdoc, startIndex)


