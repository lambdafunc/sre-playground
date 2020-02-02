#---- Includes
# Read Python Flask documentation for more in-depth information
# https://flask.palletsprojects.com/en/1.1.x/#user-s-guide
import json
import random
from flask import Flask, jsonify

#---- App Defs
# Here we define how our application
# Please consider using ENV variables for production releases!
__NAME__ = "SRE PYG - Data Service"
__HOST__ = "0.0.0.0"
__PORT__ = "9876"
__DATA__ = "data.json"
__DEBUG__ = False

# Serve app
app = Flask(__NAME__)

# Open data file
with open(__DATA__, encoding='utf-8') as data_file:
   data = json.loads(data_file.read())

#---- Expose path to serve random quotes
@app.route('/api/quote', methods=['GET'])
def get_quote():
    return jsonify(random.choice(data))

#---- Main body
# This part runs the application
if __name__ == '__main__':
    app.run(
        port=__PORT__,
        host=__HOST__,
        debug=__DEBUG__
    )
