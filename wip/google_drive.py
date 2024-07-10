from __future__ import print_function
import os.path
import pickle
import io
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def create_directory(service, name, parent_id=None):
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    if parent_id:
        file_metadata['parents'] = [parent_id]
    file = service.files().create(body=file_metadata,
                                  fields='id').execute()
    return file.get('id')

def move_files_to_directory(service, file_ids, directory_id):
    for file_id in file_ids:
        # Retrieve the existing parents to remove
        file = service.files().get(fileId=file_id,
                                   fields='parents').execute()
        previous_parents = ",".join(file.get('parents'))
        # Move the file to the new folder
        service.files().update(fileId=file_id,
                               addParents=directory_id,
                               removeParents=previous_parents,
                               fields='id, parents').execute()

def list_files(service):
    results = service.files().list(
        pageSize=100, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    return items

def main():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    # Create .bak directory
    bak_directory_id = create_directory(service, '.bak')

    # List all files in Google Drive
    files = list_files(service)
    file_ids = [file['id'] for file in files]

    # Move all files to .bak directory
    move_files_to_directory(service, file_ids, bak_directory_id)

    # Create new directories and registration points as needed
    # Example: creating a new directory called "NewDirectory"
    new_directory_id = create_directory(service, 'NewDirectory')

    # Further steps to build an index can be added here

if __name__ == '__main__':
    main()
