

class Templates(object):
    """
    This holds all templates and standard styles in one place

    Usage:
        Templates.RESOLUTION_FILENAME_TEMPLATE.format(resolution_number=resolution.number,
                                                                   resolution_name=resolution.title,
                                                                   committee_abbrev=sponsor.abbreviation)
    """
    # Standard styles
    STANDARD_FONT = 'Atkinson Hyperlegible'
    STANDARD_FONT_SIZE = 12

    # Document components
    HEADER_TEMPLATE = "AS-{resolution_number}-{year}/{committee}"

    # Files
    AGENDA_FILENAME_TEMPLATE = "{plenary_name} Resolution list"
    RESOLUTION_FILENAME_TEMPLATE = "{resolution_number} {committee_abbrev} {resolution_name}"
    ORIGINAL_FOLDER_NAME = "First readings"
    PUBLIC_FOLDER_NAME = "For campus feedback"
    FILENAME_TEMPLATE = "{} FOR CAMPUS FEEDBACK"
    RESOLUTIONS_ROOT_NAME = 'Resolutions'
    FIRST_READING_FOLDER_NAME = 'First reading'
    ACTION_FOLDER_NAME = 'Action items'
    WORKING_DRAFTS_FOLDER_NAME = 'Working drafts'

    # Plenary
    PLENARY_FOLDER_TEMPLATE = "{year} {month}"
    DATE_TEMPLATE = "{month} {thurs}-{friday}, {year}"

    # Url
    URL_BASE = 'https://docs.google.com/document/d/'



    def __init__(self):
        pass
