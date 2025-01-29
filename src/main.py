import sys
from fastapi import FastAPI
from PyQt5.QtWidgets import QApplication
from .frontend import MainWindow
from .calls import basic_call
from .routers import router
import subprocess
import uvicorn

api = FastAPI()
api.include_router(router)

def start_api():
    uvicorn.run("src.main:api", host="127.0.0.1", port=8000, reload=True)

def start_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

def main():

    start_api()

if __name__ == "__main__":
    main()