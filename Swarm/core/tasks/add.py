def perform(payload):
    a = payload.get("a")
    b = payload.get("b")
    if a is not None and b is not None:
        return {"sum": a + b}
    return {"error": "Missing values"}
