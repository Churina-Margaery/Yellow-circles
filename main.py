import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from random import choice
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.flag_change)

    def flag_change(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.flag = False

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for _ in range(4):
            x = choice(range(0, 575))
            y = choice(range(0, 451))
            rad = choice(range(1, 200))
            qp.drawEllipse(x, y, rad, rad)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

