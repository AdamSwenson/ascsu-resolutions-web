import sys


sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
sys.path.append("/")

from ResolutionManager.Repositories.ErrorHandlingRepository import ErrorHandlingRepository

import unittest


class MyTestCase(unittest.TestCase):
    def test_token_path(self):
        error_repo = ErrorHandlingRepository()

        # todo If used this needs to be generalized
        expect = "/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts/tests/private/token.json"

        self.assertEqual(expect, error_repo.token_path)


if __name__ == '__main__':
    unittest.main()
