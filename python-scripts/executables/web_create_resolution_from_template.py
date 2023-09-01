import sys
sys.path.append("/Users/ars62917/Dropbox/ResolutionManager")

# from ResolutionManager import environment as env

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

    # Load everything
    sponsor = committee_repo.load_sponsor(resolution_id)
    cosponsors = committee_repo.load_cosponsors(resolution_id)
    resolution = resolution_repo.load_resolution(resolution_id=resolution_id, sponsor=sponsor, cosponsors=cosponsors)
    plenary = plenary_repo.load_plenary(plenary_id)

    # sys.stdout.write(resolution.title)
    # return resolution

    template_repo = ResolutionTemplateRepository(plenary=plenary, dao=dao)

    resolution_file = template_repo.create_file_from_template(resolution=resolution)
    template_repo.update_title(resolution_file)
    template_repo.update_header(resolution_file)

    print(resolution_file.__dict__)

    # resolution_name = "Opposing the existence of the CO"
    # resolution_number = 3456
    # committee = Committee('Faculty Affairs', 'FA')
    # cosponsors = [ Committee('Academic Affairs', 'AA')]
    # resolution = Resolution(resolution_number, resolution_name, committee, cosponsors)
    #
    # plenary = Plenary(year=2023,
    #                   month='September',
    #                   thursday_date=12,
    #                   friday_date=14,
    #                   first_reading_folder_id='1sv_4BUV5fk6Kcjss8HeSCJWnsLZJVpKC'
    #                   )


if __name__ == '__main__':
    main()
