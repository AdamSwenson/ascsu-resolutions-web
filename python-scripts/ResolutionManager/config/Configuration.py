

class Configuration(object):
    BASE = '/Users/ars62917/Dropbox/ResolutionManager'

    CREDENTIALS_FOLDER = f"{BASE}/private"
    CREDENTIALS_FILEPATH = f"{CREDENTIALS_FOLDER}/credentials.json"
    TOKEN_FILEPATH = f"{CREDENTIALS_FOLDER}/token.json"

    GOOGLE_DRIVE_ROOT_FOLDER_ID = '1p0nw_jsf8nfFIrCDLF6IejKLyngtcYtg'

    TEMPLATE_DOCUMENT_ID = '1ipZ_SrSdh_wBHEqc92Oji-k8FxC8irp_yGMxeUZrpYU'

    TEMPLATE_HEADER_ID = 'kix.ykwloztnzf1q'
    RESOLUTION_FILENAME_TEMPLATE = "{resolution_number} {resolution_name}"

    SCOPES = ['https://www.googleapis.com/auth/documents',
              'https://www.googleapis.com/auth/drive']

    def __init__(self):
        pass
