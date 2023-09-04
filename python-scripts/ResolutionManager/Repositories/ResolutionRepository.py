from ResolutionManager.Models.Resolutions import Resolution
from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.config.Configuration import Configuration

import sys

class ResolutionRepository(object):
    def __init__(self, dao):
        self.dao = dao
        self.config = Configuration()

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


    def get_named_ranges(self, document ):
        """
        Uses the named title range to find the start and end indexes in the document object
        :param document:
        :return:
        """
        titleRangeName = self.config.TITLE_RANGE_NAME
        # print(self.config.TITLE_RANGE_NAME)
        # titleRangeName = 'titleRange'
        # Find the matching named ranges.
        named_range_list = document.get('namedRanges', {}).get(titleRangeName)
        if not named_range_list:
            raise Exception('The named range is no longer present in the document.')

        # Determine all the ranges of text to be removed, and at which indices the
        # replacement text should be inserted.
        all_ranges = []
        insert_at = {}
        for named_range in named_range_list.get('namedRanges'):
            ranges = named_range.get('ranges')

            all_ranges.extend(ranges)
            # Most named ranges only contain one range of text, but it's possible
            # for it to be split into multiple ranges by user edits in the document.
            # The replacement text should only be inserted at the start of the first
            # range.
            insert_at[ranges[0].get('startIndex')] = True

        return all_ranges

    def get_title(self, document, startIndex):
        """
        Loads the title from the google document object
        NOT USUALLY PUBLICLY CALLED
        :param document:
        :param startIndex:
        :return:
        """
        doc_content = document.get('body').get('content')
        title = ""
        for i in doc_content:
            try:
                if i['startIndex'] == startIndex:
                    for e in i['paragraph']['elements']:
                        print(e['textRun']['content'])
                        title += e['textRun']['content']

            except KeyError:
                pass
        title = title.strip().replace('\n', '')
        return title

    def get_current_title_from_drive(self, resolution):
        """ Looks up the title from the file in drive and returns the text """
        doc_repo = DocumentRepository()
        newdoc = doc_repo.get_document(resolution.document_id)
        startIndex = self.get_named_ranges(newdoc)[0]['startIndex']
        return self.get_title(newdoc, startIndex)

    def update_title_from_drive_version(self, resolution):
        """Updates the title in the db from the text in the resolution
        todo this should report when a title can't be found
        """
        title = self.get_current_title_from_drive(resolution)
        title = title.strip()
        if len(title) > 0:
            query = f"update ascsu.resolutions r set r.title = '{title}' where r.id={resolution.id}"
            result = self.dao.conn.execute(query)



