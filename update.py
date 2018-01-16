#!/usr/bin/python

import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import sys


def updatespreadsheet(doc, row, separator='+', credpath='.', headers=None, weekmode=True, sheetname='Week'):
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
    sheets = doc.worksheets()
    if weekmode:
        now = datetime.datetime.now()
        weeknumber = now.isocalendar()[1]
        weeksheet = "%s %s %s" % (sheetname, weeknumber, now.year)
        if weeksheet not in [sheet.title for sheet in sheets]:
            print("Adding new worksheet for current week")
            doc.add_worksheet(weeksheet, 6, 100)
            sheets = doc.worksheets()
    sheet = sheets[-1]
    index = len(sheet.get_all_values())
    delete = True if index == 0 else False
    putheaders = True if index == 0 else False
    index = 1 if index == 0 else index
    sheet.resize(rows=index)
    if putheaders and headers is not None:
        for line in headers.split(","):
            sheet.append_row(line.split(separator))
    sheet.append_row(row)
    sheet.resize(rows=100)
    if delete:
        sheet.delete_row(1)
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
