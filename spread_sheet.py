from google.oauth2 import service_account
import json
import os
import requests
import googleapiclient.discovery
from dotenv import load_dotenv
load_dotenv(override=True)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

service_account_info = {
    "type": os.environ['TYPE'],
    "project_id": os.environ['PROJECT_ID'],
    "private_key_id": os.environ['PRIVATE_KEY_ID'],
    "private_key": os.environ['PRIVATE_KEY'],
    "client_email": os.environ['CLIENT_EMAIL'],
    "client_id": os.environ['CLIENT_ID'],
    "auth_uri": os.environ['AUTH_URI'],
    "token_uri": os.environ['TOKEN_URI'],
    "auth_provider_x509_cert_url": os.environ['AUTH_PROVIDER_X509_CERT_URL'],
    "client_x509_cert_url": os.environ['CLIENT_X509_CERT_URL'],
}

credentials = service_account.Credentials.from_service_account_info(
        service_account_info, scopes=SCOPES)

service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id = os.environ['SPREADSHEET_ID']
range_names = [
    os.environ['RANGE']
]

def get_list():
    result = service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id, ranges=range_names).execute()
    ranges = result.get('valueRanges', [])
    return ranges[0]['values']

if __name__ == '__main__':
    print(get_list())

