import configparser
import os


class Configuration(object):
    # BASE = '/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts'
    # # BASE = "/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts"
    #
    # CREDENTIALS_FOLDER = f"{BASE}/private"
    # CREDENTIALS_FILEPATH = f"{CREDENTIALS_FOLDER}/credentials.json"
    # TOKEN_FILEPATH = f"{CREDENTIALS_FOLDER}/token.json"

    # GOOGLE_DRIVE_ROOT_FOLDER_ID = '1p0nw_jsf8nfFIrCDLF6IejKLyngtcYtg'

    # TEMPLATE_DOCUMENT_ID = '1ipZ_SrSdh_wBHEqc92Oji-k8FxC8irp_yGMxeUZrpYU'

    # TEMPLATE_HEADER_ID = 'kix.ykwloztnzf1q'
    RESOLUTION_FILENAME_TEMPLATE = "{resolution_number} {resolution_name}"

    SCOPES = ['https://www.googleapis.com/auth/documents',
              'https://www.googleapis.com/auth/drive']

    def __init__(self):
        self.set_environment()

        if self.env == 'local':
            self.config_path = "/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts/private/config.ini"
            self.BASE = "/Users/ars62917/Dropbox/ResolutionManagerWeb/python-scripts"
        else:
            self.BASE = "/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts"
            self.config_path = "/home/ascsuadam-swensoncom/ascsu.adam-swenson.com/python-scripts/private/config.ini"

        self.CREDENTIALS_FOLDER = f"{self.BASE}/private"
        self.CREDENTIALS_FILEPATH = f"{self.CREDENTIALS_FOLDER}/credentials.json"
        self.TOKEN_FILEPATH = f"{self.CREDENTIALS_FOLDER}/token.json"

        # self.config_path = "../../private/config.ini";
        self.configuration = configparser.ConfigParser()
        self.configuration.read( self.config_path )

        self.GOOGLE_DRIVE_ROOT_FOLDER_ID = self.configuration['drive']['GOOGLE_DRIVE_ROOT_FOLDER_ID']
        self.TEMPLATE_DOCUMENT_ID = self.configuration['drive']['TEMPLATE_DOCUMENT_ID']
        self.TEMPLATE_HEADER_ID = self.configuration['drive']['TEMPLATE_HEADER_ID']

        print(self.configuration)

    def set_environment(self):
        b = os.getcwd()
        loc = '/Users/ars62917'
        if b[:len(loc)] == loc:
            self.env = 'local'
        else:
            self.env = 'production'


    def base(self):
        # return 'wag'
        b = os.getcwd()
        return b

    @property
    def dsn(self):
        return f"mysql+mysqlconnector://{self.configuration['mysql']['user']}:{self.configuration['mysql']['password']}@{self.configuration['mysql']['ip']}/{self.configuration['mysql']['db']}"
        # return "mysql+mysqlconnector://root:@127.0.0.1:3306/ascsu"

    #
    # @classmethod
    # def read_config_file( cls ):
    #
    #     if not cls.file_path:
    #         # The file path could've been customized by instantiating the class
    #         # If that didn't happen, we go with the default
    #         # The folder containing the assets folder
    #         cls.proj_base = os.path.abspath( os.path.dirname( os.path.dirname( __file__ ) ) )
    #         # All login credentials are defined in files here.
    #         # THIS CONTENTS OF THIS FOLDER MUST NOT BE COMMITTED TO VERSION CONTROL!
    #         folder_path = CREDENTIALS_FOLDER_PATH.format(cls.proj_base)
    #         creds = TEST_CREDENTIALS if cls.is_test else LIVE_CREDENTIALS
    #         cls.file_path = creds.format(folder_path )
    #
    #     cls.configuration = configparser.ConfigParser()
    #     cls.configuration.read( cls.file_path )
    #     print( "Reading credentials and settings from %s" % cls.file_path )

