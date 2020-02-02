#---- Includes
# Read Python Flask documentation for more in-depth information
# https://flask.palletsprojects.com/en/1.1.x/#user-s-guide
from flask import Flask

#---- App Defs
# Here we define how our application
# Please consider using ENV variables for production releases!
__NAME__ = "SRE Playground Demo API"
__HOST__ = "0.0.0.0"
__PORT__ = "5555"
__DEBUG__ = False
__STATIC_FILE_PATH__ = "/static"

# Serve app
app = Flask(
    __NAME__,
    static_url_path=__STATIC_FILE_PATH__
)

#---- Expose path to serve content
@app.route('/')
def home():
    # Override with your custom message
    return 'Hello World!'

@app.route('/info')
def info():
    return app.send_static_file('info.html')

#---- Main body
# This part runs the application
if __name__ == '__main__':
    app.run(
        port=__PORT__,
        host=__HOST__,
        debug=__DEBUG__
    )
