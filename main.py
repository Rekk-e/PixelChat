import json
import os
from PySide2 import QtCore, QtGui, QtWidgets
import sys
from formС import Ui_ChatUi
from authform import Ui_Form
import socket
from PySide2.QtCore import QPluginLoader

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class Thread(QtCore.QThread):
    def __init__(self, MyWin, parent=None):
        super().__init__()
        self.mainwindow = MyWin

    def run(self):
        addr = self.mainwindow.address.split(':')
        host = addr[0]
        port = int(addr[1])
        soc.connect((host, port))
        senddata = {
            'nick':self.mainwindow.nick,
             'color':'yellow',
             'message':self.mainwindow.nick + ' connected to PixelChat!'
        }

        soc.send(bytes(json.dumps(senddata), 'utf-8'))
        data = soc.recv(1024).decode('utf-8')
        data = json.loads(data)
        self.mainwindow.ui.textEdit.append('<font color =' + data["color"] + '>' +
                                                             data["nick"] + '</font>' + "<font color = '#8E87AC'> >>> </font>" +
                                                             data["message"])
        while True:
            data = soc.recv(1024).decode('utf-8')
            data = json.loads(data)
            self.mainwindow.ui.textEdit.append('<font color =' + data["color"] +'>' +
                                                                 data["nick"] + '</font>' + "<font color = '#8E87AC'> >>> </font>" +
                                                                 data["message"])



class AuthForm(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(AuthForm, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.connect)

    def connect(self):
        self.Form = MyWin()
        self.Form.nick = self.ui.lineEdit.text()
        self.Form.color = self.ui.lineEdit_2.text()
        self.Form.address = self.ui.lineEdit_3.text()
        self.Form.show()
        self.close()


class MyWin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.ui = Ui_ChatUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.send)

        self.Thread_instance = Thread(MyWin=self)
        self.Thread_instance.start()
        self.ui.textEdit.setText('Use / help to get a list of commands')

    def launch(self):
        self.Thread_instance.start()

    def send(self):
        if self.ui.textEdit_2.toPlainText() != '/clear':
            self.user_settings = {'nick': self.nick,
                                  'color': self.color,
                                  'message': self.ui.textEdit_2.toPlainText()}

            data = json.dumps(self.user_settings)
            soc.send(bytes(data, 'utf-8'))
            text = self.ui.textEdit_2.toPlainText()
            if text != '/smile' and text != '/angry' and text != '/shock' and text != '/help':
                self.ui.textEdit.append('<font color =' +
                self.user_settings["color"] +'>' +
                self.user_settings["nick"] + '</font>' +
                "<font color = '#8E87AC'> >>> </font>" +
                self.user_settings["message"])

        else:
            self.ui.textEdit.clear()
        self.ui.textEdit_2.clear()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    auth = AuthForm()
    auth.show()

    sys.exit(app.exec_())
    soc.close()
