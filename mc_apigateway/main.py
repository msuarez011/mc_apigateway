from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import datetime
import requests
import re

app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running..."
    return jsonify(json)


def loadFIleConfing():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataconfig = loadFIleConfing()
    print("Server running: " + "http://" + dataconfig["url-backend"]+
          ":" + str(dataconfig["port"]))
serve(app, host = dataconfig["url-backend"], port = dataconfig["port"])