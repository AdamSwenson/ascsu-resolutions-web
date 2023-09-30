import sys

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.StylingRepository import StylingRepository
from ResolutionManager.Repositories.ResolutionTemplateRespository import ResolutionTemplateRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository

def main(plenary_id=None, resolution_id=None):

    if plenary_id is None:
        plenary_id = int(sys.argv[1])
    if resolution_id is None:
        resolution_id = int(sys.argv[2])

    dao = MySqlDao()
    resolution_repo = ResolutionRepository(dao)
    committee_repo = CommitteeRepository(dao)
    # style_repo = StylingRepository()

    plenary_repo = PlenaryRepository(dao=dao)
    plenary = plenary_repo.load_plenary(plenary_id=plenary_id)
    # Load everything
    sponsor = committee_repo.load_sponsor(resolution_id)
    cosponsors = committee_repo.load_cosponsors(resolution_id)

    resolution_template_repo = ResolutionTemplateRepository(plenary=plenary, dao=dao)

    resolution = resolution_repo.load_resolution(resolution_id=resolution_id, sponsor=sponsor, cosponsors=cosponsors)
    # try:
    resolution_template_repo.add_approved(resolution)
    # except Exception as e:
    #     # todo make more specific
    #     # todo Add error logging
    #     print(e)


if __name__ == '__main__':
    main()
