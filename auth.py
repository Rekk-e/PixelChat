# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 352)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 341, 51))
        font = QFont()
        font.setFamily(u"MS Serif")
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 150, 301, 41))
        font1 = QFont()
        font1.setFamily(u"MS Serif")
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 120, 101, 21))
        font2 = QFont()
        font2.setFamily(u"MS Serif")
        font2.setPointSize(13)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 290, 121, 41))
        font3 = QFont()
        font3.setFamily(u"MS Serif")
        font3.setPointSize(16)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0,0,0, 0));\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 200, 51, 21))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 230, 301, 41))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Welcome to Pixel Chat", None))
        self.lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Nickname", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Color", None))
        self.lineEdit_2.setText("")
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
/* Панель заголовка */
TitleBar {
    background-color: rgb(54, 157, 180);
}""")
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
