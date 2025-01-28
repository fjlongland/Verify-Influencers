from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from .calls import about_influencer_call
import threading


class InfoFetcherThread(QThread):
    info_fetched = pyqtSignal(str)

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        info = about_influencer_call(self.name)
        self.info_fetched.emit(info)



class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle("Verify Influencers")
        self.setGeometry(30, 40, 1000, 1000)
        self.setWindowIcon(QIcon("green shield.jpg"))

        self.SecondWindow = None

        #////////////////Layout///////////////////////////////

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)
        
        #/////////////////name lable//////////////////////////////

        self.lblName = QLabel("Influencer Name: ", self)

        #/////////////////name feild//////////////////////////////

        self.txtIName = QLineEdit(self)

        #//////////////////search button/////////////////////////////

        self.btnSearch = QPushButton("Search", self)
        self.btnSearch.setFixedSize(150, 50)
        self.btnSearch.clicked.connect(lambda: self.search_clicked(self.txtIName.text()))

        #////////////////////spacing///////////////////////////

        layout.addWidget(self.lblName, 1, 1)
        layout.addWidget(self.txtIName, 1, 3)
        layout.addWidget(self.btnSearch, 5, 2)

        #/////////////////////layout improvement//////////////////////////

        layout.setRowStretch(0, 1)
        layout.setRowStretch(6, 1)
        layout.setRowStretch(2, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(4, 1)




    def search_clicked(self, name):

        if not self.SecondWindow:
            self.SecondWindow = SecondWindow(name)

        self.SecondWindow.show()


class SecondWindow(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setWindowTitle("Verify Influencers")
        self.setGeometry(30, 40, 1000, 1000)
        self.setWindowIcon(QIcon("green shield.jpg"))

        #///////////////////////////////////////////////////

        layout = QGridLayout(self)

        #/////////////////////////////////////////////////////

        self.lblNameDisplay = QLabel(name)

        #////////////////////////////////////////////////////

        self.txtAbout = QTextEdit()
        self.txtAbout.setReadOnly(True)

        #///////////////////////////////////////////////////

        self.lblTrustScore = QLabel("Trust Score:")

        self.lblYearlyRev = QLabel("Yearly Revenue:")

        self.lblProducts = QLabel("Products:")

        self.lblFollowers = QLabel("Followers:")

        #///////////////////////////////////////////////////

        self.txtTrustscore = QTextEdit()

        self.txtYearlyRev = QTextEdit()

        self.txtProducts = QTextEdit()

        self.txtFollowers = QTextEdit()

        #///////////////////////////////////////////////////

        layout.addWidget(self.lblNameDisplay, 0, 0)
        layout.addWidget(self.txtAbout, 1, 0, 1, 4)
        layout.addWidget(self.lblTrustScore, 2, 0)
        layout.addWidget(self.lblYearlyRev, 2, 1)
        layout.addWidget(self.lblProducts, 2, 2)
        layout.addWidget(self.lblFollowers, 2, 3)
        layout.addWidget(self.txtTrustscore, 3, 0)
        layout.addWidget(self.txtYearlyRev, 3, 1)
        layout.addWidget(self.txtProducts, 3, 2)
        layout.addWidget(self.txtFollowers, 3, 3)

        #//////////////////////////////////////////////////

        layout.setRowStretch(4, 1)

        self.setLayout(layout)

        #//////////////////////////////////////////////////

        self.fetch_influencer_info(name)

    def fetch_influencer_info(self, name):
    
        self.txtAbout.setText("Fetching information...")
        self.thread = InfoFetcherThread(name)
        self.thread.info_fetched.connect(self.update_info_display)
        self.thread.start()

    def update_info_display(self, info):
        self.txtAbout.setText(info)