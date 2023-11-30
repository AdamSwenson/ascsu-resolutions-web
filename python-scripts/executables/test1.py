import sys

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

import os

import google

from ResolutionManager.Repositories.ErrorHandlingRepository import ErrorHandlingRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.ResolutionTemplateRespository import ResolutionTemplateRepository

from ResolutionManager.config.Templates import Templates
from ResolutionManager.DAO.DAO import MySqlDao

from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository
# from Repositories.CommitteeRepository import CommitteeRepository
from ResolutionManager.Repositories.AgendaRepository import AgendaRepository

def main():
    plenary_id = 6

    # Load from database
    dao = MySqlDao()
    resolution_repo = ResolutionRepository(dao)
    plenary_repo = PlenaryRepository(dao)

    plenary = plenary_repo.load_plenary(plenary_id)

    # template_repo = ResolutionTemplateRepository(plenary=plenary, dao=dao)

    try:
        resolution_repo.load_all_resolutions()

        # resolution_file = template_repo.create_file_from_template(resolution=resolution)
    except (Exception,  google.auth.exceptions.RefreshError) as e:
        sys.stdout.write(f"bbep {e}")
        print(e)
        error_repo = ErrorHandlingRepository()
        # Delete old token file
        print(error_repo.token_path)
        error_repo.delete_old_token()
        resolution_repo.load_all_resolutions()

    #
    # path = f"{os.getcwd()}/private/token.json"
    #
    # try:
    #     if os.path.isfile(path):
    #         print(path)
    # except OSError as e:
    #     # If it fails, inform the user.
    #     print(f"Error: {e.filename} - {e.strerror}")
    #
    import datetime
    # import DAO.DAO
    # print(Templates.RESOLUTION_FILENAME_TEMPLATE.format(resolution_number= 56, resolution_name='j', committee_abbrev='tt'))
    # dao = MySqlDao()
    # agenda_repo = AgendaRepository(dao)
    #
    # agenda_repo.create_agenda_file()

    # committee_repo = CommitteeRepository(dao)
    # resolution_repo = ResolutionRepository(dao)
    # plenary_repo = PlenaryRepository(dao)


    # n = sys.argv[1]
    #
    #
    # print('taco' + n)
    # sys.stdout.write("Hello")
    # return 'taco ' + n

if __name__ == '__main__':
    main()
