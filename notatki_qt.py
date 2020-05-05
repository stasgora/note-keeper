import sys
from PySide2.QtWidgets import QApplication
from gui.qt.window import QtWindow


window = QtWindow(QApplication(sys.argv))
window.resize(500, 700)
window.set_title("Notatki")
window.show()
