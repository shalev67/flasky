
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<!DOCTYPE html><html><body><h1>Hello World my name is: %s</h1></body></html>" % os.uname()[1]

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

