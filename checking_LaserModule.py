from PyQt5 import QtWidgets

import custom_socket as socket

import uiFile.main  as qt_main
import item_widget

import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = qt_main.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.open_dialog_list = []

    def slot_measurement(self):
        item = QtWidgets.QListWidgetItem("data")
        self.ui.qt_listWidget.addItem(item)
        self.ui.qt_listWidget.setItemWidget(item, item_widget.ItemWidget(1, 2, 3, 4, 5, 6))
        self.ui.qt_scrollArea.setWidgetResizable(True)

        for dialog in self.open_dialog_list:
            dialog.close()

    def slot_item_checked(self):
        widget = self.ui.qt_listWidget.itemWidget(self.sender().currentItem())
        dialog = QtWidgets.QDialog(self)
        dialog.setFixedSize(544, 136)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(widget)
        dialog.setLayout(layout)
        dialog.show()
        self.open_dialog_list.append(dialog)


if __name__ == '__main__':

    # socket
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    if not app.exec_():
        print 'push'


