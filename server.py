import os
import platform

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    try:
        os.system()
    except Exception as e:
        return {"message": str(e)}
    finally:
        return {"message": "Success"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)
