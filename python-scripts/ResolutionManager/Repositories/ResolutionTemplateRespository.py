# import ResolutionManager.environment as env
from ResolutionManager.config.Configuration import Configuration
from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.API.CredentialsManager import CredentialsManager
from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository
from ResolutionManager.Models.Resolutions import Resolution
from ResolutionManager.config.Templates import Templates

import sys
from googleapiclient.discovery import build


# HEADER_TEMPLATE = "AS-{resolution_number}-{year}/{committee}"

class ResolutionTemplateRepository(object):

    APPROVED_TEXT = "\nApproved"
    """The text inserted into the header of approved resolutions"""

    def __init__(self, plenary=None, dao=None):
        self.config = Configuration()
        self.dao = dao
        self.plenary = plenary
        self.doc_repo = DocumentRepository()
        self.file_repo = FileRepository()
        self.cred_manager = CredentialsManager()
        self.resolution_repo = ResolutionRepository(dao)
        self.committee_repo = CommitteeRepository(dao)

        self.service = build('docs', 'v1', credentials=self.cred_manager.creds)

    def replace_named_title_range(self, document_id, new_text):
        """Replaces the text in existing named ranges."""

        # Determine the length of the replacement text, as UTF-16 code units.
        # https://developers.google.com/docs/api/concepts/structure#start_and_end_index
        new_text_len = len(new_text.encode('utf-16-le')) / 2

        # Fetch the document to determine the current indexes of the named ranges.
        document = self.service.documents().get(documentId=document_id).execute()

        # Find the matching named ranges.
        named_range_list = document.get('namedRanges', {}).get(self.config.TITLE_RANGE_NAME)
        if not named_range_list:
            raise Exception('The named range is no longer present in the document.')

        # Determine all the ranges of text to be removed, and at which indices the
        # replacement text should be inserted.
        all_ranges = []
        insert_at = {}
        for named_range in named_range_list.get('namedRanges'):
            ranges = named_range.get('ranges')
            all_ranges.extend(ranges)
            # Most named ranges only contain one range of text, but it's possible
            # for it to be split into multiple ranges by user edits in the document.
            # The replacement text should only be inserted at the start of the first
            # range.
            insert_at[ranges[0].get('startIndex')] = True

        # Sort the list of ranges by startIndex, in descending order.
        all_ranges.sort(key=lambda r: r.get('startIndex'), reverse=True)

        # Create a sequence of requests for each range.
        requests = []
        for r in all_ranges:
            # Delete all the content in the existing range.
            requests.append({
                'deleteContentRange': {
                    'range': r
                }
            })

            segment_id = r.get('segmentId')
            start = r.get('startIndex')
            if insert_at[start]:
                # Insert the replacement text.
                requests.append({
                    'insertText': {
                        'location': {
                            'segmentId': segment_id,
                            'index': start
                        },
                        'text': new_text
                    }
                })
                # Re-create the named range on the new text.
                requests.append({
                    'createNamedRange': {
                        'name': self.config.TITLE_RANGE_NAME,
                        'range': {
                            'segmentId': segment_id,
                            'startIndex': start,
                            'endIndex': start + new_text_len
                        }
                    }
                })
                # Center again
                requests.append(
                    {
                        'updateParagraphStyle': {
                            'range': {
                                'startIndex': start,
                                'endIndex': start + new_text_len
                            },
                            'paragraphStyle': {
                                'alignment': 'CENTER'
                            },
                            'fields': 'alignment'
                        }
                    })

        # Make a batchUpdate request to apply the changes, ensuring the document
        # hasn't changed since we fetched it.
        body = {
            'requests': requests,
            'writeControl': {
                'requiredRevisionId': document.get('revisionId')
            }
        }
        result = self.service.documents().batchUpdate(documentId=document_id, body=body).execute()

    def update_title_new(self, resolution: Resolution):
        return self.replace_named_title_range(resolution.document_id, resolution.title)

    def create_file_from_template(self, resolution: Resolution, template_id=None):
        if template_id is None:
            template_id = self.config.TEMPLATE_DOCUMENT_ID
        # def create_file_from_template(self, folder_id, resolution_number, resolution_name,
        #                               template_id=env.TEMPLATE_DOCUMENT_ID):

        sponsor = self.committee_repo.load_sponsor(resolution_id=resolution.id)
        """Uses the template to make a new resolution in the first readings folder
        returns Resolution object with document id of created resolution set
        """
        filename = Templates.RESOLUTION_FILENAME_TEMPLATE.format(resolution_number=resolution.number,
                                                                 resolution_name=resolution.title,
                                                                 committee_abbrev=sponsor.abbreviation)
        sys.stdout.write(f"{resolution.__dict__}")

        resolution.document_id = self.file_repo.copy_file(template_id, filename)
        self.resolution_repo.set_google_document_id(resolution, resolution.document_id)

        self.file_repo.move_file_to_folder(resolution.document_id, self.plenary.first_reading_folder_id)
        return resolution

    def make_header(self, resolution: Resolution):
        """
        Makes the string to be added to the document header
            AS-xxxx-yy
            1-2 September 2023
            Approved [if approved]

        :param resolution:
        :return:
        """
        # def make_header(self, resolution_number, year, committee, cosponsors=[]):

        # if self.plenary.year > 2000:
        #     self.plenary.year = self.plenary.year - 2000

        v = Templates.HEADER_TEMPLATE.format(resolution_number=resolution.number,
                                             year=self.plenary.two_digit_year,
                                             committee=resolution.committee.abbreviation)
        if len(resolution.cosponsors) > 0:
            for c in resolution.cosponsors:
                v += f"/{c.abbreviation}"

        v += f"\n{self.plenary.formatted_plenary_date}"

        return v

    def update_header(self, resolution):
        """Adds the header text with proper formatting to the document"""
        # def update_header(self, document_id, resolution_number, committee, cosponsors=[]):
        # txt = f"{self.make_header(resolution)}\n{self.plenary.formatted_plenary_date}"
        # txt = f"{self.make_header(resolution.number, self.plenary.year, resolution.committee, resolution.cosponsors)}\n{self.plenary.formatted_plenary_date()}"

        txt = self.make_header(resolution)
        # sys.stdout.write(f"{resolution.__dict__}")
        # sys.stdout.write(f"{txt}")

        requests = [
            {
                "insertText": {
                    "location": {
                        "segmentId": self.config.TEMPLATE_HEADER_ID,
                        "index": 0
                    },
                    "text": txt
                }
            },

            # Force header to correct format
            {
                'updateTextStyle': {

                    'range': {
                        'segmentId': self.config.TEMPLATE_HEADER_ID,
                        'startIndex': 0,
                        'endIndex': len(txt)
                    },
                    'textStyle': {
                        'weightedFontFamily': {
                            'fontFamily': 'Atkinson Hyperlegible'

                        },
                        'fontSize': {
                            'magnitude': 12,
                            'unit': 'PT'
                        },
                    },
                    'fields': 'weightedFontFamily,fontSize'
                }
            },

        ]

        result = self.service.documents().batchUpdate(
            documentId=resolution.document_id, body={'requests': requests}).execute()

        # print(result)

    def add_approved(self, resolution):
        # txt = "\nApproved"
        existing = self.make_header(resolution)
        insertStart = len(existing) +1

        requests = [
            {
                "insertText": {
                    "location": {
                        "segmentId": self.config.TEMPLATE_HEADER_ID,
                        "index": insertStart
                    },
                    "text": self.APPROVED_TEXT
                }
            },

            # Force header to correct format
            {
                'updateTextStyle': {

                    'range': {
                        'segmentId': self.config.TEMPLATE_HEADER_ID,
                        'startIndex': insertStart,
                        'endIndex': insertStart + len(self.APPROVED_TEXT)
                    },
                    'textStyle': {
                        'weightedFontFamily': {
                            'fontFamily': 'Atkinson Hyperlegible'

                        },
                        'fontSize': {
                            'magnitude': 12,
                            'unit': 'PT'
                        },
                    },
                    'fields': 'weightedFontFamily,fontSize'
                }
            },

        ]
        result = self.service.documents().batchUpdate(
            documentId=resolution.document_id, body={'requests': requests}).execute()

        return result

    def remove_approved(self, resolution):
        # txt = "\nApproved"
        existing = self.make_header(resolution)
        deleteStart = len(existing) + 1

        requests = [
            {
                'deleteContentRange': {
                    'range': {
                        'segmentId': self.config.TEMPLATE_HEADER_ID,
                        'startIndex': deleteStart,
                        'endIndex': deleteStart + len(self.APPROVED_TEXT),
                    }

                }
            },
        ]

        result = self.service.documents().batchUpdate(
            documentId=resolution.document_id, body={'requests': requests}).execute()
        return result

        # def update_title(self, resolution):
    #     # def update_title(self, document_id, title):
    #     title_idxs = {'start_index': 54, 'end_index': 62}
    #     rez_number = {'start_index': 54, 'end_index': 62}
    #
    #     title_start = title_idxs['start_index'] - 1
    #     title_end = title_idxs['start_index'] + len(resolution.title)
    #
    #     # Make sure to order backwards so offsets don't change
    #     requests = [
    #         {
    #             'insertText': {
    #                 'location': {
    #                     'index': title_start,
    #                 },
    #                 'text': resolution.title
    #             }
    #         },
    #
    #         {
    #             'updateTextStyle': {
    #                 'range': {
    #                     'startIndex': title_start,
    #                     'endIndex': title_end
    #                 },
    #                 'textStyle': {
    #                     'bold': True,
    #                 },
    #                 'fields': 'bold,'
    #             }
    #         },
    #         {
    #             'updateParagraphStyle': {
    #                 'range': {
    #                     'startIndex': title_start,
    #                     'endIndex': title_end
    #                 },
    #                 'paragraphStyle': {
    #                     'alignment': 'CENTER'
    #                 },
    #                 'fields': 'alignment'
    #             }
    #         },
    #
    #         {
    #             'deleteContentRange': {
    #                 'range': {
    #                     'startIndex': title_end,
    #                     'endIndex': title_end + 1 + len('[Title]'),
    #                 }
    #             }},
    #
    #     ]
    #
    #     result = self.service.documents().batchUpdate(
    #         documentId=resolution.document_id, body={'requests': requests}).execute()
    #
    #     return result
