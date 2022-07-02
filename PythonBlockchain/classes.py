
from ensurepip import version
import hashlib

from dataclasses import dataclass
from sqlite3 import Timestamp

@dataclass
class Transaction:
    sender: str
    receiver: str
    ammount: float

@dataclass
class TxSec:
    sucursal: str
    sku: float
    nombre: str
    costoT: float
    cantidad: int
    tipoTran: int

@dataclass
class Block:
    version: int
    timestamp: float
    nonce: int
    difficulty: int
    previous_hash: str
    transactions: list[Transaction]