from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sys
import os

from routes import index as routes

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return routes.index()


@app.route('/api', methods=['POST'])
@cross_origin()
def api():
    req = request.json

    return routes.api()


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
