async def run(payload):
    a = payload.get("a")
    b = payload.get("b")
    return {"product": a * b}
