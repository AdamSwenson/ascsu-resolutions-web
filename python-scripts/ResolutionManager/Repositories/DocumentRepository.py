from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from ResolutionManager.API.CredentialsManager import CredentialsManager
from ResolutionManager.Repositories.StylingRepository import StylingRepository

# The ID of a sample document.
DOCUMENT_ID = '195j9eDD3ccgjQRttHhJPymLJUCOUjs-jmwTrekvdjFE'


class DocumentRepository(object):

    def __init__(self):
        self.cred_manager = CredentialsManager()
        try:
            self.service = build('docs', 'v1', credentials=self.cred_manager.creds)
        except Exception as e:
            print(e)
        self.style_repo = StylingRepository()

    def create_file(self, filename):
        """Shows basic usage of the Docs API.
        Prints the title of a sample document.
        """

        try:
            # service = build('docs', 'v1', credentials=self.cred_manager.creds)

            # Retrieve the documents contents from the Docs service.
            document = self.service.documents().get(documentId=DOCUMENT_ID).execute()

            print('The title of the document is: {}'.format(document.get('title')))

            title = filename
            body = {
                'title': title
            }
            doc = self.service.documents() \
                .create(body=body).execute()

            doc_id = doc.get('documentId')

            print('Created document with title: {0}'.format(
                doc.get('title')))
            print(f"Doc id {doc_id}")
            return doc_id

        except HttpError as err:
            print(err)


    def create_file_in_folder(self, folder_id, filename):
        """Upload a file to the specified folder and prints file ID, folder ID
        Args: Id of the folder
        Returns: ID of the file uploaded
        """

        try:
            file_metadata = {
                'name': filename,
                'parents': [folder_id]
            }
            # media = MediaFileUpload('download.jpeg',
            #                         mimetype='image/jpeg', resumable=True)
            # pylint: disable=maybe-no-member
            file = self.service.files().create(body=file_metadata, fields='id').execute()
            # file = self.service.files().create(body=file_metadata, media_body=media,
            #                               fields='id').execute()
            print(F'File ID: "{file.get("id")}".')
            return file.get('id')

        except HttpError as error:
            print(F'An error occurred: {error}')
            return None

    def get_document(self, document_id):
        """Returns the object for the document"""
        try:
            document = self.service.documents().get(documentId=document_id).execute()
            return document
        except HttpError as err:
            print(err)

    def get_end_index(self, document):
        """
        :deprecated This can be handled directly on the resolution object
        :param document:
        :return:
        """
        body = document.get('body').get('content')
        return body[len(body) - 1]['endIndex']


        # requests = [
        #     # Set body to Atkinson Hyperlegible
        #     {
        #     'updateTextStyle': {
        #         'range': {
        #             'startIndex': startIndex,
        #             'endIndex': endIndex
        #         },
        #         'textStyle': {
        #             'weightedFontFamily': {
        #                 'fontFamily': 'Atkinson Hyperlegible'
        #
        #             },
        #             'fontSize': {
        #                 'magnitude': 12,
        #                 'unit': 'PT'
        #             },
        #         },
        #         'fields': 'weightedFontFamily,fontSize'
        #
        #     }
        # },
        #
        # ]
        #
        # self.service.documents().batchUpdate(
        #     documentId=resolution.document_id, body={'requests': requests}).execute()


        #
        # document = self.get_document(resolution.document_id)
        # startIndex = 1
        # endIndex = self.get_end_index(document)
        # requests = [
        #     # Set body to Atkinson Hyperlegible
        #     {
        #     'updateTextStyle': {
        #         'range': {
        #             'startIndex': startIndex,
        #             'endIndex': endIndex
        #         },
        #         'textStyle': {
        #             'weightedFontFamily': {
        #                 'fontFamily': 'Atkinson Hyperlegible'
        #
        #             },
        #             'fontSize': {
        #                 'magnitude': 12,
        #                 'unit': 'PT'
        #             },
        #         },
        #         'fields': 'weightedFontFamily,fontSize'
        #
        #     }
        # },
        #
        #     #
        # ]
        #
        # self.service.documents().batchUpdate(
        #     documentId=resolution.document_id, body={'requests': requests}).execute()


if __name__ == '__main__':
    pass
    # create_file('test5')
