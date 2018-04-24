# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Connect(object):
    def setupUi(self, Connect):
        Connect.setObjectName("Connect")
        Connect.resize(400, 300)
        Connect.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label = QtWidgets.QLabel(Connect)
        self.label.setGeometry(QtCore.QRect(70, 120, 261, 23))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Connect)
        self.pushButton.setGeometry(QtCore.QRect(150, 160, 104, 31))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Connect)
        self.pushButton.clicked.connect(Connect.slot_start)
        QtCore.QMetaObject.connectSlotsByName(Connect)

    def retranslateUi(self, Connect):
        _translate = QtCore.QCoreApplication.translate
        Connect.setWindowTitle(_translate("Connect", "Dialog"))
        self.label.setText(_translate("Connect", "프로그램을 시작합니다."))
        self.pushButton.setText(_translate("Connect", "시작"))

