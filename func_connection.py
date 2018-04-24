# -*- coding:utf-8 -*-

from uiFile.connect import Ui_Connect
from info_socket import *

from PyQt5.QtWidgets import QDialog, QMessageBox

import sys


class Connection(QDialog):
    def __init__(self, th):
        QDialog.__init__(self)
        self.ui = Ui_Connect()
        self.ui.setupUi(self)
        self.show()

        self.th = th

    def slot_start(self):
        # socket connect
        self.th.connect(self)
        self.close()



