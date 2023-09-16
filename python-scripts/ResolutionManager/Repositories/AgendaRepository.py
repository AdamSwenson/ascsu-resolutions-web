from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from ResolutionManager.API.CredentialsManager import CredentialsManager
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.StylingRepository import StylingRepository
from ResolutionManager.config.Templates import Templates


class AgendaRepository(object):
    """
    This handles everything having to do with the document containing the
    list of resolutions
    """

    def __init__(self, dao):
        self.dao = dao
        self.cred_manager = CredentialsManager()
        self.service = build('docs', 'v1', credentials=self.cred_manager.creds)
        self.resolution_repo = ResolutionRepository(self.dao)
        self.plenary_repo = PlenaryRepository(self.dao)
        self.permission_repo = PermissionsRepository()
        self.document_repo = DocumentRepository()
        self.file_repo = FileRepository()

        self.idx = 1

    def create_agenda_file(self, plenary: Plenary):
        # Create an agenda document
        fname = Templates.AGENDA_FILENAME_TEMPLATE.format(plenary_name=plenary.plenary_folder_name)
        agenda_id = self.document_repo.create_file(fname)
        self.file_repo.move_file_to_folder(agenda_id, plenary.plenary_folder_id)

        # store agenda id so can update
        plenary = self.plenary_repo.update_agenda_id(plenary, agenda_id)

        # todo Decide whether want this once have everything working properly
        self.permission_repo.make_world_writeable(agenda_id)
        return agenda_id

    def make_first_readings_heading_requests(self):
        text = "\nFirst Readings \n"
        requests = []
        requests.append({
            'insertText': {
                'location': {
                    'index': self.idx,
                },
                'text': text,
            }
        })
        requests.append({
            'updateTextStyle': {
                'range': {
                    'startIndex': self.idx,
                    'endIndex': self.idx + len(text)
                },
                'textStyle': {
                    'bold': True,
                },
                'fields': 'bold'
            }
        })

        self.idx += len(text)
        return requests

    def make_action_items_heading_requests(self):
        text = "\nAction Items \n"
        requests = []
        requests.append({
            'insertText': {
                'location': {
                    'index': self.idx,
                },
                'text': text,
            }
        })
        requests.append({
            'updateTextStyle': {
                'range': {
                    'startIndex': self.idx,
                    'endIndex': self.idx + len(text)
                },
                'textStyle': {
                    'bold': True,
                },
                'fields': 'bold'
            }
        })

        self.idx += len(text)
        return requests

    def make_resolution_list_item_requests(self, resolution):
        """Returns a list of request objects required to make the entry"""
        requests = []
        text = f"{resolution.agenda_item} \n"
        requests.append({
            'insertText': {
                'location': {
                    'index': self.idx,
                },
                'text': text,
            }
        })
        self.idx += len(text)

        url_text = f"{resolution.url} \n\n"
        requests.append({
            'insertText': {
                'location': {
                    'index': self.idx,
                },
                'text': url_text
            }
        })

        requests.append(
            {
                "updateTextStyle": {
                    "textStyle": {
                        "link": {
                            "url": resolution.url
                        }
                    },
                    "range": {
                        "startIndex": self.idx,
                        "endIndex": self.idx + len(url_text)
                    },
                    "fields": "link"
                }
            })

        self.idx += len(url_text)

        return requests

    def make_resolution_list(self, plenary: Plenary):
        """
        Creates the Resolution list google doc for the plenary.
        MAIN CALLED METHOD

        :param plenary: Plenary
        :return:
        """
        # Get all resolutions
        # For now not going to sync the database, just use title from drive if can be retrieved and default to db version
        resolutions = self.resolution_repo.load_all_resolutions_for_plenary(plenary)
        # resolutions = self.resolution_repo.load_all_resolutions()
        first_readings = [r for r in resolutions if r.is_first_reading is True and r.waiver is False]
        # todo Once figure out how committees indicate ready for second reading, remove waiver check
        waivers = [r for r in resolutions if r.is_first_reading and r.waiver is True]
        second_readings = [r for r in resolutions if r.is_first_reading is not True]

        self.create_agenda_file(plenary)

        # # Create an agenda document
        # fname = Templates.AGENDA_FILENAME_TEMPLATE.format(plenary_name=plenary.plenary_folder_name)
        # agenda_id = self.document_repo.create_file(fname)
        # self.file_repo.move_file_to_folder(agenda_id, plenary.plenary_folder_id)
        #
        # # store agenda id so can update
        # plenary = self.plenary_repo.update_agenda_id(plenary, agenda_id)
        #
        # # todo Decide whether want this once have everything working properly
        # self.permission_repo.make_world_writeable(agenda_id)

        print(plenary.agenda_id)

        self.idx = 1
        requests = []

        # todo Make action items header and update index
        aih = self.make_action_items_heading_requests()
        requests.extend(aih)

        for r in second_readings:
            try:
                sr = self.make_resolution_list_item_requests(r)
                requests.extend(sr)
            except Exception:
                pass

        for w in waivers:
            try:
                sr = self.make_resolution_list_item_requests(w)
                requests.extend(sr)
            except Exception:
                pass


        # todo Make first reading header and update index
        frh = self.make_first_readings_heading_requests()
        requests.extend(frh)

        for f in first_readings:
            try:
                fr = self.make_resolution_list_item_requests(f)
                requests.extend(fr)
            except Exception:
                pass

        #
        # for r in resolutions:
        #     try:
        #         text = f"{r.agenda_item} \n"
        #         requests.append({
        #             'insertText': {
        #                 'location': {
        #                     'index': idx,
        #                 },
        #                 'text': text,
        #             }
        #         })
        #         idx += len(text)
        #
        #         url_text = f"{r.url} \n\n"
        #         requests.append({
        #             'insertText': {
        #                 'location': {
        #                     'index': idx,
        #                 },
        #                 'text': url_text
        #             }
        #         })
        #
        #         requests.append(
        #             {
        #                 "updateTextStyle": {
        #                     "textStyle": {
        #                         "link": {
        #                             "url": r.url
        #                         }
        #                     },
        #                     "range": {
        #                         "startIndex": idx,
        #                         "endIndex": idx + len(url_text)
        #                     },
        #                     "fields": "link"
        #                 }
        #             })
        #         idx += len(url_text)
        #
        #     except Exception:
        #         pass

        print(requests)

        result = self.service.documents().batchUpdate(documentId=plenary.agenda_id,
                                                      body={'requests': requests}).execute()
