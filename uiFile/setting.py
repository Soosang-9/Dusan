# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_page.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        SettingWindow.setObjectName("SettingWindow")
        SettingWindow.resize(696, 437)
        SettingWindow.setMinimumSize(QtCore.QSize(696, 437))
        SettingWindow.setMaximumSize(QtCore.QSize(696, 437))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        SettingWindow.setFont(font)
        SettingWindow.setStyleSheet("QPushButton{\n"
"background: rgb(209, 209, 209);\n"
"font: normal;\n"
"outline:none;\n"
"}\n"
"QPushButton:hover{\n"
"  background:rgb(21, 21, 21);\n"
"  color:rgb(255, 255, 255);\n"
"  border: 2px solid rgb(209, 209, 209);\n"
"}\n"
"*{ background-color:rgb(255, 255, 255); font: \"나눔고딕\"; }")
        self.centralwidget = QtWidgets.QWidget(SettingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_laser = QtWidgets.QPushButton(self.centralwidget)
        self.btn_laser.setGeometry(QtCore.QRect(30, 290, 201, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_laser.setFont(font)
        self.btn_laser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_laser.setObjectName("btn_laser")
        self.btn_chuck_default = QtWidgets.QPushButton(self.centralwidget)
        self.btn_chuck_default.setGeometry(QtCore.QRect(250, 290, 201, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_chuck_default.setFont(font)
        self.btn_chuck_default.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_chuck_default.setObjectName("btn_chuck_default")
        self.btn_laser_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_laser_set.setGeometry(QtCore.QRect(470, 350, 201, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_laser_set.setFont(font)
        self.btn_laser_set.setObjectName("btn_laser_set")
        self.btn_coor_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_coor_set.setGeometry(QtCore.QRect(30, 350, 201, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_coor_set.setFont(font)
        self.btn_coor_set.setObjectName("btn_coor_set")
        self.btn_chuck_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_chuck_set.setGeometry(QtCore.QRect(250, 350, 201, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_chuck_set.setFont(font)
        self.btn_chuck_set.setObjectName("btn_chuck_set")
        self.btn_frame_set = QtWidgets.QPushButton(self.centralwidget)
        self.btn_frame_set.setGeometry(QtCore.QRect(470, 290, 201, 51))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_frame_set.setFont(font)
        self.btn_frame_set.setObjectName("btn_frame_set")
        self.setting_com = QtWidgets.QLineEdit(self.centralwidget)
        self.setting_com.setEnabled(False)
        self.setting_com.setGeometry(QtCore.QRect(30, 240, 641, 35))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.setting_com.setFont(font)
        self.setting_com.setInputMask("")
        self.setting_com.setText("")
        self.setting_com.setPlaceholderText("")
        self.setting_com.setObjectName("setting_com")
        self.setting_info = QtWidgets.QLabel(self.centralwidget)
        self.setting_info.setGeometry(QtCore.QRect(30, 20, 641, 201))
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.setting_info.setFont(font)
        self.setting_info.setFrameShape(QtWidgets.QFrame.Box)
        self.setting_info.setText("")
        self.setting_info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.setting_info.setObjectName("setting_info")
        SettingWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SettingWindow)
        self.statusbar.setObjectName("statusbar")
        SettingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SettingWindow)
        self.btn_chuck_default.clicked.connect(SettingWindow.slot_ok)
        self.btn_laser.clicked.connect(SettingWindow.slot_locate)
        self.btn_frame_set.clicked.connect(SettingWindow.slot_action)
        self.btn_laser_set.clicked.connect(SettingWindow.slot_action)
        self.btn_chuck_set.clicked.connect(SettingWindow.slot_action)
        self.btn_coor_set.clicked.connect(SettingWindow.slot_action)
        QtCore.QMetaObject.connectSlotsByName(SettingWindow)

    def retranslateUi(self, SettingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingWindow.setWindowTitle(_translate("SettingWindow", "MainWindow"))
        self.btn_laser.setText(_translate("SettingWindow", "레이저 위치 설정"))
        self.btn_chuck_default.setText(_translate("SettingWindow", "척 기본값 설정"))
        self.btn_laser_set.setText(_translate("SettingWindow", "레이저 사이 간격 설정"))
        self.btn_coor_set.setText(_translate("SettingWindow", "좌표계 보정값 설정"))
        self.btn_chuck_set.setText(_translate("SettingWindow", "척 보정값 설정"))
        self.btn_frame_set.setText(_translate("SettingWindow", "프레임 길이 설정"))
