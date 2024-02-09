from unittest import TestCase
from unittest.mock import MagicMock
from random import shuffle
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Models.Resolutions import Resolution
from ResolutionManager.Repositories.AgendaRepository import AgendaRepository
from ResolutionManager.Repositories.RequestRepository import RequestRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository
from helpers.Factories import plenary_factory, resolution_factory, waiver_factory, first_reading_factory, \
    second_reading_factory


class AgendaRepositoryTest(TestCase):
    def setUp(self):
        self.dao = {}
        self.agenda_repo = AgendaRepository(self.dao)
        self.plenary = plenary_factory()

    def prep_complete_lists(self):
        """Populates resolution repo with first, second, and waiver resolutions"""
        self.waivers = [waiver_factory() for i in range(1, 10)]
        self.first_readings = [first_reading_factory() for i in range(1, 10)]
        self.second_readings = [second_reading_factory() for i in range(1, 10)]
        self.resolutions = self.waivers + self.first_readings + self.second_readings
        shuffle(self.resolutions)

        resolution_repo = ResolutionRepository(dao=self.dao)
        resolution_repo.load_all_resolutions_for_plenary = MagicMock(return_value=self.resolutions)
        self.agenda_repo.resolution_repo = resolution_repo

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
        """This is brittle and only helpful for making sure the request repo behaves as expected"""
        text = "\nAction Items \n"
        expect = [
            RequestRepository.make_insert_text_request(1, text),
            RequestRepository.make_bold_text_request(1, 1 + len(text))
        ]
        result = self.agenda_repo.make_action_items_heading_requests()
        self.assertEquals(expect, result)

    def test_make_resolution_list_item_requests(self):
        self.fail()

    def test_sort_resolutions(self):
        self.prep_complete_lists()
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

    def test_sort_resolutions_if_no_second_readings_AR85(self):
        self.waivers = [waiver_factory() for i in range(1, 10)]
        self.second_readings = []
        self.first_readings = [first_reading_factory() for i in range(1, 10)]
        self.resolutions = self.waivers + self.first_readings + self.second_readings
        shuffle(self.resolutions)

        resolution_repo = ResolutionRepository(dao=self.dao)
        resolution_repo.load_all_resolutions_for_plenary = MagicMock(return_value=self.resolutions)
        self.agenda_repo.resolution_repo = resolution_repo

        rs = self.agenda_repo.sort_resolutions(self.plenary)
        self.assertEqual(len(self.agenda_repo.second_readings), 0, "second readings are empty")
        [self.assertIsInstance(r, Resolution) for r in self.agenda_repo.waivers]
        [self.assertIsInstance(r, Resolution) for r in self.agenda_repo.first_readings]

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

    def test_make_resolution_list(self):
        self.fail()
