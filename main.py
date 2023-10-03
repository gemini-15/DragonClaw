import typer
import asyncio
from rich import print
import logging 

from connection_handler.server import Server

BANNER_DRAGONCLAW = "\n[dark_red] \
██████  ██████   █████   ██████   ██████  ███    ██  ██████ ██       █████  ██     ██ \n\
██   ██ ██   ██ ██   ██ ██       ██    ██ ████   ██ ██      ██      ██   ██ ██     ██ \n\
██   ██ ██████  ███████ ██   ███ ██    ██ ██ ██  ██ ██      ██      ███████ ██  █  ██ \n\
██   ██ ██   ██ ██   ██ ██    ██ ██    ██ ██  ██ ██ ██      ██      ██   ██ ██ ███ ██ \n\
██████  ██   ██ ██   ██  ██████   ██████  ██   ████  ██████ ███████ ██   ██  ███ ███[/dark_red]\n\n"
    

def main(ip: str = "0.0.0.0", port: int = 4444):
    print(BANNER_DRAGONCLAW)
    loop = asyncio.get_event_loop()
    server = Server(loop, ip, port)
    server.start()

if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    typer.run(main)
