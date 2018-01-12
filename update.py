import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import sys


def updatespreadsheet(doc, row, separator='+', credpath='.'):
    row = row.split(separator)
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('%s/client_secret.json' % credpath, scope)
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
        doc = os.environ.get('DOC')
        if doc is None:
            print("You need to set the DOC env variable to the document name you want to update")
            sys.exit(1)
        row = ' '.join(sys.argv[1:])
        updatespreadsheet(doc, row)
