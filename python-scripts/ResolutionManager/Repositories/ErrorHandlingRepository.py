import os

from ResolutionManager.config.Configuration import Configuration


class ErrorHandlingRepository(object):
    """
    This contains tools for dealing with various errors,
    especially in interacting with google drive
    """

    def __init__(self):
        self.config = Configuration()
        pass

    @property
    def token_path(self):
        return self.config.TOKEN_FILEPATH
        # return f"{os.getcwd()}/private/token.json"

    def delete_old_token(self):
        """
        Deletes existing token file
        :return:
        """
        try:
            if os.path.isfile(self.token_path):
                os.remove(self.token_path)
        except OSError as e:
            # If it fails, inform the user.
            print(f"Error: Failed to delete token \n {e.filename} - {e.strerror}")
