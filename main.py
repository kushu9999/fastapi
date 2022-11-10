from enum import Enum
from typing import Optional

from fastapi import FastAPI, status, Response

app = FastAPI()

@app.get("/hello")
def index():
    return {"message": "Hello World"}

