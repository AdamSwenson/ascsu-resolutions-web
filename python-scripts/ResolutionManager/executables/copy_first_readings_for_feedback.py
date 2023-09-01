import ResolutionManager.environment as env

from ResolutionManager.Repositories.DocumentRepository import DocumentRepository
from ResolutionManager.Repositories.FileRepository import FileRepository

ORIGINAL_FOLDER_NAME = "First readings"
PUBLIC_FOLDER_NAME = "For campus feedback"
FILENAME_TEMPLATE = "{} FOR CAMPUS FEEDBACK"

def main(plenary):
    doc_repo = DocumentRepository()
    file_repo = FileRepository()

    # plenary_folder_id = '1ITs5N1qpTbqVqAhALrxqSsDwiSKsnSj5'
    # plenary_folder_id = plenary.plenary_folder_id

    # Get original folder id (the first readings folder)
    original_folder_name = ''
    # original_folder_id = '1sv_4BUV5fk6Kcjss8HeSCJWnsLZJVpKC'
    # original_folder_id = plenary.first_reading_folder_id


    # Create new folder for feedback versions
    # todo This needs to check that the folder doesn't already exist
    plenary.feedback_folder_id = file_repo.create_folder(PUBLIC_FOLDER_NAME)
    file_repo.move_file_to_folder(plenary.feedback_folder_id, plenary.plenary_folder_id)

    # print(file_repo.list_files())

    # Make copies and move to new folder
    # files = [f for f in file_repo.list_files()]
    files = file_repo.list_files(folder_id=plenary.first_reading_folder_id)

    for f in files:
        new_name = FILENAME_TEMPLATE.format(f['name'])
        copy_id = file_repo.copy_file(f['id'], new_name)
        file_repo.move_file_to_folder(copy_id, plenary.feedback_folder_id )

    # files = [f for f in file_repo.list_files() if original_folder_id in f['parents']  ]
    # print(files)

    # todo Return link to sharable folder
if __name__ == '__main__':
    main()