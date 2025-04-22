from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import re

# Scope needed for metadata
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

def get_drive_service():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('drive', 'v3', credentials=creds)

def extract_file_id(url):
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
    return match.group(1) if match else None

def main():
    service = get_drive_service()

    with open('file-list.txt') as f:
        file_links = f.read().splitlines()

    for link in file_links:
        file_id = extract_file_id(link)
        if file_id:
            metadata = service.files().get(fileId=file_id, fields="name,modifiedTime,lastModifyingUser(displayName,emailAddress)").execute()
            print(f"\n📄 {metadata['name']}")
            print(f"Last Modified: {metadata['modifiedTime']}")
            user = metadata.get("lastModifyingUser", {})
            print(f"By: {user.get('displayName')} ({user.get('emailAddress')})")

if __name__ == '__main__':
    main()
