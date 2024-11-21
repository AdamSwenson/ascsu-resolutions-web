import sys


sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
sys.path.append("/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts")
import unittest
from googleapiclient.discovery import build
from googleapiclient.http import HttpMock
import pprint

from ResolutionManager.Repositories.FileRepository import FileRepository

class MyTestCase(unittest.TestCase):
    """"
    This is here to try to figure out how to test interacting with the
    api
    """

    def test_filerepo(self):
        frepo = FileRepository()
        http = HttpMock('mock-responses/mock-file-response.json', {'status': '200'})
        api_key = 'your_api_key'
        frepo.service = build('drive', 'v3', http=http, developerKey=api_key)

        result = frepo.create_folder('taco')
        self.assertEqual(result, "x100b")


    def test_something(self):
        """
        See this for mocks: https://github.com/googleapis/google-api-python-client/blob/main/docs/mocks.md
        :return:
        """

        http = HttpMock('mock-responses/mock-document-response.json', {'status': '200'})
        api_key = 'your_api_key'
        service = build('books', 'v1', http=http, developerKey=api_key)
        request = service.volumes().list(source='public', q='android')
        # http = HttpMock('books-android.json', {'status': '200'})
        response = request.execute(http=http)
        pprint.pprint(response)
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
