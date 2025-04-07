# src/swarmos_node.py
import socket
import threading
import psutil
import json
import os
import importlib.util

PORT = int(input("Enter port for this peer: "))
PEERS = {}  # {name: (ip, port)}

def handle_client(conn, addr):
    data = conn.recv(4096).decode()
    if data.startswith("TASK:"):
        payload = json.loads(data[5:])
        task = payload['task']
        args = payload['args']
        print(f"[TASK RECEIVED] {task} with args {args}")
        result = run_task(task, args)
        conn.sendall(result.encode())
    conn.close()

def run_task(task, args):
    try:
        path = f"tasks/{task}.py"
        if not os.path.exists(path):
            return f"[ERROR] Task {task} not found."
        spec = importlib.util.spec_from_file_location(task, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.run(args)
    except Exception as e:
        return f"[TASK ERROR] {str(e)}"

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", PORT))
    server.listen()
    print(f"[PEER STARTED] Listening on port {PORT}...")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

def send_task(target_port, task, args):
    s = socket.socket()
    s.connect(("localhost", target_port))
    payload = json.dumps({"task": task, "args": args})
    s.sendall(f"TASK:{payload}".encode())
    data = s.recv(4096).decode()
    print(f"[RESULT] {data}")
    s.close()

def print_resources():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    print(f"[RESOURCES] CPU: {cpu}%, RAM: {mem}%, Disk: {disk}%")

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    while True:
        cmd = input(">>> ")
        if cmd.startswith("send"):
            _, port, task, *args = cmd.split()
            send_task(int(port), task, args)
        elif cmd == "status":
            print_resources()
        elif cmd == "exit":
            break
