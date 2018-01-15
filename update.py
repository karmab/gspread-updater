#!/usr/bin/python

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import sys


def updatespreadsheet(doc, row, separator='+', credpath='.'):
    if os.path.exists('/proc') and [l for l in open('/proc/self/cgroup').readlines() if 'docker' in l]:
        credpath = "%s/.credentials" % os.path.expanduser('~')
    row = row.split(separator)
    scope = ['https://spreadsheets.google.com/feeds']
    try:
        creds = ServiceAccountCredentials.from_json_keyfile_name('%s/client_secret.json' % credpath, scope)
        client = gspread.authorize(creds)
    except ValueError:
        print("Issue with credentials file. Leaving...")
        return 1
    except Exception as e:
        print(e)
        return 1
    try:
        doc = client.open(doc)
    except gspread.SpreadsheetNotFound:
        print("Spreadsheet not found. Leaving...")
        return 1
    sheet = doc.worksheets()[-1]
    index = len(sheet.get_all_values())
    index = 1 if index == 0 else index
    sheet.resize(rows=index)
    sheet.append_row(row)
    sheet.resize(rows=100)
    return 0

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
