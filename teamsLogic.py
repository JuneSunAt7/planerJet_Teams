import teams
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys

class ExampleApp(QtWidgets.QWidget, teams.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

