import os

import uvicorn

from main import app

if __name__ == "__main__":
    os.system("sudo apt install unixodbc")
    uvicorn.run(app, host="0.0.0.0", port=8181)
