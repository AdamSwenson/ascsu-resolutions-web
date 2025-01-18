import logging

from ResolutionManager.Errors.ResolutionError import ResolutionError
from ResolutionManager.Models.Plenaries import Plenary
from ResolutionManager.Models.Resolutions import Resolution
from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.config.Configuration import Configuration
from ResolutionManager.Repositories.CommitteeRepository import CommitteeRepository

import sys


class ResolutionRepository(object):
    def __init__(self, dao):
        self.dao = dao
        self.config = Configuration()
        self.logger = logging.getLogger(__name__)

    def load_resolution(self, resolution_id, sponsor=None, cosponsors=[], reading_type=None):
        """Loads resolution from database
        This should be the only method by which resolutions are loaded
        """
        # resolution_id = int(resolution_id)
        # resolution_id =11
        result = self.dao.conn.execute(f"select * from ascsu.resolutions where id = {resolution_id}").fetchone()
        r = Resolution(id=result.id,
                       number=result.number,
                       document_id=result.document_id,
                       title=result.title,
                       # waiver=result.waiver,
                       committee=sponsor,
                       cosponsors=cosponsors,
                       status=result.status,
                       reading_type=reading_type
                       # this has to come from junction table
                       # is_first_reading=result.is_first_reading,
                       # is_approved=result.is_approved)
                       )
        # Load the object representation from drive
        if r.document_id is not None:
            doc_repo = DocumentRepository()
            r.document_obj = doc_repo.get_document(r.document_id)

        return r

    def set_google_document_id(self, resolution: Resolution, document_id):
        """
        Adds the Google drive id to the resolution

        :param document_id: Google drive id of the resolution document
        :type resolution: Resolution
        """
        query = f"update ascsu.resolutions r set r.document_id = '{document_id}' where r.id={resolution.id}"
        sys.stdout.write(query)
        result = self.dao.conn.execute(query)

    def get_named_ranges(self, document):
        """
        Uses the named title range to find the start and end indexes in the document object
        :param document:
        :return:
        """
        try:
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
        except Exception as e:
            self.logger.warning(e)

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
                        # print(e['textRun']['content'])
                        title += e['textRun']['content']

            except KeyError:
                pass
        title = title.strip().replace('\n', '')
        return title

    def get_current_title_from_drive(self, resolution: Resolution):
        """ Looks up the title from the file in drive and returns the text
        :type resolution: Resolution
        """
        doc_repo = DocumentRepository()
        newdoc = doc_repo.get_document(resolution.document_id)
        startIndex = self.get_named_ranges(newdoc)[0]['startIndex']
        return self.get_title(newdoc, startIndex)

    def update_title_from_drive_version(self, resolution: Resolution):
        """Updates the title in the db from the text in the resolution
        todo this should report when a title can't be found
        :type resolution: Resolution
        """
        title = self.get_current_title_from_drive(resolution)
        # Added the reformatting to title case in AR-65
        title = title.strip().title()
        if len(title) > 0:
            query = f"update ascsu.resolutions r set r.title = '{title}' where r.id={resolution.id}"
            result = self.dao.conn.execute(query)

    def load_all_resolutions(self):
        """Loads all resolutions with the title as it exists in drive """
        # For now not going to sync the database,
        # just use title from drive if can be retrieved and default to db version
        committee_repo = CommitteeRepository(self.dao)
        resolutions = []
        query = f"select id from ascsu.resolutions"
        results = self.dao.conn.execute(query)
        for r in results:
            rid = r[0]
            sponsor = committee_repo.load_sponsor(rid)
            cosponsors = committee_repo.load_cosponsors(rid)
            rez = self.load_resolution(rid, sponsor, cosponsors)
            try:
                doc_title = self.get_current_title_from_drive(rez)
                if len(doc_title) > 0:
                    rez.title = doc_title
            except Exception as e:
                # We use the error to format log message but
                # don't raise it since we don't want to stop execution
                m = ResolutionError(e, rez, 'load_all_resolutions')
                self.logger.error(m)

            resolutions.append(rez)
        return resolutions

    def load_all_resolutions_for_plenary(self, plenary: Plenary):
        """Loads all resolutions for plenary with the title
        as it exists in drive
        :type plenary: Plenary"""
        # For now not going to sync the database,
        # just use title from drive if can be retrieved and default to db version
        committee_repo = CommitteeRepository(self.dao)
        resolutions = []

        query = f"select resolution_id, is_first_reading, is_waiver, reading_type from ascsu.plenary_resolution where plenary_id = {plenary.id}"
        results = self.dao.conn.execute(query)

        for rid, first_reading, is_waiver, reading_type in results:
            # self.logger.warning(rid)
            # make sure casts correctly
            # first_reading = bool(first_reading)
            # added AR-58
            # is_waiver = bool(is_waiver)

            # print((rid, is_waiver, first_reading))

            # sys.stderr.write(f"{rid} {first_reading} {is_waiver}" )
            try:
                # rid = r[0]
                sponsor = committee_repo.load_sponsor(rid)
                cosponsors = committee_repo.load_cosponsors(rid)
                rez = self.load_resolution(resolution_id=rid, sponsor=sponsor, cosponsors=cosponsors,
                                           reading_type=reading_type)
                # self.logger.warning(f"borp {rez}")

                # rez.is_first_reading = first_reading
                # rez.is_waiver = is_waiver

                # dev HOTFIX AR-128
                try:
                    doc_title = ''
                    doc_title = self.get_current_title_from_drive(rez)
                    if len(doc_title) > 0:
                        rez.title = doc_title
                except Exception as e:
                    pass

                resolutions.append(rez)

            except Exception as e:
                # We use the error to format log message but
                # don't raise it since we don't want to stop execution
                m = ResolutionError(e, rez, 'load_all_resolutions_for_plenary')
                self.logger.error(m)

        return resolutions

    def set_as_action_item(self, plenary: Plenary, resolution: Resolution):
        """Marks the resolution as an action item for the plenary
        :type resolution: Resolution
        :type plenary: Plenary
        """
        # NB, doesn't alter the waiver flag in case something that was supposed to be a first reading
        # accidentally got moved into the action folder and then moved back out. Agenda creation doesn't
        # use the waiver flag so shouldn't be a problem

        query = f"""UPDATE ascsu.plenary_resolution AS pr
        INNER JOIN
        (SELECT * FROM ascsu.plenary_resolution p WHERE p.plenary_id = {plenary.id} AND p.resolution_id = {resolution.id}) AS b
        ON pr.id = b.id
        SET pr.is_first_reading = 0, pr.reading_type='action'
        WHERE pr.id = b.id"""
        self.dao.conn.execute(query)
        # Update the model object just in case it is needed
        resolution.is_first_reading = False
        resolution.reading_type = 'action'
        return resolution

    def set_as_first_reading_item(self, plenary: Plenary, resolution: Resolution):
        """Marks the resolution as a first reading item  for the plenary.
        This is generally used to fix errors, e.g., a first reading item gets accidentally
        moved into the action items folder and then moved back

        :type resolution: Resolution
        :type plenary: Plenary

        NB, will set the waiver to the value on the resolution object.
        """
        waiver = 1 if resolution.is_waiver is True else 0

        query = f"""UPDATE ascsu.plenary_resolution AS pr
        INNER JOIN
        (SELECT * FROM ascsu.plenary_resolution p WHERE p.plenary_id = {plenary.id} AND p.resolution_id = {resolution.id}) AS b
        ON pr.id = b.id
        SET pr.is_first_reading = 1, pr.is_waiver = {waiver}, pr.reading_type = 'first'
        WHERE pr.id = b.id"""
        self.dao.conn.execute(query)
        # Update the model object just in case it is needed
        resolution.is_first_reading = True
        resolution.reading_type = 'first'
        return resolution

    def set_as_working_item(self, plenary: Plenary, resolution: Resolution):
        """Marks the resolution as an action item for the plenary
        :type resolution: Resolution
        :type plenary: Plenary
        """
        # NB, doesn't alter the waiver flag in case something that was supposed to be a first reading
        # accidentally got moved into the action folder and then moved back out. Agenda creation doesn't
        # use the waiver flag so shouldn't be a problem



        query = f"""UPDATE ascsu.plenary_resolution AS pr
        INNER JOIN
        (SELECT * FROM ascsu.plenary_resolution p WHERE p.plenary_id = {plenary.id} AND p.resolution_id = {resolution.id}) AS b
        ON pr.id = b.id
        SET pr.is_first_reading = 0, pr.reading_type='working'
        WHERE pr.id = b.id"""
        self.dao.conn.execute(query)
        # Update the model object just in case it is needed
        # resolution.is_first_reading = False
        resolution.reading_type = 'working'
        return resolution
