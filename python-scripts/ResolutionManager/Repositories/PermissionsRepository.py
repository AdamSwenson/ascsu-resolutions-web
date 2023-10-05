from ResolutionManager.API.CredentialsManager import CredentialsManager

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class PermissionsRepository(object):

    def __init__(self):
        self.cred_manager = CredentialsManager()
        self.service = build('drive', 'v3', credentials=self.cred_manager.creds)

    def make_all_in_folder_readonly(self, folder_id, reason='restricted during plenary'):
        content_restriction = {'readOnly': True, 'reason': reason}

        response = self.service.files() \
            .update(fileId=folder_id, body={'contentRestrictions': [content_restriction]}, fields="contentRestrictions") \
            .execute()
        return response

    def remove_readonly_from_all_in_folder(self, folder_id):
        content_restriction = {'readOnly': False}

        response = self.service.files() \
            .update(fileId=folder_id, body={'contentRestrictions': [content_restriction]}, fields="contentRestrictions") \
            .execute()
        return response

    # def create_permission(self, file_id):
    #     user_permission = {
    #         'type': 'anyone',
    #         'role': 'writer',
    #         # 'emailAddress': 'user@example.com'
    #     }
    #     self.service.permissions().create(fileId=file_id, body=user_permission, fields='id').execute()

    def delete_permission(self, file_id, permission_id):
        return self.service.permissions().delete(fileId=file_id, permissionId=permission_id).execute()

    def get_permission(self, file_id):
        return self.service.permissions().list(fileId=file_id).execute()

    def make_world_writeable(self, file_id):
        user_permission = {
            'type': 'anyone',
            'role': 'writer',
            # 'emailAddress': 'user@example.com'
        }
        self.service.permissions().create(fileId=file_id, body=user_permission, fields='id').execute()

    def remove_world_writable(self, file_id):
        permission_id = 'anyoneWithLink'
        return self.delete_permission(file_id, permission_id)

    def make_world_readable(self, file_id):
        user_permission = {
            'type': 'anyone',
            'role': 'reader',
            # 'emailAddress': 'user@example.com'
        }
        return self.service.permissions().create(fileId=file_id, body=user_permission, fields='id').execute()

    def remove_world_readable(self, file_id):
        permission_id = 'anyoneWithLink'
        return self.delete_permission(file_id, permission_id)

    def get_sharing_link(self, file_id):
        return self.service.files().get(fileId=file_id).execute()

    #
    # def share_file(self, real_file_id, real_user, real_domain):
    #     """Batch permission modification.
    #     Args:
    #         real_file_id: file Id
    #         real_user: User ID
    #         real_domain: Domain of the user ID
    #     Prints modified permissions
    #
    #     """
    #
    #     try:
    #         # create drive api client
    #         ids = []
    #         file_id = real_file_id
    #
    #         def callback(request_id, response, exception):
    #             if exception:
    #                 # Handle error
    #                 print(exception)
    #             else:
    #                 print(f'Request_Id: {request_id}')
    #                 print(F'Permission Id: {response.get("id")}')
    #                 ids.append(response.get('id'))
    #
    #         # pylint: disable=maybe-no-member
    #         batch = self.service.new_batch_http_request(callback=callback)
    #         user_permission = {
    #             'type': 'user',
    #             'role': 'writer',
    #             'emailAddress': 'user@example.com'
    #         }
    #         batch.add(self.service.permissions().create(fileId=file_id,
    #                                                body=user_permission,
    #                                                fields='id', ))
    #         domain_permission = {
    #             'type': 'domain',
    #             'role': 'reader',
    #             'domain': 'example.com'
    #         }
    #         domain_permission['domain'] = real_domain
    #         batch.add(self.service.permissions().create(fileId=file_id,
    #                                                body=domain_permission,
    #                                                fields='id', ))
    #         batch.execute()
    #
    #     except HttpError as error:
    #         print(F'An error occurred: {error}')
    #         ids = None
    #
    #     return ids
    #
    # if __name__ == '__main__':
    #     share_file(real_file_id='1dUiRSoAQKkM3a4nTPeNQWgiuau1KdQ_l',
    #                real_user='gduser1@workspacesamples.dev',
    #                real_domain='workspacesamples.dev')
    # def make_all_in_folder_only_owner_editable(self, folder_id, reason='restricted during plenary'):
    #     content_restriction = {'readOnly': True, 'ownerRestricted': True, 'reason': reason}
    #
    #     response = self.service.files().update(fileId=folder_id, body={'contentRestrictions': [content_restriction]},
    #                                             fields="contentRestrictions").execute()
    #     return response
