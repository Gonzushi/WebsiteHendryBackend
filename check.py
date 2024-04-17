import platform

from fastapi import FastAPI

str(platform.uname())

app = FastAPI()


@app.get("/")
def home():
    return {"message": str(platform.uname())}
