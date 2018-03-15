# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt, QRectF, QPoint
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QGraphicsItem


class DrawCircles(QGraphicsItem):
    def __init__(self, x, y):
        QGraphicsItem.__init__(self)
        self.x = x
        self.y = y

    # 사용하지 않지만 반드시 선언해주어야 한다.
    def boundingRect(self):
        return QRectF(self.x, self.y, 50, 50)

    def paint(self, painter, option, widget=None):
        rec = self.boundingRect()
        pen = QPen()
        pen.setWidth(6)
        pen.setColor(Qt.red)
        painter.setPen(pen)
        painter.setBrush(Qt.yellow)
        painter.setRenderHint(painter.Antialiasing)

        center = QPoint(self.x, self.y)

        # painter.fillRect(rec, Qt.white)
        painter.drawEllipse(center, 50, 50)
    #    painter.drawRect(rec)