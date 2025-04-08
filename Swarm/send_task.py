import requests

with open("testfile.txt", "r") as f:
    content = f.read()

task = {
    "type": "store",
    "payload": {
        "filename": "testfile.txt",
        "file_content": content
    }
}

response = requests.post("http://localhost:8080/task", json=task)
print("📨 Response:", response.text)
