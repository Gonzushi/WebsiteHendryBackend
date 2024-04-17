import os
import platform

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    try:
        command = """
if ! [[ "18.04 20.04 22.04 23.04" == *"$(lsb_release -rs)"* ]];
then
    echo "Ubuntu $(lsb_release -rs) is not currently supported.";
    exit;
fi"""
        os.system()
    except Exception as e:
        return {"message": str(e)}
    finally:
        return {"message": "Success"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8181)
