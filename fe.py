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
    content = request.get_json(silent=True)
    row = content.get('row')
    upassword = content.get('password')
    if password is not None and upassword != password:
        result = {'result': 'failure', 'reason': 'not authorized'}
        code = 403
    else:
        print("Updating spreadsheet...")
        updatespreadsheet(doc, row)
        result = {'result': 'success'}
        code = 200
    response = jsonify(result)
    response.status_code = code
    return response

if __name__ == '__main__':
    global password
    if 'DOC' not in os.environ:
        print("You need to set the DOC env variable to the document name you want to update")
        sys.exit(1)
    else:
        doc = os.environ['DOC']
    if 'PASSWORD' in os.environ:
        password = os.environ['PASSWORD']
    else:
        password = None
    app.run(host="0.0.0.0", port=9000)
