import sys
from ResolutionManager.DAO.DAO import MySqlDao

import datetime
# https://stackoverflow.com/questions/55102788/module-not-found-running-on-command-line

def main():


    # committee_repo = CommitteeRepository(dao)
    # resolution_repo = ResolutionRepository(dao)
    # plenary_repo = PlenaryRepository(dao)


    n = sys.argv[1]


    print('taco' + n)
    sys.stdout.write("Hello")
    return 'taco ' + n

if __name__ == '__main__':
    main()