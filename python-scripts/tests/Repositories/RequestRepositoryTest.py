from unittest import TestCase

from ResolutionManager.Repositories.RequestRepository import RequestRepository


class RequestRepositoryTest(TestCase):
    def test_make_input_text_request(self):
        r = RequestRepository.make_insert_text_request(2, 'taco')
        expect = {
            'insertText': {
                'location': {
                    'index': 2,
                },
                'text': 'taco',
            }
        }
        self.assertEqual(r, expect)


    def test_make_insert_text_request_with_segment_id(self):
        r = RequestRepository.make_insert_text_request(2, 'taco', segmentId=1)
        expect = {
            'insertText': {
                'location': {
                    'segmentId' : 1,
                    'index': 2,
                },
                'text': 'taco',
            }
        }
        self.assertEqual(r, expect)

