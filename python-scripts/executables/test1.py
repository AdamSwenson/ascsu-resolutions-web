import sys


# https://stackoverflow.com/questions/55102788/module-not-found-running-on-command-line
# sys.path.append("/Users/ars62917/Dropbox/ResolutionManager/ResolutionManager")
sys.path.append("/Users/ars62917/Dropbox/ResolutionManager")

from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository
# from Repositories.CommitteeRepository import CommitteeRepository


def main():
    import datetime
    # import DAO.DAO

    # committee_repo = CommitteeRepository(dao)
    # resolution_repo = ResolutionRepository(dao)
    # plenary_repo = PlenaryRepository(dao)


    n = sys.argv[1]


    print('taco' + n)
    sys.stdout.write("Hello")
    return 'taco ' + n

if __name__ == '__main__':
    main()