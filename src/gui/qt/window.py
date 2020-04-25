from PySide2.QtWidgets import *


class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.menu_bar = QMenuBar()
		self.layout.addWidget(self.menu_bar)
		self.menu_bar.addMenu(QMenu("File"))
