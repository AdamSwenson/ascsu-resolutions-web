class Committee(object):

    def __init__(self, full_name, abbreviation, id=None):
        self.id = id
        self.full_name = full_name
        self.abbreviation = abbreviation


    @property
    def name(self):
        return self.full_name

