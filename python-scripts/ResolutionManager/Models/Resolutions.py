from ResolutionManager.Models.Committees import Committee
from ResolutionManager.config.Templates import Templates


class Resolution(object):

    def __init__(self, id=None, number=None,
                 title=None,
                 document_id=None,
                 is_waiver=None,
                 committee: Committee = None,
                 cosponsors=[],
                 document_obj=None,
                 is_first_reading=None,
                 is_approved=None,
                 status=None,
                 reading_type=None,
                 year=24):
        """
        :param is_first_reading: Whether the resolution is currently in first reading
        :type is_first_reading: bool
        :param number:
        :param title:
        :param document_id: Google Drive id
        :param document_obj The dictionary representation of the document
        """
        # todo Add correct date --- year!
        self.reading_type = reading_type
        self.status = status
        self.year = year
        self.is_approved = bool(is_approved)
        self.is_first_reading_old = bool(is_first_reading)
        self.document_obj = document_obj
        self.is_waiver = bool(is_waiver)
        self.id = id
        self.committee = committee
        self.cosponsors = cosponsors
        self.document_id = document_id
        self.title = title
        self.number = number

    def __str__(self):
        return f"Resolution id:{self.id} number:{self.number} title:{self.title} readingType:{self.reading_type} "

    @property
    def end_index(self):
        """Gets the endIndex from the document representation"""
        if self.document_obj is not None:
            body = self.document_obj.get('body').get('content')
            return body[len(body) - 1]['endIndex']

    @property
    def is_action(self):
        """Returns the inverse of is_first_reading """
        return self.reading_type == 'action'
        # todo Replace with reading_type
        return not self.is_first_reading

    @property
    def is_first_reading(self):
        return self.reading_type == 'first'

    @property
    def waiver(self):
        # todo This is inconsistent should be is_waiver

        # todo Replace with reading_type
        return self.reading_type == 'waiver'
        return self.is_waiver == 1 or self.is_waiver is True

    @property
    def name(self):
        return self.title

    @property
    def url(self):
        # In AR-69 changed to handling None in the document id
        if self.document_id is None: return "---None---"
        return Templates.URL_BASE + self.document_id

    @property
    def agenda_item(self):
        """Returns the text as it should appear in the agenda """

        t = f"AS-{self.number}-{self.year}/{self.committee.abbreviation}"
        if len(self.cosponsors) > 0:
            for c in self.cosponsors:
                t += f"/{c.abbreviation}"
        t += f" {self.title}"

        if self.waiver is True:
            t += " WAIVER "
        return t

    @property
    def max_end_index_in_header(self):
        """Returns the maximum end index in the header. This is a utility
        used to help with formatting"""
        end_indices = []
        h = list(self.document_obj['headers'].keys())[0]
        # h = self.document_obj['headers'][0]
        end_indices.extend([a['endIndex'] for a in self.document_obj['headers'][h]['content']])

        # for h in self.document_obj['headers']:
        #     end_indices.extend([a['endIndex'] for a in self.document_obj['headers'][h]['content']])
        return max(end_indices)
