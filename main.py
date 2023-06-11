import datetime
import sys

import plyer
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

import design
import teamsLogic
import filemanagment
import timemanager

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.addButton.clicked.connect(self.add_task)
        self.currButton.clicked.connect(self.current_task)
        self.fireTaskButton.clicked.connect(self.fire_task)
        self.weekButton.clicked.connect(self.week_task)
        self.archiveButton.clicked.connect(self.arc_task)
        self.bthAdd.clicked.connect(self.save)
        self.tableWidget.itemDoubleClicked.connect(self.ready_task)
        self.delArchive.clicked.connect(self.deleteArc)
        self.tableWidget.itemClicked.connect(self.start_timers)
        self.teamsButton.clicked.connect(self.teams)

        self.difficultSlider.setRange(0, 5)
        self.difficultSlider.setValue(3)

        self.frame.setVisible(False)
        self.archiveData.setVisible(False)
        self.fireTasksFrame.setVisible(False)
        self.weekFrame.setVisible(False)
        data = ''
        for j in range(len(filemanagment.read_curr())):
            for i in range(4):
                print(len(filemanagment.read_curr()))
                if len(filemanagment.read_curr()) == 26:

                    self.tableWidget.setRowCount(0)
                else:
                    data = filemanagment.read_curr()[j].split('.')

                    self.tableWidget.setItem(j, i, QTableWidgetItem(data[i]))
                    self.tableWidget.item(j,i).setToolTip(data[i])
                    curr_date = datetime.date.today()
                    date_object = datetime.datetime.strptime(data[1], '%Y-%m-%d').date()
                    timeTask = str((date_object-curr_date).days) + ' days'
                    timer = (date_object-curr_date).days
                    if timer <= 3:
                        if i < 1:
                            plyer.notification.notify(message='Time to execute ' + str(data[0] + ' will end soon!'),
                                                      app_name='PlanerJet Teams',
                                                      title='Archive', )
                    self.tableWidget.setItem(j, 4, QTableWidgetItem(timeTask))
                    with open('stat.pj', 'r', encoding='utf-8') as timetracker:
                        for line in timetracker:
                            columns = line.split(';')
                            if columns == ['\r\n']:
                                pass
                            else:
                                if columns[0] == data[i]:
                                    self.tableWidget.item(j, 0).setBackground(QtGui.QColor(150, 255, 70))

        if len(filemanagment.read_curr()) != 0:
            filemanagment.m_to_archive()



    def __clear(self):
        self.frame.setVisible(False)
        self.archiveData.setVisible(False)
        self.fireTasksFrame.setVisible(False)
        self.weekFrame.setVisible(False)
        self.tableWidget.setVisible(False)

    def add_task(self):
        self.__clear()
        self.frame.setVisible(True)




    def current_task(self):
        self.__clear()
        self.tableWidget.setVisible(True)
        for j in range(len(filemanagment.read_curr())):
            for i in range(4):
                print(len(filemanagment.read_curr()))
                if len(filemanagment.read_curr()) == 26:
                    self.tableWidget.setItem(0, 0, QTableWidgetItem(''))
                else:
                    data = filemanagment.read_curr()[j].split('.')

                    self.tableWidget.setItem(j, i, QTableWidgetItem(data[i]))
                    curr_date = datetime.date.today()
                    date_object = datetime.datetime.strptime(data[1], '%Y-%m-%d').date()
                    timeTask = str((date_object-curr_date).days) + ' days'
                    self.tableWidget.setItem(j, 4, QTableWidgetItem(timeTask))
                    with open('stat.pj', 'r', encoding='utf-8') as timetracker:
                        for line in timetracker:
                            columns = line.split(';')
                            if columns == ['\r\n']:
                                pass
                            else:
                                if columns[0] == data[i]:
                                    self.tableWidget.item(j, 0).setBackground(QtGui.QColor(150, 255, 70))
                                    self.tableWidget.item(j, 1).setBackground(QtGui.QColor(150, 255, 70))
                                    self.tableWidget.item(j, 2).setBackground(QtGui.QColor(150, 255, 70))
                                    self.tableWidget.item(j, 3).setBackground(QtGui.QColor(150, 255, 70))
                                    self.tableWidget.item(j, 4).setBackground(QtGui.QColor(150, 255, 70))



    def fire_task(self):
        self.__clear()
        self.fireTasksFrame.setVisible(True)
        for j in range(len(filemanagment.read_fired())):
            for i in range(4):
                print(filemanagment.read_fired())
                if filemanagment.read_fired() == ['']:
                    pass
                else:
                    data = filemanagment.read_fired()[j].split('.')
                    if data == ['']:
                        pass
                    else:
                        self.firedTable.setItem(j, i, QTableWidgetItem(data[i]))

    def week_task(self):
        self.__clear()
        self.weekFrame.setVisible(True)
        for j in range(len(filemanagment.week_tasks())):
            for i in range(4):
                print(filemanagment.week_tasks())
                if filemanagment.week_tasks() == ['']:
                    pass
                else:
                    data = filemanagment.week_tasks()[j].split('.')
                    print(data)
                    self.mainTasksView.setItem(j, i, QTableWidgetItem(data[i]))

    def arc_task(self):
        self.__clear()
        self.archiveData.setVisible(True)
        self.arcTaskView.setText(filemanagment.read_arc())
        timemanager.statistics()

    def save(self):
        times = self.deadlineTime.date().toPyDate()
        filemanagment.wr_to_main_file(str(self.lineInputTask.text()), str(times), str(self.difficultSlider.value()), str(self.resoursesList.toPlainText()).replace("\n", '&'))
        self.__clear()
        self.tableWidget.setVisible(True)
        msg = QtWidgets.QMessageBox()
        msg.setText('Task '+ self.lineInputTask.text() + ' added')
        msg.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 255, 213, 255), stop:1 rgba(184, 170, 255, 255));\n"
