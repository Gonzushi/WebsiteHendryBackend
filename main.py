import os
import signal
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.analytics import api as analytics_api
from apps.project_crud import api as project_crud_api
from apps.project_map import api as project_map_api


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_dotenv()
    yield
    os.kill(os.getpid(), signal.SIGTERM)


app = FastAPI(lifespan=lifespan)
app.include_router(project_crud_api.router)
app.include_router(analytics_api.router)
app.include_router(project_map_api.router)


origins = [
    "http://localhost:5173",
    "https://hendrywidyanto.com",
    "https://www.hendrywidyanto.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Welcome to my API! If you would like to play around with the API, go to api.hendrywidyanto.com/docs"
    }
