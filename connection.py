import base64

from PyQt5 import QtGui
from PyQt5 import QtWidgets
import ssl
import pybase64
import socket

def gen_key():
    cert = open('certPJ.cr', 'w')

    getip = str(socket.gethostbyname(socket.gethostname()))
    data = getip.encode('utf-8')

    data_cert = base64.b64encode(data)
    cert.write(str(data_cert).replace('b', ''))
    cert.close()

    return str(data_cert).replace('b', '')


class InputConnect: # server
    def __init__(self):
        pass


class OutputConnect: # client
    def __init__(self):
        pass

    def connection(self, ip, data):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, 55000))
        sock.send(bytes(str(data), encoding='UTF-8'))
        data = sock.recv(1024)
        sock.close()
        print(data)
