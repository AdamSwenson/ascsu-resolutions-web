import sys
from unittest.mock import MagicMock

sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
sys.path.append("/")
import unittest
from googleapiclient.discovery import build
from googleapiclient.http import HttpMock
import pprint

from ResolutionManager.Repositories.FileRepository import FileRepository


class FileRepositoryTest(unittest.TestCase):
    """"
    Tests for FileRepository

    See this for mocks: https://github.com/googleapis/google-api-python-client/blob/main/docs/mocks.md
    """


    def test_create_folder(self):
        pass
        # frepo = FileRepository()
        # http = HttpMock('../mock-responses/mock-file-response.json', {'status': '200'})
        # api_key = 'your_api_key'
        # frepo.service = build('drive', 'v3', http=http, developerKey=api_key)
        #
        # result = frepo.create_folder('taco')
        # self.assertEqual(result, "x100b")

    def test_copy_file(self):
        frepo = FileRepository()
        fileid = "1RvAyHak38xQC3jqoIJPXY4ZmKPLqktMv2LibdoenH5w"

        copy_id = frepo.copy_file(fileid, 'copied_file')
        self.assertIsNotNone(copy_id)
        print(copy_id)

if __name__ == '__main__':
    unittest.main()
