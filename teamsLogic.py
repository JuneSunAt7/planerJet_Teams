import teams
import timer
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys
import connection
import datetime


class TeamsPlugin(QtWidgets.QMainWindow, teams.Ui_Form):
    def __init__(self, parent=None):
        super(TeamsPlugin, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.add_team)
        self.pushButton_2.clicked.connect(self.connect)
        self.pushButton_3.clicked.connect(self.settings)
        self.pushButton_4.clicked.connect(self.teams)
        self.pushButton_5.clicked.connect(self.senderMess)

        self.__clear()
        self.connect()
        connection.gen_key()

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

    def senderMess(self):
        self.progressBar.setVisible(True)
        self.progressBar.setRange(0,100)
        self.progressBar.setValue(11)



def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('teams.ico'))
    window = TeamsPlugin()
    window.setWindowIcon(QtGui.QIcon('teams.ico'))
    window.show()
    window.setFixedSize(924, 682)
    app.exec_()

if __name__ == "__main__":

    main()



