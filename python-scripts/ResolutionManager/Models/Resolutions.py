from ResolutionManager.Models.Committees import Committee
from ResolutionManager.config.Templates import Templates


class Resolution(object):

    def __init__(self, id=None, number=None,
                 title=None,
                 document_id=None,
                 waiver=None,
                 committee: Committee = None,
                 cosponsors=[],
                 document_obj=None,
                 is_first_reading=None,
                 is_approved=None,
                 year=23):
        """
        :param is_first_reading: Whether the resolution is currently in first reading
        :type is_first_reading: bool
        :param number:
        :param title:
        :param document_id: Google Drive id
        :param document_obj The dictionary representation of the document
        """
        # todo Add correct date --- year!
        self.year = year
        self.is_approved = bool(is_approved)
        self.is_first_reading = bool(is_first_reading)
        self.document_obj = document_obj
        self.waiver = bool(waiver)
        self.id = id
        self.committee = committee
        self.cosponsors = cosponsors
        self.document_id = document_id
        self.title = title
        self.number = number

    @property
    def end_index(self):
        """Gets the endIndex from the document representation"""
        if self.document_obj is not None:
            body = self.document_obj.get('body').get('content')
            return body[len(body) - 1]['endIndex']

    @property
    def name(self):
        return self.title

    @property
    def url(self):
        return Templates.URL_BASE + self.document_id

    @property
    def agenda_item(self):
        """Returns the text as it should appear in the agenda """

        t = f"AS-{self.number}-{self.year}/{self.committee.abbreviation}"
        if len(self.cosponsors) > 0:
            for c in self.cosponsors:
                t += f"/{c.abbreviation}"
        t += f" {self.title}"
        if self.waiver == 1:
            t += " WAIVER "
        return t
