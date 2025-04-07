import asyncio
from core.node import SwarmNode
import json

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

async def main():
    config = load_config()
    node = SwarmNode(
        name=config['name'],
        port=config['port'],
        memory=config['memory']
    )
    await node.start()

if __name__ == '__main__':
    asyncio.run(main())
