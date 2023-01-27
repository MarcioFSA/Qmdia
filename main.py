from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import QApplication, QMainWindow
import sys
from teste import Ui_Form

class MainWindow(QMainWindow):
   def __init__(self, parent=None):
       QMainWindow.__init__(self)
       self.ui = Ui_Form()
       self.ui.setupUi(self)
       self.show()


if __name__ == "__main__":
   app = QApplication([])
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())


