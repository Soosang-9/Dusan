from PyQt5 import QtWidgets
import uiFile.item as qt_item


class ItemWidget(QtWidgets.QWidget):
    def __init__(self, *values):
        QtWidgets.QWidget.__init__(self)
        self.ui = qt_item.Ui_Form()
        self.ui.setupUi(self)
        self.show()

        self.register_item_info(values)

    def register_item_info(self, values):
        self.ui.qt_value_count.setText('{}'.format(values[0]))
        self.ui.qt_value_lu.setText('{}'.format(values[1]))
        self.ui.qt_value_ld.setText('{}'.format(values[2]))
        self.ui.qt_value_ru.setText('{}'.format(values[3]))
        self.ui.qt_value_rd.setText('{}'.format(values[4]))
        self.ui.qt_value_time.setText('{}'.format(values[5]))