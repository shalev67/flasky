
from flask import Flask
from mongoengine import *
import os

app = Flask(__name__)

connect(host=os.environ['MONGODB_CONNECTION_STRING'])
#onnect(host="mongodb://localhost:27017/example")

class FiboCache(Document):
    index = IntField(unique=True,required=True)
    value = IntField(required=True)

@app.route('/fibo/<int:number>')
def fibo(number):
    cache = FiboCache.objects(index=number)
    if len(cache):
        return "<!DOCTYPE html><html><body><h1>Fibonacci number <i>F<sub>%s</sub></i> = %s</h1><h1 style=\"color:green;\">This number is cached</h1></body></html>" % (str(cache[0].index),str(cache[0].value))
    else:
        new_cache = FiboCache(index=number, value=fib(number))
        new_cache.save()
        return "<!DOCTYPE html><html><body><h1>Fibonacci number <i>F<sub>%s</sub></i> = %s</h1><h1 style=\"color:red;\">This is a new number</h1></body></html>" % (str(new_cache.index),str(new_cache.value))

@app.route('/fibo/admin/cache')
def cache():
    cache = FiboCache.objects.order_by('index')
    if len(cache):
        style_table = 'table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}'
        style_td = 'td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}'
        style='<style>%s %s</style>' % (style_table,style_td)
        td_indexes = str()
        td_values = str()
        for i in cache:
            td_indexes += '<td><i>F</i><sub>%s</sub></td>' % (str(i.index))
            td_values += '<td>%s</td>' % (str(i.value)) 
        return "<!DOCTYPE html><html><head>%s</head><body><h1 style=\"color:green;\">Cache</h1><table><tr>%s</tr><tr>%s</tr></table></body></html>" % (style,td_indexes,td_values)
    else:
        return "<!DOCTYPE html><html><body><h1 style=\"color:red;\">No cache</h1></body></html>"

@app.route('/fibo/admin/cache/drop')
def drop_cache():
    FiboCache.drop_collection()
    return "<!DOCTYPE html><html><body><h1 style=\"color:red;\">Dropped cache</h1></body></html>"

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
