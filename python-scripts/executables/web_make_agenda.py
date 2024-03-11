import logging
import sys

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.AgendaRepository import AgendaRepository
from ResolutionManager.config.Configuration import Configuration

import web_sync_action_item_status as action_sync

def main(plenary_id=None):
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:

        if plenary_id is None:
            plenary_id = int(sys.argv[1])

        action_sync.main(plenary_id)

        dao = MySqlDao()
        agenda_repo = AgendaRepository(dao)
        plenary_repo = PlenaryRepository(dao)

        plenary = plenary_repo.load_plenary(plenary_id)

        agenda_repo.make_resolution_list(plenary)
    except Exception as e:
        logger.warning(e)

if __name__ == '__main__':
    main()
