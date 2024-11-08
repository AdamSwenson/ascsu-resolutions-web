# import sys
# sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/ResolutionManager")
# sys.path.append("/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts")
# sys.path.append("/")

from unittest import TestCase

from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Models.Resolutions import Resolution
from ResolutionManager.Repositories.SyncRepository import SyncRepository
from helpers.Factories import plenary_factory, resolution_factory


class SyncRepositoryTest(TestCase):

    def setUp(self):
        self.dao = {}
        self.obj = SyncRepository(self.dao)
        self.plenary = plenary_factory()


    def test__search_plenary_resolutions(self):

        self.assertTrue(True)

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
