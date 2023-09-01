from ResolutionManager.Models.Resolutions import Resolution
import sys

class ResolutionRepository(object):
    def __init__(self, dao):
        self.dao = dao

    def load_resolution(self, resolution_id, sponsor=None, cosponsors=[]):
        # resolution_id = int(resolution_id)
        # resolution_id =11
        result = self.dao.conn.execute(f"select * from ascsu.resolutions where id = {resolution_id}").fetchone()

        # sys.stdout.write(str(resolution_id))

        return Resolution(id=result.id, number=result.number, document_id=result.document_id, title=result.title, committee=sponsor, cosponsors=cosponsors)


    def set_google_document_id(self, resolution, document_id):
        query = f"update ascsu.resolutions r set r.document_id = '{document_id}' where r.id={resolution.id}"
        sys.stdout.write(query)
        result = self.dao.conn.execute(query)
