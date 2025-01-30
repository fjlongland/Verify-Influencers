import os
import sys
from fastapi import FastAPI
#from PyQt5.QtWidgets import QApplication
#from .frontend import MainWindow
from .calls import basic_call
from .routers import router
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import uvicorn

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

api.include_router(router)



def start_api():
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("src.main:api", host="0.0.0.0", port=port, reload=True)

#def start_app():
    #app = QApplication(sys.argv)
    #window = MainWindow()
    #window.show()
    #sys.exit(app.exec_())

def main():

    #start_app()
    start_api()

if __name__ == "__main__":
    main()