import sys

from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.go)

    def go(self):
        pass

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
