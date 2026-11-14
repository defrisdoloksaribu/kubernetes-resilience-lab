from main import app

@app.middleware("http")
async def add_version_header(request, call_next):
    response = await call_next(request)
    response.headers["X-App-Version"] = "v2"
    return response
