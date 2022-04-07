import os
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": f" from docker {os.environ['HOSTNAME']}"}


@app.get("/version")
async def read_health():
    return {"version": "0.2"}


@app.get("/health")
async def read_health():
    return {"status": "OK"}

