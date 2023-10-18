import sys
import os
sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository


def main():
    """
    This is used to trigger the authentication process to get
    a new token.
    Make sure token.json has been deleted first

    :return:
    """

    # Delete old token file
    try:
        path = f"{os.getcwd()}/private/token.json"
        if os.path.isfile(path):
            os.remove(path)

    except OSError as e:
        # If it fails, inform the user.
        print(f"Error: {e.filename} - {e.strerror}")

    # Trigger the new oauth request to generate a new token
    dao = MySqlDao()
    resolution_repo = ResolutionRepository(dao)
    results = resolution_repo.load_all_resolutions()



if __name__ == '__main__':
    main()
