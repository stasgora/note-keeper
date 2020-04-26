from PySide2.QtWidgets import *
from PySide2 import QtCore


class NotePopup(QDialog):
	def __init__(self, parent):
		super(NotePopup, self).__init__(parent)
		width = 400
		height = 300
		self.setWindowTitle('Nowa notatka')
		# self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
		self.move((parent.width() - width) / 2, (parent.height() - height) / 2)
		self.resize(width, height)

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)
