
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world! myname is " + os.uname()[1]

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

