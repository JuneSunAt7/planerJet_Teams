import teams
import timer
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys

import datetime

class TeamsPlugin(QtWidgets.QWidget, teams.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_team)
        self.pushButton_2.clicked.connect(self.connect)
        self.pushButton_3.clicked.connect(self.settings)
        self.pushButton_4.clicked.connect(self.teams)

        self.__clear()
        self.connect()

    def __clear(self):
        self.frame.setVisible(False)
        self.frame_2.setVisible(False)
        self.frame_3.setVisible(False)
        self.frame_4.setVisible(False)
        self.frame_5.setVisible(False)

    def add_team(self):
        self.__clear()
        self.frame_2.setVisible(True)

    def connect(self):
        self.__clear()
        self.frame.setVisible(True)

    def settings(self):
        self.__clear()
        self.frame_3.setVisible(True)

    def teams(self):
        self.__clear()
        self.frame_5.setVisible(True)


def mainTeams():
    app = QtWidgets.QApplication(sys.argv)
    window = TeamsPlugin()
    window.setFixedSize(924, 682)
    window.show()
    app.exec_()
