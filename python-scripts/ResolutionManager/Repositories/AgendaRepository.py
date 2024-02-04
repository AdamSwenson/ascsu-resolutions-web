import sys

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
            {
                'deleteContentRange': {
                    'range': {'startIndex': 1, 'endIndex': final_index}
                }
            }
        ]
        try:

            result = self.service.documents().batchUpdate(documentId=plenary.agenda_id,
                                                          body={'requests': requests}).execute()
        except HttpError as e:
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

    def make_page_title_requests(self, plenary: Plenary):
        text = f"ASCSU Resolutions\n {plenary.month} {plenary.year}\n\n"
        # text = template.format({'month': plenary.month, 'year': plenary.year})

        # text = template.format({'month': plenary.month, 'year': plenary.year})
        # text = "ASCSU Resolutions\n"

        requests = [{
            'insertText': {
                'location': {
                    'index': self.idx,
                },
                'text': text,
            }
        },
        {'updateParagraphStyle': {
                'range': {
                    'startIndex': self.idx,
                    'endIndex': self.idx + len(text)
                },
                'paragraphStyle': {
                    'namedStyleType': 'TITLE'
                },
                'fields': 'namedStyleType'
            }
            },
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
        ]

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
        text = f"{resolution.agenda_item} \n"
        requests.append({
            'insertText': {
                'location': {
                    'index': self.idx,
                },
                'text': text,
            }
        })

        requests.append({'updateParagraphStyle': {
            'range': {
                'startIndex': self.idx,
                'endIndex': self.idx + len(text)
            },
            'paragraphStyle': {
                'alignment': 'START'
            },
            'fields': 'alignment'
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

        requests.append({'updateParagraphStyle': {
            'range': {
                'startIndex': starting_idx,
                'endIndex': self.idx
            },
            'paragraphStyle': {
                'namedStyleType': 'NORMAL_TEXT'
            },
            'fields': 'namedStyleType'
        }
        })

        return requests

    def make_resolution_list(self, plenary: Plenary):
        """
        MAIN CALLED METHOD

        Creates the Resolution list google doc for the plenary.

        :param plenary: Plenary
        :return:
        """
        # Get all resolutions
        # For now not going to sync the database, just use title from drive if can be retrieved and default to db version
        resolutions = self.resolution_repo.load_all_resolutions_for_plenary(plenary)

        # resolutions = self.resolution_repo.load_all_resolutions()
        first_readings = [r for r in resolutions if r.is_first_reading is True and r.is_waiver is False]
        # todo Once figure out how committees indicate ready for second reading, remove waiver check
        waivers = [r for r in resolutions if r.is_first_reading is True and r.is_waiver is True]
        second_readings = [r for r in resolutions if r.is_first_reading is not True]

        # Creates a new agenda file or clears the content from the existing one
        self.create_agenda_file(plenary)

        print(plenary.agenda_id)

        self.idx = 1
        requests = []

        pt = self.make_page_title_requests(plenary)
        requests.extend(pt)

        # Make action items header and update index
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
            except Exception as e:
                print(e)
                pass

        # Make first reading header and update index
        frh = self.make_first_readings_heading_requests()
        requests.extend(frh)

        for f in first_readings:
            try:
                fr = self.make_resolution_list_item_requests(f)

                # todo AR-69 problem was here with the first readings
                requests.extend(fr)
            except Exception as e:
                print(e)
                pass

        print(requests)

        result = self.service.documents().batchUpdate(documentId=plenary.agenda_id,
                                                      body={'requests': requests}).execute()
