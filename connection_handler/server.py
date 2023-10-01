import asyncio
import logging

from common import TransportType

IP_BROADCAST = "0.0.0.0"
PORT = 4444

class server:


    def __init__(self, server_host: str, server_port: int, loop: asyncio.AbstractEventLoop):
        self.__server_host = server_host
        self.__server_port = server_port
        self.__server_loop = loop

        logging.info(f'Server initialized at {self.server_host}:{self.server_port}')

    @property
    def server_host(self):
        return self.__server_host
    
    @property
    def server_port(self):
        return self.__server_port
    
    @property
    def server_loop(self):
        return self.__server_loop
    
    
    async def start(self):
        self.server = await asyncio.start_server(self.client_handler, self.server_host, self.server_port)
        logging.info("Server listening at : {}:{}", self.server_host, self.server_port)


    async def client_handler(reader, writer):
        logging.info("New remote connection.")
        line = str()
