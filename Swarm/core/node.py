import json
from aiohttp import web
from core.network import NetworkManager
from core.tasks.task_handler import handle_task

class SwarmNode:
    def __init__(self, name, port, memory):
        self.name = name
        self.port = port
        self.memory = memory
        self.app = web.Application()
        self.app.router.add_post('/task', self.handle_task)
        self.network = NetworkManager()

    async def handle_task(self, request):
        data = await request.json()
        print(f"[{self.name}] Received task: {data.get('type')}")
        result = await handle_task(data)
        return web.json_response({"result": result})

    async def start(self):
        runner = web.AppRunner(self.app)
        await runner.setup()
        site = web.TCPSite(runner, port=self.port)
        print(f"[{self.name}] Node running on port {self.port}")
        await site.start()
