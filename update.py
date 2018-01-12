import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import sys


def updatespreadsheet(row, separator='+'):
    row = row.split(separator)
    DOC = "OpenShift Solutions Engineering Weekly Status"
    doc = os.environ.get('DOC', DOC)
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    doc = client.open(doc)
    sheet = doc.worksheets()[-1]
    index = len(sheet.get_all_values())
    sheet.resize(rows=index)
    sheet.append_row(row)
    sheet.resize(rows=1000)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("No information provided. Leaving")
        sys.exit(1)
    else:
        row = ' '.join(sys.argv[1:])
        updatespreadsheet(row)
