import asyncio
import logging
import sys
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
    
    
    def start(self):
        '''
        Starts the server
        '''
        try: 
            self.server = asyncio.start_server(self.accept_connection, self.server_host, self.server_port)
            logging.info(f"Server listening at : {self.server_host}:{self.server_port}")
            self.server_loop.run_until_complete(self.server)
            self.server_loop.run_forever()
        except Exception as e:
            logging.error(e)
        except KeyboardInterrupt:
            logging.info("Keyboard interrupt.")
        

    def accept_connection(self, client_reader: asyncio.StreamReader, client_writer: asyncio.StreamWriter):
        '''
        Client handler when getting a new connection. 
        '''
        logging.info("New remote connection registered.")
        
        task = asyncio.Task(self.client_handler(client_reader, client_writer))
        client_info = client_writer.get_extra_info('peername')
        logging.info(client_info)


    async def client_handler(self, client_reader: asyncio.StreamReader, client_writer: asyncio.StreamWriter):
        """
        Handles the incoming messages from the client. 

        """
        while True:
            command = sys.stdin.readline()
            client_writer.write(command.encode())
            await client_writer.drain()
            client_message = str((await client_reader.read(1024)).decode("utf8"))

            if client_message.startswith("quit"):
                break
            print(f'{client_message}')
        
        logging.info("Client disconnected.")