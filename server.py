import platform

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "\n".join([str(platform.platform())])}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)
