import os.path

# from ResolutionManager import environment as env
# import ResolutionManager.config.environment as env

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these scopes, delete the file token-1.json.
# SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
SCOPES = ['https://www.googleapis.com/auth/documents',
          'https://www.googleapis.com/auth/drive']
# 'https://www.googleapis.com/auth/drive.metadata.readonly'

# TOKEN_FILENAME = env.TOKEN_FILEPATH
# CREDENTIALS_FILENAME = env.CREDENTIALS_FILEPATH

from ResolutionManager.config.Configuration import Configuration

BASE = "/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/"

CREDENTIALS_FOLDER = f"{BASE}/private"
CREDENTIALS_FILEPATH = f"{CREDENTIALS_FOLDER}/credentials.json"
TOKEN_FILEPATH = f"{CREDENTIALS_FOLDER}/token.json"

GOOGLE_DRIVE_ROOT_FOLDER_ID = '1p0nw_jsf8nfFIrCDLF6IejKLyngtcYtg'

TEMPLATE_DOCUMENT_ID = '1ipZ_SrSdh_wBHEqc92Oji-k8FxC8irp_yGMxeUZrpYU'

TEMPLATE_HEADER_ID = 'kix.ykwloztnzf1q'
RESOLUTION_FILENAME_TEMPLATE = "{resolution_number} {resolution_name}"

class CredentialsManager(object):

    def __init__(self):
        self.creds = None
        self.get_credentials()



    def get_credentials(self):
        cred_manager = CredentialsManager()

        self.creds = None
        # The file token-1.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(cred_manager.TOKEN_FILEPATH):
            # if os.path.exists(env.TOKEN_FILEPATH):
            self.creds = Credentials.from_authorized_user_file(cred_manager.TOKEN_FILEPATH, SCOPES)

        # self.creds = Credentials.from_authorized_user_file(env.TOKEN_FILEPATH, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILEPATH, SCOPES)

                # env.CREDENTIALS_FILEPATH, SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(TOKEN_FILEPATH, 'w') as token:
                # with open(env.TOKEN_FILEPATH, 'w') as token:
                token.write(self.creds.to_json())

        return self.creds


