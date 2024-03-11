import logging

from ResolutionManager.Models.Committees import Committee


class CommitteeRepository(object):

    def __init__(self, dao):
        self.dao = dao
        # self.conn = self.dao.engine.connect()
        self.logger = logging.getLogger(__name__)


    def load_committee(self, committee_id):
        c = self.dao.conn.execute(f"select * from ascsu.committees where id = {committee_id}").fetchone()
        return Committee(full_name=c.name, abbreviation=c.abbreviation, id=c.id)

    def load_cosponsors(self, resolution_id):
        cosponsor_ids = self.dao.conn.execute(
            f"select committee_id from ascsu.committee_resolution cr where cr.resolution_id = {resolution_id} and cr.is_cosponsor = 1").fetchall()
        cosponsor_ids = [c[0] for c in cosponsor_ids]
        return [self.load_committee(c) for c in cosponsor_ids]

    def load_sponsor(self, resolution_id):
        sponsor_id = self.dao.conn.execute(
            f"select cr.committee_id from ascsu.committee_resolution cr where cr.resolution_id = {resolution_id} and cr.is_sponsor = 1").fetchone()
        return self.load_committee(sponsor_id.committee_id)
        # sponsor = Committee(full_name=sponsor.name, abbreviation=sponsor.abbreviation, id=sponsor.id)
