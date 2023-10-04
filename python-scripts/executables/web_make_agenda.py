import sys

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.AgendaRepository import AgendaRepository


def main(plenary_id=None):
    if plenary_id is None:
        plenary_id = int(sys.argv[1])

    dao = MySqlDao()
    agenda_repo = AgendaRepository(dao)
    plenary_repo = PlenaryRepository(dao)

    plenary = plenary_repo.load_plenary(plenary_id)

    agenda_repo.make_resolution_list(plenary)


if __name__ == '__main__':
    main()
