import logging
import sys


sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.config.Configuration import Configuration

from ResolutionManager.DAO.DAO import MySqlDao

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.StylingRepository import StylingRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository


def main(plenary_id=None):
    config = Configuration()
    logger = logging.getLogger(__name__)

    try:
        if plenary_id is None:
            plenary_id = int(sys.argv[1])

        dao = MySqlDao()
        resolution_repo = ResolutionRepository(dao)
        style_repo = StylingRepository()
        plenary_repo = PlenaryRepository(dao)

        plenary = plenary_repo.load_plenary(plenary_id)

        resolutions = resolution_repo.load_all_resolutions_for_plenary(plenary)

        for r in resolutions:
            try:
                style_repo.enforce_styling_on_resolution(r)
            except Exception as e:
                print(r, e)
                t = f"{e} \n {r}"
                logger.warning(t)
    except Exception as e:
        logger.warning(e)


if __name__ == '__main__':
    main()

    #
    #
    # docid = '1Mc3L3DgCxZ9hOCbBnzAMogWybZvpAX2V5w1mc5nBppk'
    # doc = doc_repo.get_document(docid)
    #
    # def get_end_index(document):
    #     body = document.get('body').get('content')
    #     return body[len(body) - 1]['endIndex']
    #
    # startIndex = 1
    # endIndex = get_end_index(doc)
    # requests = [{
    #     'updateTextStyle': {
    #                 'range': {
    #                     'startIndex':startIndex,
    #                     'endIndex': endIndex
    #                 },
    #                 'textStyle': {
    #                     'weightedFontFamily': {
    #                         'fontFamily':  'Atkinson Hyperlegible'
    #
    #                     },
    #                     'fontSize': {
    #                         'magnitude': 12,
    #                         'unit': 'PT'
    #                     },
    #                 },
    #                         'fields': 'weightedFontFamily,fontSize'
    #
    #     }
    # }
    # ]
    #
    # doc_repo.service.documents().batchUpdate(
    #             documentId=docid, body={'requests': requests}).execute()
    #
