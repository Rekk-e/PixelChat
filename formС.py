# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_ChatUi(object):
    def setupUi(self, ChatUi):
        if not ChatUi.objectName():
            ChatUi.setObjectName(u"PixelChat")
        ChatUi.resize(441, 538)
        self.label = QLabel(ChatUi)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 441, 541))
        self.label.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_2 = QLabel(ChatUi)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 10, 361, 61))
        font = QFont()
        font.setFamily(u"MS Serif")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.textEdit = QTextEdit(ChatUi)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 80, 361, 371))
        font1 = QFont()
        font1.setFamily(u"MS Serif")
        font1.setPointSize(12)
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 170, 0);")
        self.textEdit.setFrameShape(QFrame.StyledPanel)
        self.textEdit.setReadOnly(True)
        self.pushButton = QPushButton(ChatUi)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(300, 460, 101, 51))
        font2 = QFont()
        font2.setFamily(u"MS Serif")
        font2.setPointSize(14)
        self.pushButton.setFont(font2)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0,0,0, 0));\n"
"color: rgb(255, 255, 255);")
        self.textEdit_2 = QTextEdit(ChatUi)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(40, 460, 251, 51))
        self.textEdit_2.setFont(font1)
        self.textEdit_2.setStyleSheet(u"border-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")

        self.retranslateUi(ChatUi)

        QMetaObject.connectSlotsByName(ChatUi)
    # setupUi

    def retranslateUi(self, ChatUi):
        ChatUi.setWindowTitle(QCoreApplication.translate("PixelChat", u"PixelChat", None))

        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("ChatUi", u"PixelChat", None))
        self.textEdit.setHtml(QCoreApplication.translate("ChatUi", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Serif'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("ChatUi", u"SEND", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
/* Панель заголовка */
TitleBar {
    background-color: rgb(54, 157, 180);
}""")
    Form = QWidget()
    ui = Ui_ChatUi()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())