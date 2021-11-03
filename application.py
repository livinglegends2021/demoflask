from flask import Flask 
application = Flask(__name__)


@application.route("/")
def home():
    return 'Hi World'

@application.route("/page")
def page():
    return 'This is my pageeee'

if __name__=="__main__":
    application.run()
