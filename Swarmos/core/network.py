import aiohttp
import asyncio

class NetworkManager:
    def __init__(self, node):
        self.node = node
        self.peers = []

    async def discover_peers(self):
        # For manual testing, you can set known peers here:
        self.peers = [
            f"http://localhost:{other_port}/ping"
            for other_port in range(8001, 8003)
            if other_port != self.node.port
        ]
        print(f"[{self.node.name}] Discovered peers: {self.peers}")
