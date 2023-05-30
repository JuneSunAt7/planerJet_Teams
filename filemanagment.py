import os
import csv
from PyQt5 import QtWidgets  # for message about errors
import datetime
import re
import pandas as pd
import plyer

def read_curr():
    s = ''
    if int(os.stat('CURR.csv').st_size) == 0:
        return 'data.2023-01-01.not.found('
    with open('CURR.csv', newline='', encoding='utf-8') as csvfile:
        for line in csvfile:
            columns = line.split(';')
            if columns == ['\r\n']:
                pass
            else:
                s += columns[0] + '.' +columns[1]+'.'+columns[2]+'.'+columns[3]
                print(s)
    s = s.replace("task deadline diff resources", '')

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')

    return parse


def read_fired():
    s = ''
    with open('CURR.csv', 'r', encoding='utf-8') as source:
        for line in source:

            columns = line.split(';')
            if columns == ['\n']:
                pass
            else:
                curr_date = datetime.date.today()
                date_object = datetime.datetime.strptime(columns[1], '%Y-%m-%d').date()
                if (date_object - curr_date).days <= 4:
                    if (date_object - curr_date).days > 0:
                        s += columns[0] + '.' + columns[1] + '.' + columns[2] + '.' + columns[3]
    s = s.replace("task deadline diff resources", '')

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')

    return parse


def read_arc():
    s = ''
    with open('ARC.csv', newline='', encoding='utf-8') as csvfile:
        for line in csvfile:
            columns = line.split(';')
            s += str('Task: '+columns[0] + ' archived: ' + columns[1] + '\n').replace('"', '')
    print(s)

    return s

def m_to_archive():
    with open('CURR.csv', 'r', encoding='utf-8') as f:
        lines = f.read().split()
        print('lines')
        print(lines)
    s = ''
    with open('CURR.csv', 'r', encoding='utf-8') as source:
        for line in source:
            columns = line.split(';')
            if columns == ['\n']:
                pass
            else:
                curr_date = datetime.date.today()
                date_object = datetime.datetime.strptime(columns[1], '%Y-%m-%d').date()
                if (date_object - curr_date).days < 0:
                    s += columns[0] + '.' + columns[1] + '.' + columns[2] + '.' + columns[3]
                    plyer.notification.notify(message='Task ' + str(columns[0] + ' moved to archive'),
                                              app_name='PlanerJet Alone',
                                              title='Archive', )

                    with open('ARC.csv', 'a+', encoding='utf-8') as arc:
                        arc.write(columns[0] + ';' + str(curr_date) + '\n')
                    lines.remove(line.replace('\n', ''))
    s = s.replace("\n", ',')
    with open('CURR.csv', 'w', encoding='utf-8') as rewrite:
        for elem in lines:
            rewrite.write('\n'+elem)


def move_to_arch_custom(element, data):
    with open('CURR.csv', 'r', encoding='utf-8') as f:
        lines = f.read().split()
        print('lines')
        print(lines)
        print(str(element))
    curr_date = datetime.date.today()
    plyer.notification.notify(message='Task ' + str(data) + ' moved to archive', app_name='PlanerJet Alone', title='Archive', )
    lines.pop(element)
    with open('ARC.csv', 'a+', encoding='utf-8') as arc:
        arc.write(str(data) + ';' + str(curr_date) + '\n')
    with open('CURR.csv', 'w', encoding='utf-8') as rewrite:
        for elem in lines:
            rewrite.write('\n'+elem)




def wr_to_main_file(taskname, deadline, diff, resources):
    data = str(taskname).replace('\n', ' ').replace(',', ' ')+';'+ deadline+';'+ diff+';'+ str(resources).replace('\n', ' ').replace(',', ' ')

    with open('CURR.csv', 'a', encoding='utf-8') as file:
        file.write('\n'+data)

def week_tasks():
    s = ''
    with open('CURR.csv', 'r', encoding='utf-8') as source:
        for line in source:
            columns = line.split(';')
            if columns == ['\n']:
                pass
            else:
                curr_date = datetime.date.today()
                date_object = datetime.datetime.strptime(columns[1], '%Y-%m-%d').date()
                if (date_object - curr_date).days <= 7:
                    if (date_object - curr_date).days >= 0:
                        s += columns[0] + '.' +columns[1]+'.'+columns[2]+'.'+columns[3]
    s = s.replace("task deadline diff resources", '')

    s = s.replace("\n", ',')
    parse = s.strip('[]').replace("\r", "").split(',')

    return parse

def delete():
    with open('ARC.csv', 'w', encoding='utf-8') as delMe:
        delMe.write('')



def rm_all():
    pass



