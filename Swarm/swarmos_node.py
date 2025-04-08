import asyncio
from aiohttp import web
from core.node import SwarmNode
import json

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

async def start_node():
    config = load_config()
    node = SwarmNode(
        name=config['name'],
        port=config['port'],
        memory=config['memory']
    )
    await node.start()

    app = web.Application()
    app.add_routes([web.post('/task', node.handle_task)])

    print(f"[{node.name}] Node running on port {node.port}")
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, 'localhost', node.port)
    await site.start()

    # Keep running forever
    while True:
        await asyncio.sleep(3600)

if __name__ == '__main__':
    asyncio.run(start_node())
