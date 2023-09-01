import os.path

from ResolutionManager import environment as env

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


class CredentialsManager(object):

    def __init__(self):
        self.creds = None
        self.get_credentials()


    def get_credentials(self):
        self.creds = None
        # The file token-1.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(env.TOKEN_FILEPATH):
            self.creds = Credentials.from_authorized_user_file(env.TOKEN_FILEPATH, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    env.CREDENTIALS_FILEPATH, SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(env.TOKEN_FILEPATH, 'w') as token:
                token.write(self.creds.to_json())

        return self.creds


