import sys
import os


sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.ErrorHandlingRepository import ErrorHandlingRepository


def main():
    """
    This is used to trigger the authentication process to get
    a new token.
    Make sure token.json has been deleted first

    :return:
    """
    error_repo = ErrorHandlingRepository()

    # Delete old token file
    error_repo.delete_old_token()

    # Trigger the new oauth request to generate a new token
    dao = MySqlDao()
    resolution_repo = ResolutionRepository(dao)
    results = resolution_repo.load_all_resolutions()



if __name__ == '__main__':
    main()
