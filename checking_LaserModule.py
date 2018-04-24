from PyQt5 import QtWidgets
from PyQt5 import uic

import custom_socket as socket
import uiFile.main  as qt_main
import uiFile.item as qt_item

import sys


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = qt_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

    def slot_ok(self):
        pass

if __name__ == '__main__':

    # socket
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow()

    if not app.exec_():
        print 'push'


