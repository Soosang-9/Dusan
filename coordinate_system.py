# -*- coding: utf-8 -*-

# made by Leni.
# 2017.11.14.Tuesday - test start.

# import uiFile.
from uiFile.main import Ui_MainWindow

# import PyQt5 modules.
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsLineItem

# import other modules.
import sys
import numpy as np


from Dusan.test import DrawCircles


# make Main_Function class.
class MainFunction(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.round = 50

        # set range.
        self.gScene = QGraphicsScene(0, 0, self.ui.graphicsView.width()-5, self.ui.graphicsView.height()-5, self.ui.graphicsView)
        print 'graphics View x %f', self.ui.graphicsView.width()
        print 'graphics View y %f', self.ui.graphicsView.height()
        self.ui.graphicsView.setScene(self.gScene)

        # test circle
        self.circle = QGraphicsEllipseItem()
        red = QBrush(Qt.red)
        pen = QPen(Qt.black)
        pen.setWidth(6)

        # test line
        self.x_line = QGraphicsLineItem(self.gScene.width()/2, 0, self.gScene.width()/2, self.gScene.height())
        self.gScene.addItem(self.x_line)
        self.y_line = QGraphicsLineItem(0, self.gScene.width()/2, self.gScene.height(), self.gScene.width()/2)
        self.gScene.addItem(self.y_line)

        #self.circle2 = DrawCircles(int(self.gScene.width()/2), int(self.gScene.height()/2))
        #self.gScene.addItem(self.circle2)

        print 'gScene View x %f', self.gScene.width()/2
        print 'gScene View y %f', self.gScene.height()/2

        self.circle = self.gScene.addEllipse(self.gScene.width()/2-self.round, self.gScene.height()/2-self.round,
                                             self.round*2, self.round*2, pen, red)

        # check Item argv.
        self.g_item = QGraphicsRectItem(self.gScene.width()/2, self.gScene.height()/2, 100, 100)
        self.gScene.addItem(self.g_item)
        self.g1_item = QGraphicsRectItem(self.gScene.width()/2, self.gScene.height()/2, 100, 100)
        self.gScene.addItem(self.g1_item)
        # self.gScene.addItem(self.circles)
        self.show()

    def slot_ok(self):
        random_x = np.random.random_integers(-300, 300)
        random_y = np.random.random_integers(-300, 300)

        # 값 조정은 display로 한다.
        self.ui.layer_a.display(100)

        tip = ''
        self.circle.setPos(float(random_x), float(random_y))
        self.g1_item.setPos(float(random_x), float(random_y))

        print 'x > %s' % self.g_item.x()
        print 'circle -> %d' % self.circle.x()
        print 'circle -> %d' % self.circle.y()

        if self.g_item.x() != self.circle.x():
            tip += ' move x > %f\n' % (self.g_item.x() - self.circle.x())
        if self.g_item.y() != self.circle.y():
            tip += ' move y > %f' % (self.g_item.y() - self.circle.y())

        self.ui.information.setText(tip)


# start Main process.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainFunction = MainFunction()
    sys.exit(app.exec_())
