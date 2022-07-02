import json
from math import prod
from flask import Flask
from flask import jsonify
from flask import request

class TransactObj(object):
    def __init__(self,sucursal,product):
        self.sucursal = sucursal
        self.product = product

def TransacDecoder(obj):
    if '__type__' in obj and obj['__type__'] == 'Student':
        return TransactObj(obj['sucursal'],obj['product'])
    return obj

app = Flask(__name__)

@app.route('/hello',methods=['GET','POST'])
def welcome():
    return "Hello World!"

@app.route("/transaction")
def addTransact():
    print (request.is_json)
    content = request.get_json()
    print(content)
    print(content['Sucursal'])
    return 'JSON posted'

if __name__ == '__main__':
    app.run(debug=True)