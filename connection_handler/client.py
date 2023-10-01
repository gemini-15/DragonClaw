import socket
from common import TransportType

BUFFER_RECV = 4096

class client:

    transportType = TransportType.TCP
    target_host = "127.0.0.1"   # Default address
    target_port = "8080"        # Default port
    buffer = b''

    def __init__(self, transportType, target_host, target_port):
        self.transportType = transportType
        self.target_host = target_host
        self.target_port = target_port

        match self.transportType:
            case TransportType.TCP:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.target_host, self.target_port))

            case TransportType.UDP:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

            case _:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_RAW)

    def send_data(self, data):
        self.buffer = bytes(data)
        match self.transportType:
            case TransportType.TCP:
                self.client.send(self.buffer)

            case TransportType.UDP:
                self.client.sendto(self.buffer, (self.target_host, self.target_port))

            case _:
                self.client.sendto(self.buffer, (self.target_host, self.target_port))

    def receive_data(self):

        match self.transportType:
            case TransportType.TCP:
                resp = self.client.recv(BUFFER_RECV)
                return resp.decode()
            case TransportType.UDP: 
                resp, addr = self.client.recvfrom(BUFFER_RECV)
                return resp.decode()

    def close_conn(self):
        self.client.close()


    
