async def run(payload):
    code = payload.get("code")
    local_vars = {}
    try:
        exec(code, {}, local_vars)
        return {"output": local_vars}
    except Exception as e:
        return {"error": str(e)}
