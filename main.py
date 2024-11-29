from PyQt6.QtCore import Qt, QPointF, QRectF
from random import randint as ri
import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6.QtGui import QPainter, QColor, QPolygonF
from math import sin, cos, pi


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.STAT = 0
        self.coords = (None, None)
        self.flag = False
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('Суперматизм')

    def pin(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_flag(self.qp)
            self.qp.end()
        # self.flag = False

    def draw_flag(self, qp):
        D = ri(20, 100)
        r, g, b = ri(0, 255), ri(0, 255), ri(0, 255)
        qp.setBrush(QColor(r, g, b))
        x, y = self.coords
        if self.STAT == 1:
            qp.drawEllipse(QPointF(x, y), D, D)
        if self.STAT == 2:
            x, y = x - D / 2, y - D / 2
            qp.drawRect(QRectF(x, y, D, D))
        elif self.STAT == 3:
            coords = QPolygonF([QPointF(x, y - D),
                                QPointF(x + cos(7 * pi / 6) * D,
                                        y - sin(7 * pi / 6) * D),
                                QPointF(x + cos(11 * pi / 6) * D,
                                        y - sin(11 * pi / 6) * D)])
            self.qp.drawPolygon(coords)
        self.STAT = 0

    def mouseMoveEvent(self, event):
        self.coords = event.pos().x(), event.pos().y()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Space:
            self.STAT = 3
            self.pin()
            # треугольник

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.STAT = 1
            self.pin()
        if event.button() == Qt.MouseButton.RightButton:
            self.STAT = 2
            self.pin()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())



