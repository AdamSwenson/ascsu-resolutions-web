# import sys
# sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
# sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
# sys.path.append("/")

from unittest import TestCase
from unittest.mock import MagicMock

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Models.Resolutions import Resolution
from ResolutionManager.Repositories.SyncRepository import SyncRepository
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.config.Configuration import Configuration

from TestingParent import TestingParent

from helpers.Factories import plenary_factory, resolution_factory
from helpers.FakeItems import get_test_plenary


class SyncRepositoryTest(TestingParent):

    def setUp(self):
        self.initialize()
        self.dao = MagicMock()

        self.file_repo = MagicMock(FileRepository)
        self.resolution_repo = MagicMock(ResolutionRepository)

        self.obj = SyncRepository(self.dao)
        self.plenary = plenary_factory()

        self.original_ids = {
            'first': [1, 2, 3],
            'waiver': [4, 5],
            'working': [6, 7, 8],
            'action': [9, 10]
        }

        self.changed_ids = {
            'first': [9, 10],
            'waiver': [1, 2],
            'working': [3, 4, 5],
            'action': [6, 7]
        }

    def test_sync_w_live_drive(self):
        """This runs sync on the test plenary in the drive."""
        config = Configuration()
        dao = MySqlDao()

        plenary = get_test_plenary()
        obj = SyncRepository(dao)
        obj.sync(plenary)

    def test__search_plenary_resolutions(self):
        res = [resolution_factory() for i in range(0,5)]
        self.obj.db_plenary_resolutions = res

        for r in res:
            f = self.obj._search_plenary_resolutions(r.document_id)
            self.assertIsNotNone(f)
            self.assertEquals(r.id, f.id, "Found correct resolution")

        n = resolution_factory()
        self.assertIsNone(self.obj._search_plenary_resolutions(n.document_id))

    def test__find_deleted_resolutions(self):
        all_resolutions = [resolution_factory() for i in range(0, 5)]
        self.obj.db_plenary_resolutions = all_resolutions[1:]
        self.fail()

    def test__find_resolutions_to_update_to_action(self):
        self.fail()

    def test__find_resolutions_to_update_to_first(self):
        self.fail()

    def test__find_resolutions_to_update_to_working(self):
        self.fail()

    def test__sync_action_resolutions(self):
        self.fail()

    def test__sync_first_resolutions(self):
        self.fail()

    def test__sync_working_resolutions(self):
        self.fail()
