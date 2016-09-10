
from flask import Flask
app = Flask(__name__)

@app.route('/fibo/<int:number>')
def fibo(number):
    return "<!DOCTYPE html><html><body><h1>Fibonacci number <i>F<sub>%s</sub></i> = %s</h1></body></html>" % (str(number),str(fib(number)))

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
