from unittest import TestCase
from unittest.mock import MagicMock

from ResolutionManager.DAO.DAO import MySqlDao
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from ResolutionManager.config.Configuration import Configuration
from TestingParent import TestingParent
from helpers.Factories import plenary_factory, resolution_factory
from helpers.FakeItems import get_test_plenary


class ResolutionRepositoryTest(TestingParent):

    def setUp(self):
        self.initialize()
        self.dao = MagicMock()


        self.obj = ResolutionRepository(self.dao)
        self.plenary = plenary_factory()


    def test_set_as_working_item_w_live_drive(self):
        """This runs sync on the test plenary in the drive."""
        config = Configuration()
        dao = MySqlDao()

        plenary = get_test_plenary()
        obj = ResolutionRepository(dao)
        resolution = resolution_factory()

        # obj.set_as_working_item(plenary, resolution)


    def test_set_as_working_item(self):
        self.fail()
