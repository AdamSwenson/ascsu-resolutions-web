import sys

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.config.Templates import Templates

from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository
# from Repositories.CommitteeRepository import CommitteeRepository


def main():
    import datetime
    # import DAO.DAO
    print(Templates.RESOLUTION_FILENAME_TEMPLATE.format(resolution_number= 56, resolution_name='j', committee_abbrev='tt'))

    # committee_repo = CommitteeRepository(dao)
    # resolution_repo = ResolutionRepository(dao)
    # plenary_repo = PlenaryRepository(dao)


    # n = sys.argv[1]
    #
    #
    # print('taco' + n)
    sys.stdout.write("Hello")
    # return 'taco ' + n

if __name__ == '__main__':
    main()
