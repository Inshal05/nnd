import aiohttp
from aiohttp import web
import asyncio
import json
import importlib
import os
from core.network import NetworkManager

class SwarmNode:
    def __init__(self, name, port, memory=1024):
        self.name = name
        self.port = port
        self.memory = memory
        self.app = web.Application()
        self.peers = []
        self.network = NetworkManager(self)
        self.setup_routes()

    def setup_routes(self):
        self.app.add_routes([
            web.get('/ping', self.handle_ping),
            web.post('/task', self.handle_task),
        ])

    async def start(self):
        print(f"[{self.name}] Starting on port {self.port}")
        await self.network.discover_peers()
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, '0.0.0.0', self.port)
        await site.start()
        print(f"[{self.name}] Ready to receive tasks...")
        while True:
            await asyncio.sleep(3600)

    async def handle_ping(self, request):
        return web.json_response({'status': 'alive', 'name': self.name})

    async def handle_task(self, request):
        try:
            data = await request.json()
            task_type = data.get('type')
            payload = data.get('payload')
            print(f"[{self.name}] Received task: {task_type}")
            result = await self.execute_task(task_type, payload)
            return web.json_response({'result': result})
        except Exception as e:
            return web.json_response({'error': str(e)})

    async def execute_task(self, task_type, payload):
        try:
            module = importlib.import_module(f"tasks.{task_type}")
            result = await module.run(payload)
            return result
        except ModuleNotFoundError:
            return f"Task module '{task_type}' not found"
        except Exception as e:
            return str(e)
