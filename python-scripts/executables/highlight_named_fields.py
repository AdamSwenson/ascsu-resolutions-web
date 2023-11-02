"""
Used to troubleshoot named ranges by highlighting them
"""

import sys

sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.DAO.DAO import MySqlDao

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.StylingRepository import StylingRepository


def main(resolution_id=None):
    """
    Highlights the named ranges to assist in troubleshooting
    :param resolution_id:
    :return:
    """
    if resolution_id is None:
        resolution_id = int(sys.argv[1])

    dao = MySqlDao()
    resolution_repo = ResolutionRepository(dao)
    style_repo = StylingRepository()
    resolution = resolution_repo.load_resolution(resolution_id)

    named_ranges = [
        {'name': style_repo.config.TITLE_RANGE_NAME,
         'indicies': style_repo.get_indicies_for_named_range(resolution, style_repo.config.TITLE_RANGE_NAME)[0],
         'color': {
             "rgbColor": {
                 "red": 1,
                 "green": 0,
                 "blue": 0
             }
         }
         },

        {'name': style_repo.config.GROUP_TITLE_RANGE_NAME,
         'indicies': style_repo.get_indicies_for_named_range(resolution, style_repo.config.GROUP_TITLE_RANGE_NAME)[0],
         'color': {
             "rgbColor": {
                 "red": 0,
                 "green": 1,
                 "blue": 0
             }
         }
         },

        {'name': style_repo.config.RATIONALE_RANGE_NAME,
         'indicies': style_repo.get_indicies_for_named_range(resolution, style_repo.config.RATIONALE_RANGE_NAME)[0],
         'color': {
             "rgbColor": {
                 "red": 0,
                 "green": 0,
                 "blue": 1
             }
         }
         },

        {'name': style_repo.config.TITLE_RANGE_NAME,
         'indicies': style_repo.get_indicies_for_named_range(resolution, style_repo.config.TITLE_RANGE_NAME)[0],
         'color': {
             "rgbColor": {
                 "red": 1,
                 "green": 0,
                 "blue": 0
             }
         }
         },

        {'name': style_repo.config.DISTRIBUTION_LIST_RANGE_NAME,
         'indicies':
             style_repo.get_indicies_for_named_range(resolution, style_repo.config.DISTRIBUTION_LIST_RANGE_NAME)[0],
         'color': {
             "rgbColor": {
                 "red": 0.5,
                 "green": 0,
                 "blue": 0.5
             }
         }
         },
    ]

    sys.stdout.write(f"{named_ranges}")

    requests = []

    for n in named_ranges:
        requests.append({
            'updateParagraphStyle': {
                'range': {
                    'startIndex': n['indicies']['startIndex'],
                    'endIndex': n['indicies']['endIndex']
                },
                'paragraphStyle': {
                    'shading': {
                        'backgroundColor': {
                            "color": n['color']
                        },
                    }
                },
                'fields': 'shading'
            }
        })

    body = {'requests': requests}
    # if revision_id is not None:
    #     # Lock to ensure that hasn't change since we fetched
    #     body['writeControl'] = {'requiredRevisionId': revision_id}

    style_repo.service.documents().batchUpdate(
        documentId=resolution.document_id,
        body=body
    ).execute()


if __name__ == '__main__':
    main()
