import sys


sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Models.Committees import Committee
from ResolutionManager.Models.Resolutions import Resolution

from ResolutionManager.DAO.DAO import MySqlDao

from ResolutionManager.Repositories.ResolutionTemplateRespository import ResolutionTemplateRepository
from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
from ResolutionManager.Repositories.ErrorHandlingRepository import ErrorHandlingRepository


import google


def main(plenary_id=None, resolution_id=None):

    if plenary_id is None:
        plenary_id = int(sys.argv[1])
    if resolution_id is None:
        resolution_id = int(sys.argv[2])
    # sys.stdout.write(f"{plenary_id} {resolution_id}")

    # Load from database
    dao = MySqlDao()
    committee_repo = CommitteeRepository(dao)
    resolution_repo = ResolutionRepository(dao)
    plenary_repo = PlenaryRepository(dao)
    permission_repo = PermissionsRepository()

    # Load everything
    sponsor = committee_repo.load_sponsor(resolution_id)
    cosponsors = committee_repo.load_cosponsors(resolution_id)
    resolution = resolution_repo.load_resolution(resolution_id=resolution_id, sponsor=sponsor, cosponsors=cosponsors)
    plenary = plenary_repo.load_plenary(plenary_id)

    template_repo = ResolutionTemplateRepository(plenary=plenary, dao=dao)

    resolution_file = template_repo.create_file_from_template(resolution=resolution)

    # Make readable since this must happen before range updates
    permission_repo.make_world_writeable(resolution.document_id)

    # Update parts of the file
    # AR-29
    template_repo.update_title_new(resolution_file)
    # template_repo.update_title(resolution_file)
    template_repo.update_header(resolution_file)

    print(resolution_file.__dict__)


if __name__ == '__main__':
    main()
