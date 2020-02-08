import requests
from dotenv import load_dotenv
load_dotenv(override=True)
import os

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
SPREADSHEET_ID = os.environ['SPREADSHEET_ID']
COLUMN_RANGE = os.environ['COLUMN_RANGE']

headers = {'Authorization' : 'Bearer ' + ACCESS_TOKEN}
api_uri = 'https://sheets.googleapis.com/v4/spreadsheets/'
uri = api_uri + SPREADSHEET_ID + '/values/' + COLUMN_RANGE

def get_list():
    response = requests.get(uri, headers=headers)
    data = response.json()
    return data['values']

if __name__ == '__main__':
    print(get_list())

