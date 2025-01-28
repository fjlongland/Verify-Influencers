import sys
from PyQt5.QtWidgets import QApplication
from .frontend import MainWindow
from .calls import basic_call

def main():

    question = "tell me a joke."

    #basic_call(question)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()