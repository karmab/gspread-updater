#!/usr/bin/python

from flask import Flask, request, jsonify
from update import updatespreadsheet
import os

app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    """
    adds line
    """
    print(request)
    # name = request.form['name'].lower()
    # upassword = request.form['password']
    result = {'result': 'success'}
    # code = 200
    result = {'result': 'failure', 'reason': 'wrong'}
    response = jsonify(result)
    # response.status_code = code
    return response

if __name__ == '__main__':
    if 'PASSWORD' in os.environ:
        password = os.environ['PASSWORD']
    else:
        password = None
    app.run(host="0.0.0.0", port=9000)
    # run()
