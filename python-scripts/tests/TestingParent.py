from unittest import TestCase

from googleapiclient.http import HttpMock
from googleapiclient.discovery import build


class TestingParent(TestCase):

    def initialize(self) -> None:
        self.http = HttpMock('mock-responses/mock-file-response.json', {'status': '200'})
        api_key = 'your_api_key'
        self.service_mock = build('drive', 'v3', http=self.http, developerKey=api_key)
