import logging
import sys

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.config.Configuration import Configuration


def main(plenary_id=None):
    # if plenary_id is None:
    #     plenary_id = int(sys.argv[1])
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:
        dao = MySqlDao()
        resolution_repo = ResolutionRepository(dao)
        results = resolution_repo.load_all_resolutions()

        # query = f"select id from ascsu.resolutions"
        # results = resolution_repo.dao.conn.execute(query)
        for r in results:
            # rid = r[0]
            resolution_repo.update_title_from_drive_version(r)
    except Exception as e:
        logger.warning(e)

if __name__ == '__main__':
    main()
