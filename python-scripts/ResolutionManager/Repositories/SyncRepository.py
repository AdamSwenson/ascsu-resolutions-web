import logging

from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Repositories.FileRepository import FileRepository
from ResolutionManager.Repositories.ResolutionRepository import ResolutionRepository


class SyncRepository(object):
    """Handles syncing any manual changes with the database"""

    def __init__(self, dao):
        self.dao = dao
        self.logger = logging.getLogger(__name__)

        self.db_plenary_resolutions = []
        self.plenary = None

        # self.plenary_repo = PlenaryRepository(dao)
        self.resolution_repo = ResolutionRepository(dao)
        self.file_repo = FileRepository()

        self.action_item_file_ids = []
        self.first_reading_file_ids = []
        self.working_file_ids = []
        # self.extant_files = []

        # resolutions we need to do something with
        self.deleted_files = []
        self.update_to_action_resolutions = []
        self.update_to_first_resolutions = []
        self.update_to_working_resolutions = []

        # dict of things that have been done outside of the app (i.e., directly in the drive)
        # self.actions_taken = {
        #     'moved_to_action': [],
        #     'moved_to_first': [],
        #     'moved_to_working': []
        # }
        #
        # self.actions_needing_review = {
        #     'deleted_by_user': []
        # }

    def sync(self, plenary):
        """Handles all syncing.
        Main called method
        """
        self.plenary = plenary

        try:
            # load all resolutions which should be part of the plenary, according to the db
            self.db_plenary_resolutions = self.resolution_repo.load_all_resolutions_for_plenary(self.plenary)
        except Exception as e:
            print('Error loading resolutions from db ', e)
            self.logger.error(f'Error loading resolutions from db \n{e}', )

        # Get all resolutions for the plenary from the drive
        self._load_from_drive()

        self._find_deleted_resolutions()
        self._find_resolutions_to_update_to_first()
        self._find_resolutions_to_update_to_action()
        self._find_resolutions_to_update_to_working()

        self._sync_action_resolutions()
        self._sync_working_resolutions()
        self._sync_first_resolutions()

        # print(self.__dict__)

    @property
    def extant_files(self):
        """File ids (document_id) which still exist in the drive"""
        return self.first_reading_file_ids + self.action_item_file_ids + self.working_file_ids

    def _load_from_drive(self):
        """Check the drive and load file ids for each reading type as they exist in the drive
        Populates internal lists of file ids
        """
        try:
            print('Action item files in drive')
            # NB, the raw result from drive is a dict with the key id
            # that corresponds to document_id in the Resolution object
            b = self.file_repo.list_files(self.plenary.second_reading_folder_id)
            self.action_item_file_ids = [f['id'] for f in
                                         self.file_repo.list_files(self.plenary.second_reading_folder_id)]
        except TypeError as e:
            print(e)
            pass

        try:
            print('First reading files in drive')
            self.first_reading_file_ids = [f['id'] for f in
                                           self.file_repo.list_files(self.plenary.first_reading_folder_id)]
        except TypeError:
            pass
        try:
            print('Working files in drive')
            self.working_file_ids = [f['id'] for f in self.file_repo.list_files(self.plenary.working_drafts_folder_id)]
        except TypeError:
            pass

    def _search_plenary_resolutions(self, file_id):
        """Gets the resolution object for the given document id"""
        a = [r for r in self.db_plenary_resolutions if r.document_id == file_id]
        print('search', a)
        if len(a) > 0: return a[0]
        return None

    def _find_deleted_resolutions(self):
        """Populates the deleted_files list with resolution objects which have been manually deleted"""
        for r in self.db_plenary_resolutions:
            if r.document_id not in self.extant_files:
                self.deleted_files.append(r)
                # Log the deleted items
                m = f"""\n===========================\n
                RESOLUTION MANUALLY DELETED\n
                Resolution #{r.id}\n
                Title: {r.title}\n
                Plenary: {self.plenary.formatted_plenary_date}\n
                \n===========================\n
                """
                self.logger.warning(m)

    def _find_resolutions_to_update_to_action(self):
        print(self.action_item_file_ids)
        for f in self.action_item_file_ids:
            r = self._search_plenary_resolutions(f)

            print(r)
            if r is not None and r.reading_type != 'action':
                self.update_to_action_resolutions.append(r)

    def _find_resolutions_to_update_to_first(self):
        for f in self.first_reading_file_ids:
            r = self._search_plenary_resolutions(f)
            if r is not None and r.reading_type != 'first' and r.reading_type != 'waiver':
                self.update_to_first_resolutions.append(r)

    def _find_resolutions_to_update_to_working(self):
        """Returns a list of resolution objects which have been manually moved to
        the working folder."""
        for f in self.working_file_ids:
            r = self._search_plenary_resolutions(f)
            if r is not None and r.reading_type != 'working':
                self.update_to_working_resolutions.append(r)

    def _sync_action_resolutions(self):
        """Takes all resolution in the update_to_action_resolutions list
        and sets them as action resolutions in the database"""
        for r in self.update_to_action_resolutions:
            self.resolution_repo.set_as_action_item(self.plenary, r)

    def _sync_first_resolutions(self):
        """Takes all resolutions in the update_to_first_resolution list and sets them
        as first readings in the database"""
        for r in self.update_to_first_resolutions:
            self.resolution_repo.set_as_first_reading_item(self.plenary, r)

    def _sync_working_resolutions(self):
        """Takes all resolutions in the update_to_working resolution list and sets them
        as working in the database"""
        for r in self.update_to_working_resolutions:
            self.resolution_repo.set_as_working_item(self.plenary, r)

