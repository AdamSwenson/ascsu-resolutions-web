import logging

from googleapiclient.discovery import build

from ResolutionManager.API.CredentialsManager import CredentialsManager
from ResolutionManager.Repositories.RequestRepository import RequestRepository
from ResolutionManager.config.Configuration import Configuration
from ResolutionManager.config.Templates import Templates
from ResolutionManager.Models.Resolutions import Resolution


# STANDARD_FONT = 'Atkinson Hyperlegible'
# STANDARD_FONT_SIZE = 12


class StylingRepository(object):

    def __init__(self):
        self.cred_manager = CredentialsManager()
        self.service = build('docs', 'v1', credentials=self.cred_manager.creds)
        self.config = Configuration()
        self.logger = logging.getLogger(__name__)

    # ======================== Utlities which make direct requests
    @staticmethod
    def is_excluded(paragraph, skip_list=[]):
        """
        Returns True if the text of the paragraph exactly matches something in the
        list.
        Returns False otherwise

        >>>p = {'startIndex': 1,
        'endIndex': 17,
        'paragraph':  {'elements': [{'startIndex': 1, 'endIndex': 17,
        'textRun': {'content': 'Academic Senate\n',
         'textStyle': {'fontSize': {'magnitude': 12, 'unit': 'PT'},
          'weightedFontFamily': {'fontFamily': 'Atkinson Hyperlegible',
           'weight': 400}}}}],
      'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT',
       'alignment': 'CENTER',
       'direction': 'LEFT_TO_RIGHT'}}}
       >>>assert(is_excluded(p, skip_list=[ 'Academic Senate\n']) is True)
       >>>assert(is_excluded(p, skip_list=[]) is False)
        """
        #     if len(skip_list) == 0: return false

        try:

            for k in paragraph['paragraph']['elements']:
                try:
                    if k['textRun']['content'] in skip_list:
                        return True
                except KeyError as e:
                    print(e, k)
        except KeyError as e:
            print(e)

        return False

    def double_space(self, document_id, list_of_indicies, revision_id=None):
        """
        Given a list of dictionaries
            [{'startIndex': 93, 'endIndex': 1290}]
        makes a request to set them as double spaced
        """
        requests = []

        for i in list_of_indicies:
            requests.append(RequestRepository.make_double_space_request(i['startIndex'], i['endIndex']))

        body = {'requests': requests}
        if revision_id is not None:
            # Lock to ensure that hasn't change since we fetched
            body['writeControl'] = {'requiredRevisionId': revision_id}

        self.service.documents().batchUpdate(
            documentId=document_id,
            body=body
        ).execute()

    def single_space(self, document_id, list_of_indicies, revision_id=None):
        """Given a list of dictionaries
            [{'startIndex': 93, 'endIndex': 1290}]
        makes a request to set them as single spaced
        """
        requests = []

        for i in list_of_indicies:
            requests.append(RequestRepository.make_single_space_request(i['startIndex'], i['endIndex']))

        body = {'requests': requests}
        if revision_id is not None:
            # Lock to ensure that hasn't change since we fetched
            body['writeControl'] = {'requiredRevisionId': revision_id}

        self.service.documents().batchUpdate(
            documentId=document_id,
            body={'requests': requests}
        ).execute()

    def force_font(self, document_id, list_of_indicies, revision_id=None):
        """
        Given a list of dictionaries
            [{'startIndex': 93, 'endIndex': 1290}]
        makes a request to set to the standard font
        """
        requests = []

        for i in list_of_indicies:
            requests.append({
                'updateTextStyle': {
                    'range': {
                        'startIndex': i['startIndex'],
                        'endIndex': i['endIndex']
                    },
                    'textStyle': {
                        'weightedFontFamily': {
                            'fontFamily': Templates.STANDARD_FONT

                        },
                        'fontSize': {
                            'magnitude': Templates.STANDARD_FONT_SIZE,
                            'unit': 'PT'
                        },
                    },
                    'fields': 'weightedFontFamily,fontSize'

                }
            })

        body = {'requests': requests}
        if revision_id is not None:
            # Lock to ensure that hasn't change since we fetched
            body['writeControl'] = {'requiredRevisionId': revision_id}

        self.service.documents().batchUpdate(
            documentId=document_id,
            body={'requests': requests}
        ).execute()

    def get_indicies_for_named_range(self, resolution: Resolution, range_name):
        """
        Returns a list of dictionaries of the start and end indicies for the
        named range
            e.g., [{'startIndex': 93, 'endIndex': 1290}]
        :param resolution: Resolution
        :param range_name: string Name of range
        :return: list
        """
        try:
            # Determine the length of the replacement text, as UTF-16 code units.
            # https://developers.google.com/docs/api/concepts/structure#start_and_end_index

            # Fetch the document to determine the current indexes of the named ranges.
            # We're going to do this de novo in case the resolution object may be out of date
            document = self.service.documents().get(documentId=resolution.document_id).execute()
            # Set it on the resolution just in case
            resolution.document_obj = document

            # Find the matching named ranges.
            named_range_list = document.get('namedRanges', {}).get(range_name)
            if not named_range_list:
                raise Exception('The named range is no longer present in the document.')

            # Determine all the ranges of text to be removed, and at which indices the
            # replacement text should be inserted.
            all_ranges = []
            # insert_at = {}
            for named_range in named_range_list.get('namedRanges'):
                ranges = named_range.get('ranges')
                all_ranges.extend(ranges)
                # Most named ranges only contain one range of text, but it's possible
                # for it to be split into multiple ranges by user edits in the document.
                # The replacement text should only be inserted at the start of the first
                # range.
                # insert_at[ranges[0].get('startIndex')] = True

            # Sort the list of ranges by startIndex, in descending order.
            all_ranges.sort(key=lambda r: r.get('startIndex'), reverse=True)
            return all_ranges
        except Exception as e:
            self.logger.warning(e)

    #  ======================== Requests covering parts of resolution

    def single_space_group_name(self, resolution: Resolution):
        """Make the 'Academic senate of the the CSU' single spaced"""
        # Determine the length of the replacement text, as UTF-16 code units.
        # https://developers.google.com/docs/api/concepts/structure#start_and_end_index

        ranges = self.get_indicies_for_named_range(resolution, range_name=self.config.GROUP_TITLE_RANGE_NAME)
        self.single_space(resolution.document_id, ranges)

    def double_space_resolution(self, resolution: Resolution):
        """Forces resolution body to be double spaced"""
        title_range = self.get_indicies_for_named_range(resolution, self.config.TITLE_RANGE_NAME)
        distribution_range = self.get_indicies_for_named_range(resolution, self.config.DISTRIBUTION_LIST_RANGE_NAME)
        title_end = title_range[-1:][0]['endIndex'] + 1
        distribution_start = distribution_range[0]['startIndex'] - 1
        rng = [{'startIndex': title_end, 'endIndex': distribution_start}]
        print("Double spacing range: ", rng)

        self.double_space(resolution.document_id, rng)

    def force_font_on_resolution(self, resolution: Resolution):
        """Makes the whole resolution body have the standard font"""
        idx = [{'startIndex': 1, 'endIndex': resolution.end_index}]
        self.force_font(resolution.document_id, idx)

    def single_space_distribution_list(self, resolution: Resolution):
        """Makes the resolution's distribution list single spaced"""
        ranges = self.get_indicies_for_named_range(resolution, range_name=self.config.DISTRIBUTION_LIST_RANGE_NAME)
        self.single_space(resolution.document_id, ranges)

    def enforce_styling_on_body(self, resolution: Resolution):
        """
        Main called method

        Enforces: font on entire resolution, line spacing of document and componsnets

        :param resolution: Resolution
        :return:
        """
        # document = self.get_document(resolution.document_id)
        # startIndex = 1
        # endIndex = self.get_end_index(document)

        # self.style_repo.force_font(resolution, startIndex, endIndex)
        self.force_font_on_resolution(resolution)
        self.double_space_resolution(resolution)
        self.single_space_distribution_list(resolution)
        self.single_space_group_name(resolution)

    def enforce_styling_on_title(self, resolution: Resolution, revision_id=None):
        """
        Ensures title is:
            Single spaced
            Bold
            todo Title cased

        @ticket: AR-38

        todo It does not seem possible to force to title case
        """
        title_range = self.get_indicies_for_named_range(resolution, self.config.TITLE_RANGE_NAME)
        requests = []
        for i in title_range:
            requests.append(RequestRepository.make_single_space_request(i['startIndex'], i['endIndex']))
            requests.append(RequestRepository.make_bold_text_request(i['startIndex'], i['endIndex']))

        body = {'requests': requests}
        if revision_id is not None:
            # Lock to ensure that hasn't change since we fetched
            body['writeControl'] = {'requiredRevisionId': revision_id}

        self.service.documents().batchUpdate(
            documentId=resolution.document_id,
            body=body
        ).execute()

    def enforce_styling_on_resolution(self, resolution):
        self.enforce_styling_on_body(resolution)
        self.enforce_styling_on_title(resolution)

    #
    # def double_space(self, resolution, paragraph, skip_text=[]):
    #     """"
    #     todo: Revise this so it only makes one batched request to avoid quota limits
    #
    #     Makes the paragraph double spaced
    #     Paragraph should be:
    #        {'startIndex': 1,
    #         'endIndex': 17,
    #         'paragraph': {
    #             'elements': [
    #                 {'startIndex': 1,
    #                     'endIndex': 17,
    #                     'textRun': {'content': 'Academic Senate\n',
    #                     'textStyle': {'fontSize': {'magnitude': 12, 'unit': 'PT'},
    #                     'weightedFontFamily': {'fontFamily': 'Atkinson Hyperlegible',
    #                     'weight': 400}}
    #                     }
    #                     }
    #                     ],
    #          'paragraphStyle': {'namedStyleType': 'NORMAL_TEXT',
    #           'alignment': 'CENTER',
    #           'direction': 'LEFT_TO_RIGHT'}}},
    #
    #
    #     :argument skip_text List of strings that if exactly matches the text, will prevent text from being double-spaced.
    #     """
    #     # Don't process if exactly matches text to skip
    #     if self.is_excluded(paragraph, skip_text): return True
    #
    #     requests = [
    #         {
    #             'updateParagraphStyle': {
    #                 'range': {
    #                     'startIndex': paragraph['startIndex'],
    #                     'endIndex': paragraph['endIndex']
    #                 },
    #                 'paragraphStyle': {
    #                     'lineSpacing' : 200
    #                 },
    #                 'fields': 'lineSpacing'
    #             }
    #         },
    #
    #     ]
    #
    #     self.service.documents().batchUpdate(
    #         documentId=resolution.document_id, body={'requests': requests}).execute()
