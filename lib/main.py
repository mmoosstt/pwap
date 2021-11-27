import sys
import asyncio
import socket
import uvicorn 
import traceback

from spos.storage.db.setup import setupDatabase
from spos.ui.app import client
from spos.config import config, report

setupDatabase(config['database'])

class MyServer(uvicorn.Server):
    
    async def run(self, sockets=None):
        self.config.setup_event_loop()
        return await self.serve(sockets=sockets)
    


async def run():
    apps = []
    
    # find free ports on localhost
    
    if config['port'] is None:
        sock1 = socket.socket() 
        sock1.bind(("", 0))
        _, port1 = sock1.getsockname()
        sock1.close()
        config['port'] = port1
    
    port1 = 8008
    #port1 = config['port']
    
    server1 = MyServer(config=uvicorn.Config("spos.api.setup:app", host=config['host'], port=port1))
    qtTask = asyncio.ensure_future(client.qt_loop(port1, [server1]))
    
    apps.append(server1.run())
    apps.append(qtTask)
    
    return await asyncio.gather(*apps)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(run())
    except:
        traceback.print_exc()
        loop.close()
        
    print("done-SPOS")