from flask import Flask, jsonify
from flask_cors import CORS

#Importing code that I wrote
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

# sanity check route
@app.route('/incidents_per_year', methods=['GET'])
def incidents_per_year():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()
