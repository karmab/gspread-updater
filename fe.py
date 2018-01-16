#!/usr/bin/python

from flask import Flask, request, jsonify
from update import updatespreadsheet
import os
import sys

app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    """
    adds line
    """
    if request.is_json:
        content = request.get_json(silent=True)
    else:
        content = request.form
    row = content.get('row')
    upassword = content.get('password')
    if password is not None and upassword != password:
        result = {'result': 'failure', 'reason': 'not authorized'}
        code = 403
    elif row is None:
        result = {'result': 'failure', 'reason': 'missing row information'}
        code = 422
    else:
        print("Updating spreadsheet...")
        res = updatespreadsheet(doc, row, credpath=credpath, headers=headers, weekmode=weekmode)
        if res == 0:
            result = {'result': 'success'}
            code = 200
        else:
            result = {'result': 'failure', 'reason': 'issue processing this sheet'}
            code = 422
    response = jsonify(result)
    response.status_code = code
    return response

if __name__ == '__main__':
    global password
    global weekmode
    global credpath
    if 'KUBERNETES_PORT' in os.environ:
        credpath = '/tmp/.credentials'
    else:
        credpath = '.'
    if 'DOC' not in os.environ:
        print("You need to set the DOC env variable to the document name you want to update")
        sys.exit(1)
    else:
        doc = os.environ['DOC']
    password = os.environ['PASSWORD'] if 'PASSWORD' in os.environ else None
    weekmode = os.environ['WEEKMODE'] if 'WEEKMODE' in os.environ else False
    weekmode = True if 'true' in weekmode.lower() else False
    headers = os.environ['HEADERS'] if 'HEADERS' in os.environ else None
    app.run(host="0.0.0.0", port=9000)
