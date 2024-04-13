import os
import signal
from contextlib import asynccontextmanager

from fastapi import FastAPI

from apps.project_crud import api as project_crud_api


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    os.kill(os.getpid(), signal.SIGTERM)


app = FastAPI(lifespan=lifespan)
app.include_router(project_crud_api.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to my API! If you would like to play around with the API, go to api.hendrywidyanto.com/docs"
    }
