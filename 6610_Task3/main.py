from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/sync")
def sync_endpoint():
    start = time.time()
    time.sleep(2)
    end = time.time()

    execution_time = end - start

    return {
        "message": "Sync response",
        "execution_time_seconds": round(execution_time, 3)
    }

@app.get("/async")
async def async_endpoint():
    start = time.time()
    await asyncio.sleep(2)
    end = time.time()

    execution_time = end - start

    return {
        "message": "Async response",
        "execution_time_seconds": round(execution_time, 3)
    }
