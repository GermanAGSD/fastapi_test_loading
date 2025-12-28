import threading

from fastapi import FastAPI
import uvicorn
import time
import asyncio


app = FastAPI()

@app.get("/sync/{id}")
def sync_func(id: int):
    print(f"Кол-во потоков {threading.active_count()}")
    print(f"sync start {id}: {time.time():2f}")
    time.sleep(3)
    print(f"sync end {id}: {time.time():2f}")

@app.get("/async/{id}")
async def async_func(id: int):
    print(f"Кол-во потоков {threading.active_count()}")
    print(f"async start {id}: {time.time():2f}")
    await asyncio.sleep(3)
    print(f"async end {id}: {time.time():2f}")

# Количество открытых сессий workers
# uvicorn.run("main:app", host="192.168.3.2", port=8001, workers=5)

if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.3.2", port=8001)
