from unittest import TestCase
from unittest.mock import MagicMock
from random import shuffle
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Models.Resolutions import Resolution
from ResolutionManager.Repositories.AgendaRepository import AgendaRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from helpers.Factories import plenary_factory, resolution_factory, waiver_factory, first_reading_factory, \
    second_reading_factory


class TestAgendaRepository(TestCase):
    def setUp(self):
        self.waivers = [waiver_factory() for i in range(1, 10)]
        self.first_readings = [first_reading_factory() for i in range(1, 10)]
        self.second_readings = [second_reading_factory() for i in range(1, 10)]
        self.resolutions = self.waivers + self.first_readings + self.second_readings
        shuffle(self.resolutions)
        self.dao = {}
        resolution_repo = ResolutionRepository(dao=self.dao)
        resolution_repo.load_all_resolutions_for_plenary = MagicMock(return_value=self.resolutions)

        self.agenda_repo = AgendaRepository(self.dao)
        self.agenda_repo.resolution_repo = resolution_repo
        self.plenary = plenary_factory()

    def test_check_setup(self):
        self.assertIsInstance(self.agenda_repo, AgendaRepository)
        # waivers = [resolution_factory() for i in range(1, 10)]
        for w in self.waivers:
            self.assertIsInstance(w, Resolution)
            self.assertIs(w.is_waiver, True)

    def test_clear_body_content(self):
        self.fail()

    def test_copy_template_file(self):
        self.fail()

    def test_create_agenda_file(self):
        self.fail()

    def test_make_first_readings_heading_requests(self):
        self.fail()

    def test_make_page_title_requests(self):
        self.fail()

    def test_make_action_items_heading_requests(self):
        self.fail()

    def test_make_resolution_list_item_requests(self):
        self.fail()

    def test_sort_resolutions(self):
        rs = self.agenda_repo.sort_resolutions(self.plenary)
        [self.assertIsInstance(r, Resolution) for r in self.agenda_repo.waivers]
        [self.assertIsInstance(r, Resolution) for r in self.agenda_repo.first_readings]
        [self.assertIsInstance(r, Resolution) for r in self.agenda_repo.second_readings]

        for r in self.agenda_repo.waivers:
            self.assertIsInstance(r, Resolution)
            self.assertIs(r.is_waiver, True)
            self.assertIs(r.is_first_reading, True)
            self.assertIs(r.is_action, False)

        for r in self.agenda_repo.first_readings:
            self.assertIsInstance(r, Resolution)
            self.assertIs(r.is_waiver, False)
            self.assertIs(r.is_first_reading, True)
            self.assertIs(r.is_action, False)

        for r in self.agenda_repo.second_readings:
            self.assertIsInstance(r, Resolution)
            self.assertIs(r.is_waiver, False)
            self.assertIs(r.is_first_reading, False)
            self.assertIs(r.is_action, True)


    def test_make_resolution_list(self):
        self.fail()
