import random
import sys

from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class QPainter:
    pass

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.go)
        self._is_paint = False

    def go(self):
        self._is_paint = True
        self.update()

    def paintEvent(self, a0):
        if self._is_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp: QPainter) -> None:
        color = QColor(255, 255, 0)
        radius - random.randint(10, min(self.width(), self.height()) // 2)
        x = random.randrange(radius, self.width() - radius)
        y = random.randrange(radius, self.height() - radius)
        qp.setBrush(color)
        qp.drawEllipse(x, y, radius, radius)



def exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


if __name__ == '__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighOpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighOpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_EnableHighOpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighOpiPixmaps, True)

    sys.excepthook = sys.excepthook
    sys.excepthook = exception_hook()

    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())
