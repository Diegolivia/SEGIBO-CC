from flask import Flask
from flask import request
from blockchain import *

from classes import TxSec

blockchain = Blockchain()

def TransacDecoder(obj):
    return TxSec(obj['sucursal'],obj['SKU'],obj['nombre'],obj['costo'],obj['cantidad'],obj['tipotransaccion'])

app = Flask(__name__)

@app.route("/transaction")
def addTransact():
    print (request.is_json)
    content = request.get_json()
    blockchain.mine(TransacDecoder(content))
    return 'JSON posted'

def initBlockchain():
    #Validate Blockchain
    blockchain.isValid()

if __name__ == '__main__':
    initBlockchain()
    app.run(debug=True)