"border-radius:15px;")
        msg.exec()
        for j in range(len(filemanagment.read_curr())):
            for i in range(4):
                print(len(filemanagment.read_curr()))
                if len(filemanagment.read_curr()) == 26:
                    pass
                else:
                    data = filemanagment.read_curr()[j].split('.')

                    self.tableWidget.setItem(j, i, QTableWidgetItem(data[i]))
                    curr_date = datetime.date.today()
                    date_object = datetime.datetime.strptime(data[1], '%Y-%m-%d').date()
                    timeTask = str((date_object-curr_date).days) + ' days'
                    self.tableWidget.setItem(j, 4, QTableWidgetItem(timeTask))

    def ready_task(self):
        row = self.tableWidget.currentRow()
        filemanagment.move_to_arch_custom(row, self.tableWidget.item(row, 0).text())
        timemanager.timer_end(self.tableWidget.item(row,0).text())
        if row > -1:
            self.tableWidget.removeRow(row)
            self.tableWidget.selectionModel().clearCurrentIndex()

    def start_timers(self):
        row = self.tableWidget.currentRow()
        self.tableWidget.item(row,0).setBackground(QtGui.QColor(150, 255, 70))

        timemanager.time_count(self.tableWidget.item(row,0).text())



    def deleteArc(self):
        filemanagment.delete()
        self.__clear()
        self.tableWidget.setVisible(True)
        msg = QtWidgets.QMessageBox()
        msg.setText('Archive deleted')
        msg.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
                          "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(170, 255, 213, 255), stop:1 rgba(184, 170, 255, 255));\n"
                          "border-radius:15px;")
        msg.exec()

    def teams(self):
        pass


def main():
    try:
        from ctypes import windll  # Only exists on Windows.
        myappid = 'gem13.PlanerJet.Teams.1.'
        windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    except ImportError:
        pass
    filemanagment.read_curr()
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('teams.ico'))
    window = ExampleApp()
    window.setWindowIcon(QtGui.QIcon('teams.ico'))
    window.show()
    window.setFixedSize(1150, 732)
    app.exec_()



if __name__ == '__main__':
    main()
