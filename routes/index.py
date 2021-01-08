import json
from flask import jsonify


def index():
    return 'Index route works!'

with open('./result.json',encoding='UTF8') as json_file:
    data = json.load(json_file)
    # ML integration goes in here

def api():
    # ML Controller insert here
    return jsonify(data)