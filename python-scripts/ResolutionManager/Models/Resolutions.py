from ResolutionManager.Models.Committees import Committee

URL_BASE = 'https://docs.google.com/document/d/'

class Resolution(object):

    def __init__(self, id=None, number=None, title=None, document_id=None, waiver=None, committee: Committee = None, cosponsors=[]):
        """
        :param number:
        :param title:
        :param document_id: Google Drive id
        """
        self.waiver = waiver
        self.id = id
        self.committee = committee
        self.cosponsors = cosponsors
        self.document_id = document_id
        self.title = title
        self.number = number

    @property
    def name(self):
        return self.title

    @property
    def url(self):
        return URL_BASE + self.document_id

    @property
    def agenda_item(self):
        """Returns the text as it should appear in the agenda """
        # todo Add correct date!
        t = f"AS-{self.number}-23/{self.committee.abbreviation}"
        if len(self.cosponsors) > 0:
            for c in self.cosponsors:
                t += f"/{c.abbreviation}"
        t += f" {self.title}"
        if self.waiver == 1:
            t += " WAIVER "
        return t


