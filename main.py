import random
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow


class CirclesWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.flag = False
        self.list_ellipses = [[]]
        self.setWindowTitle("Git и желтые окружности")
        self.loadUI()

    def loadUI(self):
        self.pushButton.clicked.connect(self.draw)
        self.show()

    def draw(self):
        self.flag = True
        self.list_ellipses[-1].append(random.randint(15, 75))
        self.list_ellipses[-1].append(random.randint(0, 500))
        self.list_ellipses[-1].append(random.randint(0, 480))
        self.list_ellipses[-1].append(random.randint(1, 10))
        self.list_ellipses.append([])
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            for circle in self.list_ellipses[:-1]:
                pen = QPen(QColor(random.randint(0, 255),
                                  random.randint(0, 255), random.randint(0, 255)))
                pen.setWidth(circle[-1])
                qp.setPen(pen)
                qp.drawEllipse(*circle[:-1], circle[-2])
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CirclesWidget()
    sys.exit(app.exec_())
