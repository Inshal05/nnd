import requests

task = {
    "type": "zip",
    "payload": {
        "filename": "myself.txt"
    }
}

response = requests.post("http://localhost:8080/task", json=task)
print("📨 Response:", response.text)
