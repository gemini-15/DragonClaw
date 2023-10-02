import typer
import asyncio
from rich import print

from connection_handler.server import Server


def main(ip: str = "0.0.0.0", port: int = 4444):
    print("\n[dark_red]██████  ██████   █████   ██████   ██████  ███    ██  ██████ ██       █████  ██     ██ \n\
██   ██ ██   ██ ██   ██ ██       ██    ██ ████   ██ ██      ██      ██   ██ ██     ██ \n\
██   ██ ██████  ███████ ██   ███ ██    ██ ██ ██  ██ ██      ██      ███████ ██  █  ██ \n\
██   ██ ██   ██ ██   ██ ██    ██ ██    ██ ██  ██ ██ ██      ██      ██   ██ ██ ███ ██ \n\
██████  ██   ██ ██   ██  ██████   ██████  ██   ████  ██████ ███████ ██   ██  ███ ███[/dark_red]")
    
    loop = asyncio.get_event_loop()
    server = Server(loop, ip, port)
    
if __name__ == "__main__":
    typer.run(main)
