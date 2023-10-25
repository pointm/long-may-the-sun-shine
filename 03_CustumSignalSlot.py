import sys
import typing
from PyQt5 import QtCore
# 导入PyQt5基本的控件
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# 导入qt designer生成的小文件
from Ui_03_CustumSignalSlot import Ui_Dialog


class PrintText(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(PrintText, self).__init__(parent)  # 不加这句话没办法在实例化的时候初始化代码
        self.setupUi(self)  # 没有这句话不显示UI哈
    # 需要自定义的插槽函数就在这里自定义一下就行

    def hereisjonny(self):
        print('hereisjonny')

    def whathefuckisthis(self):
        print('whathefuckisthis')


if __name__ == '__main__':
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = PrintText()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
