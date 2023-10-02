import asyncio
import logging
from typing import Optional



IP_BROADCAST = "0.0.0.0"
DEFAULT_PORT = 4444

class Server:


    def __init__(self,  loop: asyncio.AbstractEventLoop, server_host: Optional[str] = None, server_port: Optional[int] = None):
        if server_host is None:
            self.__server_host = IP_BROADCAST
        self.__server_host = server_host
        if server_port is None:
            self.__server_port = DEFAULT_PORT
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
        '''
        Starts the server
        '''
        try: 
            self.server = await asyncio.start_server(self.client_handler, self.server_host, self.server_port)
            logging.info("Server listening at : {}:{}", self.server_host, self.server_port)
            self.server_loop.run_until_complete(self.server)
            self.server_loop.run_forever()
        except Exception as e:
            logging.error(e)
        except KeyboardInterrupt:
            logging.info("Keyboard interrupt.")
        

    def client_handler(self, client_reader: asyncio.StreamReader, client_writer: asyncio.StreamWriter):
        '''
        Client handler when getting a new connection. 
        '''
        logging.info("New remote connection.")
        line = str()
