from core.tasks import add, store, status, unzip, zipfile_task

async def handle_task(task):
    task_type = task.get("type")
    payload = task.get("payload", {})

    if task_type == "add":
        return add.perform(payload)
    elif task_type == "store":
        return store.perform(payload)
    elif task_type == "status":
        return status.perform(payload)
    elif task_type == "unzip":
        return unzip.perform(payload)
    elif task_type == "zip":
        return zipfile_task.perform(payload)
    else:
        return {"error": "Unknown task type"}
