from flask import Flask, jsonify, request
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
@app.route('/incidents_per_year', methods=['GET', 'POST'])
def incidents_per_year():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        airline = post_data['airline']
        year = post_data['year']
        graphOneData = data.graphOneData(airline, year)
        return jsonify(graphOneData)

if __name__ == '__main__':
    app.run()
