import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
from Ui_03_CustumSignalSlot import *


class MainWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        def hereisjonny(self):
            print('hereisjonny')
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
