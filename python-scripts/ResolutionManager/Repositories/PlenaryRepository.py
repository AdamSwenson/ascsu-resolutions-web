import logging

from ResolutionManager.Models.Plenaries import Plenary


class PlenaryRepository(object):
    def __init__(self, dao):
        self.dao = dao
        self.logger = logging.getLogger(__name__)


    # def create_plenary(self, thursday_date):
    #     result = self.dao.execute("Insert into ascsu.plenaries (thursday_date) values ({thursday_date})")
    #
    #     return Plenary(thursday_date=result.thursday_date)

    def load_plenary(self, plenary_id):
        print(plenary_id)
        result = self.dao.conn.execute(f"select * from plenaries where id = {plenary_id}").fetchone()

        return Plenary(id=result.id,
                       thursday_date=result.thursday_date,
                       first_reading_folder_id=result.first_reading_folder_id,
                       plenary_folder_id=result.plenary_folder_id,
                       feedback_folder_id=result.feedback_folder_id,
                       second_reading_folder_id=result.second_reading_folder_id,
                       working_drafts_folder_id=result.working_drafts_folder_id,
                       agenda_id=result.agenda_id)

    def update_agenda_id(self, plenary, agenda_id):
        """Saves the document id of the agenda to the db"""
        self.dao.conn.execute(f"update ascsu.plenaries p set p.agenda_id = '{agenda_id}' where p.id = {plenary.id}")
        plenary.agenda_id = agenda_id
        return plenary

    def update_plenary_folder(self, plenary, plenary_folder_id):
        self.dao.conn.execute(
            f"update ascsu.plenaries p set p.plenary_folder_id = '{plenary_folder_id}' where p.id = {plenary.id}")
        plenary.plenary_folder_id = plenary_folder_id
        return plenary

    def update_plenary_first_reading_folder(self, plenary, first_reading_folder_id):
        self.dao.conn.execute(
            f"update ascsu.plenaries p set p.first_reading_folder_id = '{first_reading_folder_id}' where p.id = {plenary.id}")
        plenary.first_reading_folder_id = first_reading_folder_id
        return plenary

    def update_plenary_second_reading_folder(self, plenary, second_reading_folder_id):
        self.dao.conn.execute(
            f"update ascsu.plenaries p set p.second_reading_folder_id = '{second_reading_folder_id}' where p.id = {plenary.id}")
        plenary.second_reading_folder_id = second_reading_folder_id
        return plenary

    def update_feedback_folder(self, plenary, feedback_folder_id):
        self.dao.conn.execute(
            f"update ascsu.plenaries p set p.feedback_folder_id = '{feedback_folder_id}' where p.id = {plenary.id}")
        plenary.feedback_folder_id = feedback_folder_id
        return plenary

    def update_working_drafts_folder(self, plenary, working_drafts_folder_id):
        self.dao.conn.execute(
            f"update ascsu.plenaries p set p.working_drafts_folder_id = '{working_drafts_folder_id}' where p.id = {plenary.id}")
        plenary.working_drafts_folder_id = working_drafts_folder_id
        return plenary

