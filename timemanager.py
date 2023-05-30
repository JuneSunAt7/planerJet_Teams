from threading import Thread
import main
import design
import filemanagment
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt


def time_count(task):
    timer_start = datetime.datetime.now()
    with open('stat.pj', 'a+', encoding='utf-8') as timer:
        timer.write('\n'+str(task) + ';' + timer_start.strftime('%Y-%m-%d %H-%M')+';')


def timer_end(task):
    timer_start = datetime.datetime.now()
    with open("stat.pj", "r", encoding='utf-8') as f:
        data = f.readlines()

    def transformation(line):
        if task in line:
            line = line.replace('\n','') + timer_start.strftime('%Y-%m-%d %H-%M')+'\n'

        return line
    data = map(transformation, data)
    data = set(data)
    with open("stat.pj", "w", encoding='utf-8') as f:

        f.write(''.join(data))


def statistics():
    data = ''
    memory = []
    names = []
    with open('stat.pj', 'r', encoding='utf-8') as timer:
        for line in timer:
            columns = line.split(';')
            if columns == ['\n']:
                pass
            else:
                if len(columns) < 3:
                    pass
                else:
                    data += columns[0] + '.' + columns[1] + '.' +columns[2]

    data = data.replace("\n", ',')
    parse = data.strip('[]').replace("\r", "").split(',')


    for i in range(len(parse)):
        stat = parse[i].strip('[]').split('.')
        if stat == ['']:
            pass
        else:
            if stat[2] == '':
                pass
            else:
                tdelta = (datetime.datetime.strptime(stat[2], '%Y-%m-%d %H-%M') - datetime.datetime.strptime(stat[1], '%Y-%m-%d %H-%M')).seconds / 3600
                memory.append(tdelta)
                names.append(stat[0])

    plt.xlabel('Tasks')
    plt.ylabel('Hours')
    plt.bar(x=names, height=memory, color=['green'])
    plt.title('Statistics')
    plt.show()


def computer_time():

    pass
