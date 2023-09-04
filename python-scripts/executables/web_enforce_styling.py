import sys
import os

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
# from ResolutionManager.Repositories.FileRepository import FileRepository

from ResolutionManager.DAO.DAO import MySqlDao
# from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository
# from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository

def main():
    # if plenary_id is None:
    #     plenary_id = int(sys.argv[1])

    dao = MySqlDao()
    # committee_repo = CommitteeRepository(dao)
    # plenary_repo = PlenaryRepository(dao)
    resolution_repo = ResolutionRepository(dao)
    doc_repo = DocumentRepository()
    # file_repo = FileRepository()

    resolutions = resolution_repo.load_all_resolutions()

    for r in resolutions:
        try:
            doc_repo.enforce_styling_on_resolution(r)
        except Exception as e:
            # todo make more specific
            # todo Add error logging
            print(e)

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
