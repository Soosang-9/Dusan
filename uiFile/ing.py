# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ing.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ing(object):
    def setupUi(self, Connect):
        Connect.setObjectName("Connect")
        Connect.resize(359, 255)
        Connect.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Connect.setStyleSheet("background:rgb(255, 213, 44);\n"
"font: bold 18pt \"나눔고딕\";\n"
"color:rgb(44, 44, 44);\n"
"")
        self.label = QtWidgets.QLabel(Connect)
        self.label.setGeometry(QtCore.QRect(20, 60, 331, 121))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setStyleSheet("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Connect)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        _translate = QtCore.QCoreApplication.translate
        Connect.setWindowTitle(_translate("Connect", "Dialog"))
        self.label.setText(_translate("Connect", "측정중입니다. . ."))

