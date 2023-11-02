import sys
from enum import Enum



class TransportType(Enum):
    TCP = 1
    UDP = 2
    OTHER = 3

def interrupt_handler(signum, action):
    pass