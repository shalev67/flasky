
import os
from flask import Flask

app = Flask(__name__)

is_200 = True

@app.route("/")
def hello():
    if is_200:
        return "<!DOCTYPE html><html><body><h1>Hello World my name is: %s</h1></body></html>" % os.uname()[1]
    else:
        return "<!DOCTYPE html><html><body><h1>Hello darkness my old friend: %s</h1></body></html>" % os.uname()[1], 500

@app.route('/bug')
def bug():
    while 1:
        pass

@app.route('/error')
def error():
    global is_200 
    is_200 = False
    return "ERROR"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

