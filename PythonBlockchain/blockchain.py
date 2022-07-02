from hashlib import sha256
from classes import *

DIFFICULTY=4
LIMITTRANSACT = 2

def updatehash(*args):
    BaseHash="";h=sha256()
    for arg in args:
        BaseHash += str(arg)
    h.update(BaseHash.encode('utf-8'))
    return h.hexdigest()

class Block():
    def __init__(self, number=0,prev_hash=0*64,nonce=0,numT=0):
        self.number=number
        self.prev_hash=prev_hash
        self.nonce=nonce
        self.numT=  numT
        self.data=[]
        pass
    
    def Genesis(self):
        print("GenesisMade")
        return Block(0,0*64,0,10)

    def hash(self):
        return updatehash(
            self.number,
            self.prev_hash,
            self.data,
            self.nonce
        ) 
    def __str__(self):
        return str("Block#: %s\nHash: %s\nPrevious: %s\nNonce: %s\nData: %s\n" %(
            self.number,
            self.hash(),
            self.prev_hash,
            self.nonce,
            self.data,
        )
    )
    def addTransact(self,tx):
        if self.numT >= LIMITTRANSACT:
            return False
        else :
            self.data.append(tx)
            self.numT+=1
            return True
        pass

class Blockchain():
    difficulty = DIFFICULTY

    def __init__(self):
        self.chain =[Block().Genesis()]

    def add(self,block):
        self.chain.append(block)

    def mine(self,txs):
    #si es True, la transaccion se añade al bloque actual
        while True:
            if(self.chain[-1].addTransact(txs)):
                print("Añadido a Bloque %s" %(self.chain[-1].number))
                return True
            #Si es False, el bloque llego a su limite, se procede a realizar el minado del bloque
            else: 
                while True:
                    if self.chain[-1].hash()[:self.difficulty]=="0"*self.difficulty:
                        print(self.chain[-1])
                        self.add(Block(self.chain[-1].number+1,self.chain[-1].hash()));break
                    else:
                        self.chain[-1].nonce +=1

    #Se valida que la blockchain se encuentre correctamente construida
    def isValid(self):
        for i in range(1,len(self.chain)):
            _previous = self.chain[i].prev_hash
            _current = self.chain[i-1].hash()
            if _previous != _current or _current[:self.difficulty]!="0"*self.difficulty:
                return False
        return True

    def txCalls(self):
        txs=[]
        for block in self.chain:
            for tx in block.data:
                txs.append(tx)
        return txs



##TestCode
#def main():
#    blockchain = Blockchain()
#    transacts = [
#    TxSec("Lima1",1000001,"IT1",5,20,0),
#    TxSec("Lima2",1000002,"IT3",5,20,0),
#    TxSec("Lima3",1000003,"IT5",5,20,0),
#    TxSec("Lima1",1000004,"IT4",5,20,0),
#    TxSec("Lima2",1000004,"IT1",5,20,0),
#    TxSec("Lima3",1000003,"IT6",5,20,0),
#    TxSec("Lima1",1000002,"IT4",5,20,0),
#    TxSec("Lima2",1000001,"IT1",5,20,0),
#    TxSec("Lima3",1000005,"IT2",5,20,0)]
#    num = 0
#
#    for tx in transacts:
#        num+=1
#        blockchain.mine(tx)
#
#    for block in blockchain.chain:
#        print(block)
#
#    print(blockchain.isValid())