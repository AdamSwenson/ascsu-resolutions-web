import logging
import sys

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from ResolutionManager.API.CredentialsManager import CredentialsManager
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.PermissionsRepository import PermissionsRepository
from ResolutionManager.Repositories.PlenaryRepository import PlenaryRepository
from ResolutionManager.Repositories.RequestRepository import RequestRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.Repositories.StylingRepository import StylingRepository
from ResolutionManager.config.Configuration import Configuration
from ResolutionManager.config.Templates import Templates


class AgendaRepository(object):
    """
    This handles everything having to do with the document containing the
    list of resolutions
    """

    def __init__(self, dao):
        self.config = Configuration()
        self.dao = dao
        self.cred_manager = CredentialsManager()
        self.service = build('docs', 'v1', credentials=self.cred_manager.creds)
        self.resolution_repo = ResolutionRepository(self.dao)
        self.plenary_repo = PlenaryRepository(self.dao)
        self.permission_repo = PermissionsRepository()
        self.document_repo = DocumentRepository()
        self.file_repo = FileRepository()

        self.idx = 1

        self.first_readings = []
        self.second_readings = []
        self.waivers = []

        self.logger = logging.getLogger(__name__)

    def clear_body_content(self, plenary):
        """
        Deletes all content from the body of the document
        :param plenary:
        :return:
        """
        document_obj = self.document_repo.get_document(plenary.agenda_id)

        # Get last body item
        final_index = document_obj['body']['content'][len(document_obj['body']['content']) - 2]['endIndex']

        requests = [
            RequestRepository.make_delete_content_request(1, final_index)
        ]

        # requests = [
        #     {
        #         'deleteContentRange': {
        #             'range': {'startIndex': 1, 'endIndex': final_index}
        #         }
        #     }
        # ]
        try:

            result = self.service.documents().batchUpdate(documentId=plenary.agenda_id,
                                                          body={'requests': requests}).execute()
        except HttpError as e:
            self.logger.warning(e)
            sys.stdout.write("{e}")
            print(e)

    def copy_template_file(self, plenary):
        """
        Creates a copy of the agenda template and moves it to appropriate folder.
        Sets the agenda_id on the plenary
        :return:
        """
        template_id = self.config.AGENDA_TEMPLATE_ID
        filename = Templates.AGENDA_FILENAME_TEMPLATE.format(plenary_name=plenary.plenary_folder_name)

        agenda_id = self.file_repo.copy_file(template_id, filename)
        self.file_repo.move_file_to_folder(agenda_id, plenary.plenary_folder_id)
        self.plenary_repo.update_agenda_id(plenary, agenda_id)
        return agenda_id

    def create_agenda_file(self, plenary: Plenary):
        """
        This creates a new agenda file if none already exists. If one does, it will
        wipe it clean
        :param plenary:
        :return:
        """
        if plenary.agenda_id is None:
            # No agenda document exists, so create one
            self.copy_template_file(plenary=plenary)
        else:
            # We already have one, so wipe it clean
            self.clear_body_content(plenary=plenary)

        # todo Decide whether want this once have everything working properly
        self.permission_repo.make_world_writeable(plenary.agenda_id)
        return plenary.agenda_id

    def make_first_readings_heading_requests(self):
        text = "\nFirst Readings \n"

        requests = [
            RequestRepository.make_insert_text_request(self.idx, text),
            RequestRepository.make_bold_text_request(self.idx, self.idx + len(text))
        ]
        # requests = []
        # requests.append({
        #     'insertText': {
        #         'location': {
        #             'index': self.idx,
        #         },
        #         'text': text,
        #     }
        # })
        # requests.append({
        #     'updateTextStyle': {
        #         'range': {
        #             'startIndex': self.idx,
        #             'endIndex': self.idx + len(text)
        #         },
        #         'textStyle': {
        #             'bold': True,
        #         },
        #         'fields': 'bold'
        #     }
        # })

        self.idx += len(text)
        return requests

    def make_page_title_requests(self, plenary: Plenary):
        text = f"ASCSU Resolutions\n {plenary.month} {plenary.year}\n\n"
        # text = template.format({'month': plenary.month, 'year': plenary.year})

        # text = template.format({'month': plenary.month, 'year': plenary.year})
        # text = "ASCSU Resolutions\n"

        requests = [
            RequestRepository.make_insert_text_request(self.idx, text),
            RequestRepository.make_title_style_request(self.idx, self.idx + len(text))
        ]

        # requests = [
        #     {
        #         'insertText': {
        #             'location': {
        #                 'index': self.idx,
        #             },
        #             'text': text,
        #         }
        #     },
        #     {
        #         'updateParagraphStyle': {
        #             'range': {
        #                 'startIndex': self.idx,
        #                 'endIndex': self.idx + len(text)
        #             },
        #             'paragraphStyle': {
        #                 'namedStyleType': 'TITLE'
        #             },
        #             'fields': 'namedStyleType'
        #         }
        #     },
        # {
        #     'updateTextStyle': {
        #         'range': {
        #             'startIndex': self.idx,
        #             'endIndex': self.idx + len(text)
        #         },
        #         'textStyle': {
        #             'bold': True,
        #         },
        #         'fields': 'bold'
        #     }
        # },
        # {
        #     'updateParagraphStyle': {
        #         'range': {
        #             'startIndex': self.idx,
        #             'endIndex': self.idx + len(text)
        #         },
        #         'paragraphStyle': {
        #             'alignment': 'CENTER'
        #         },
        #         'fields': 'alignment'
        #     }
        # }
        # ]

        self.idx += len(text)
        return requests

    def make_action_items_heading_requests(self):
        text = "\nAction Items \n"

        requests = [
            RequestRepository.make_insert_text_request(self.idx, text),
            RequestRepository.make_bold_text_request(self.idx, self.idx + len(text))
        ]

        # requests = []
        #
        #
        # requests.append({
        #     'insertText': {
        #         'location': {
        #             'index': self.idx,
        #         },
        #         'text': text,
        #     }
        # })
        # requests.append({
        #     'updateTextStyle': {
        #         'range': {
        #             'startIndex': self.idx,
        #             'endIndex': self.idx + len(text)
        #         },
        #         'textStyle': {
        #             'bold': True,
        #         },
        #         'fields': 'bold'
        #     }
        # })

        # requests.append({'updateParagraphStyle': {
        #     'range': {
        #         'startIndex': self.idx,
        #         'endIndex': self.idx + len(text)
        #     },
        #     'paragraphStyle': {
        #         'alignment': 'START'
        #     },
        #     'fields': 'alignment'
        # }
        # })

        self.idx += len(text)
        return requests

    def make_resolution_list_item_requests(self, resolution):
        """Returns a list of request objects required to make the entry"""
        starting_idx = self.idx

        requests = []

        # Add the resolution name and number
        text = f"{resolution.agenda_item} \n"

        requests.append(RequestRepository.make_insert_text_request(self.idx, text))
        requests.append(RequestRepository.make_align_left_request(self.idx, self.idx + len(text)))

        # requests.append({
        #     'insertText': {
        #         'location': {
        #             'index': self.idx,
        #         },
        #         'text': text,
        #     }
        # })
        #
        # requests.append({'updateParagraphStyle': {
        #     'range': {
        #         'startIndex': self.idx,
        #         'endIndex': self.idx + len(text)
        #     },
        #     'paragraphStyle': {
        #         'alignment': 'START'
        #     },
        #     'fields': 'alignment'
        # }
        # })

        self.idx += len(text)

        # Add url
        url_text = f"{resolution.url} \n\n"
        requests.append(RequestRepository.make_insert_text_request(self.idx, url_text))
        requests.append(RequestRepository.make_url_request(self.idx, self.idx + len(url_text), resolution.url))

        #
        # requests.append({
        #     'insertText': {
        #         'location': {
        #             'index': self.idx,
        #         },
        #         'text': url_text
        #     }
        # })
        #
        # requests.append(
        #     {
        #         "updateTextStyle": {
        #             "textStyle": {
        #                 "link": {
        #                     "url": resolution.url
        #                 }
        #             },
        #             "range": {
        #                 "startIndex": self.idx,
        #                 "endIndex": self.idx + len(url_text)
        #             },
        #             "fields": "link"
        #         }
        #     })

        self.idx += len(url_text)

        # Make sure it has the correct styling
        requests.append(RequestRepository.make_normal_text_style_request(starting_idx, self.idx))

        # requests.append({'updateParagraphStyle': {
        #     'range': {
        #         'startIndex': starting_idx,
        #         'endIndex': self.idx
        #     },
        #     'paragraphStyle': {
        #         'namedStyleType': 'NORMAL_TEXT'
        #     },
        #     'fields': 'namedStyleType'
        # }
        # })

        return requests

    def sort_resolutions(self, plenary: Plenary):
        """
        Populates the second_items, waivers, and first_readings lists
        :param plenary:
        :return:
        """
        resolutions = self.resolution_repo.load_all_resolutions_for_plenary(plenary)

        self.first_readings = [r for r in resolutions if r.is_first_reading is True and r.is_waiver is False]
        self.waivers = [r for r in resolutions if r.is_first_reading is True and r.is_waiver is True]
        self.second_readings = [r for r in resolutions if r.is_first_reading is not True]

    def make_resolution_list(self, plenary: Plenary):
        """
        MAIN CALLED METHOD

        Creates the Resolution list google doc for the plenary.

        :param plenary: Plenary
        :return:
        """
        logging.warning('make resolution list')
        # Populate the resolution lists
        self.sort_resolutions(plenary)

        # Creates a new agenda file or clears the content from the existing one
        self.create_agenda_file(plenary)

        # print(plenary.agenda_id)

        self.idx = 1
        requests = []

        pt = self.make_page_title_requests(plenary)
        requests.extend(pt)

        # Make action items header and update index
        aih = self.make_action_items_heading_requests()
        requests.extend(aih)

        for r in self.second_readings:
            try:
                sr = self.make_resolution_list_item_requests(r)
                requests.extend(sr)
            except Exception as e:
                self.logger.warning(e)

        for w in self.waivers:
            try:
                sr = self.make_resolution_list_item_requests(w)
                requests.extend(sr)
            except Exception as e:
                self.logger.warning(e)

        # Make first reading header and update index
        frh = self.make_first_readings_heading_requests()
        requests.extend(frh)

        for f in self.first_readings:
            try:
                fr = self.make_resolution_list_item_requests(f)

                # todo AR-69 problem was here with the first readings
                requests.extend(fr)
            except Exception as e:
                self.logger.warning(e)

        # print(requests)

        result = self.service.documents().batchUpdate(documentId=plenary.agenda_id,
                                                      body={'requests': requests}).execute()
