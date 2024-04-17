import platform
import uvicorn

from fastapi import FastAPI

str(platform.uname())

app = FastAPI()


@app.get("/")
def home():
    return {"message": str(platform.uname())}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)