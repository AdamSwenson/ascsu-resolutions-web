import sys
sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.DAO.DAO import MySqlDao

from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
from ResolutionManager.config.Templates import Templates


def main(plenary_id=None):
    if plenary_id is None:
        plenary_id = int(sys.argv[1])

    # Load from database
    dao = MySqlDao()
    committee_repo = CommitteeRepository(dao)
    resolution_repo = ResolutionRepository(dao)
    plenary_repo = PlenaryRepository(dao)
    permission_repo = PermissionsRepository()
    document_repo = DocumentRepository()
    file_repo = FileRepository()

    plenary = plenary_repo.load_plenary(plenary_id)

    # Get all resolutions
    # For now not going to sync the database, just use title from drive if can be retrieved and default to db version
    resolutions = resolution_repo.load_all_resolutions()

    # Create an agenda document
    fname = Templates.AGENDA_FILENAME_TEMPLATE.format(plenary_name=plenary.plenary_folder_name)
    agenda_id = document_repo.create_file(fname)
    file_repo.move_file_to_folder(agenda_id, plenary.plenary_folder_id)

    # store agenda id so can update
    plenary = plenary_repo.update_agenda_id(plenary, agenda_id)

    # todo Decide whether want this once have everything working properly
    permission_repo.make_world_writeable(agenda_id)

    print(agenda_id)

    idx = 1
    requests = []
    for r in resolutions:
        try:
            text = f"{r.agenda_item} \n"
            requests.append({
                'insertText': {
                    'location': {
                        'index': idx,
                    },
                    'text': text,
                }
            })
            idx += len(text)

            url_text = f"{r.url} \n\n"
            requests.append({
                'insertText': {
                    'location': {
                        'index': idx,
                    },
                    'text': url_text
                }
            })

            requests.append(
                {
                    "updateTextStyle": {
                        "textStyle": {
                            "link": {
                                "url": r.url
                            }
                        },
                        "range": {
                            "startIndex": idx,
                            "endIndex": idx + len(url_text)
                        },
                        "fields": "link"
                    }
                })
            idx += len(url_text)

        except Exception:
            pass

    print(requests)

    result = document_repo.service.documents().batchUpdate(documentId=agenda_id, body={'requests': requests}).execute()

    # # Currently this only inserts text and link but does not create a clickable link
    # text = ""
    # try:
    #     for r in resolutions:
    #         text += f"{r.agenda_item} \n"
    #         #         text += f"{r.url}\n"
    # except Exception:
    #     print(f"Error with : {r.__dict__}")
    #     pass
    #
    # requests.append({
    #     'insertText': {
    #         'location': {
    #             'index': idx,
    #         },
    #         'text': text,
    #     }
    # })
    #
    # # TODO Make this work so that the links are live
    # # for r in resolutions:
    # #     try:
    # #         text = f"{r.agenda_item} \n"
    # #         requests.append(    {
    # #         'insertText': {
    # #             'location': {
    # #                 'index': idx,
    # #             },
    # #             'text': text,
    # #         }
    # #         })
    # #         idx += len(text)
    #
    # #         requests.append(    {
    # #         'insertText': {
    # #             'location': {
    # #                 'index': idx,
    # #             },
    # #             'text': r.url,
    # #         }
    # #         })
    #
    # # #         requests.append(
    # # #          {
    # # #              "updateTextStyle": {
    # # #                  "textStyle": {
    # # #                      "link": {
    # # #                          "url": r.url
    # # #                      }
    # # #                  },
    # # #                  "range": {
    # # #                      "startIndex": idx,
    # # #                      "endIndex": idx + len(r.url)
    # # #                  },
    # # #                  "fields": "link"
    # # #              }
    # # #          }
    # # #         )
    # #         idx += len(r.url)
    #
    # #     except Exception:
    # #         pass
    #
    # print(requests)
    #
    # result = document_repo.service.documents().batchUpdate(documentId=agenda_id, body={'requests': requests}).execute()
    # sys.stdout.write(f"{result.__dict__}")

if __name__ == '__main__':
    main()

# ================================ do not need
    # # Get all resolutions
    # # For now not going to sync the database, just use title from drive if can be retrieved and default to db version
    # resolutions = resolution_repo.load_all_resolutions()
    #
    # # Create an agenda document
    # fname = f"{plenary.plenary_folder_name} Agenda"
    # # fname = AGENDA_FILENAME_TEMPLATE.format({'plenary_name' : plenary.plenary_folder_name})
    # agenda_id = document_repo.create_file_in_folder(plenary.plenary_folder_id, fname)
    # # maybe should store, that way can update
    #
    # text = [f"{r.agenda_item} \n" for r in resolutions]
    #
    # requests = [
    #     {
    #         'insertText': {
    #             'location': {
    #                 'index': 1,
    #             },
    #             'text': text
    #
    #         }
    #     }
    # ]
    # result = document_repo.service.documents().batchUpdate(documentId=agenda_id, body={'requests': requests}).execute()
    #
    # # resolutions = []
    # # query = f"select id from ascsu.resolutions"
    # # results = dao.conn.execute(query)
    # # for r in results:
    # #     rid = r[0]
    # #     sponsor = committee_repo.load_sponsor(rid)
    # #     cosponsors = committee_repo.load_cosponsors(rid)
    # #     rez = resolution_repo.load_resolution(rid, sponsor, cosponsors)
    # #     try:
    # #         doc_title = resolution_repo.get_current_title_from_drive(rez)
    # #         if len(doc_title)>0:
    # #             rez.title = doc_title
    # #     except Exception:
    # #         # todo Catch appropriately
    # #         pass
    # #
    # #     resolutions.append(rez)
    # #
    # #
    # #
    #
