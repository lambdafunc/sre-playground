#---- Includes
# Read Python Flask documentation for more in-depth information
# https://flask.palletsprojects.com/en/1.1.x/#user-s-guide
import requests
from flask import Flask, render_template, jsonify

#---- App Defs
# Here we define how our application
# Please consider using ENV variables for production releases!
__NAME__ = "SRE PYG - Content Service"
__HOST__ = "0.0.0.0"
__PORT__ = "5555"
__DEBUG__ = False
__RANDOM_QUOTE_PATH__ = "http://0.0.0.0:9876/api/quote"

# Serve app
app = Flask(__NAME__)

#---- Get Random quote from our Data instance
def get_quote():
    try:
        r = requests.get(url=__RANDOM_QUOTE_PATH__)
        return r.json()
    except Exception as e:
        print(e)
        return {"author": "Error", "text": "Seems like your data instance is not on."}

#---- Expose path to serve content
@app.route('/')
def home():
    data = get_quote()
    return render_template('info.html', data=data)

#---- Main body
# This part runs the application
if __name__ == '__main__':
    app.run(
        port=__PORT__,
        host=__HOST__,
        debug=__DEBUG__
    )
