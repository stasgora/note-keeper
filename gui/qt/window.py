import sys

from PySide2.QtWidgets import *

from gui.window import Window


class QtWindow(Window, QWidget):
	def __init__(self, application):
		QWidget.__init__(self)
		self.application = application

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.menu_bar = QMenuBar()
		self.layout.addWidget(self.menu_bar)
		self.menu_bar.addMenu(QMenu("File"))

	def resize(self, width, height):
		QWidget.resize(self, width, height)

	def set_title(self, title):
		QWidget.setWindowTitle(self, title)

	def show(self):
		QWidget.show(self)
		sys.exit(self.application.exec_())
