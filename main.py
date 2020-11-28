import random
import sys

from PyQt5.QtGui import QPen, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from giTT1.ui_file import Ui_MainWindow


class CirclesWidget(Ui_MainWindow, QMainWindow):
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
        self.color = QColor(random.randint(0, 255) for _ in range(3))
        self.repaint()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            for circle in self.list_ellipses[:-1]:
                pen = QPen(self.color)
                pen.setWidth(circle[-1])
                qp.setPen(pen)
                qp.drawEllipse(*circle[:-1], circle[-2])
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CirclesWidget()
    sys.exit(app.exec_())
