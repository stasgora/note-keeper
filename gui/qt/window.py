import sys

from PySide2.QtWidgets import *

from gui.qt.note import Note
from gui.window import Window
from logic.note_loader import load_note


class QtWindow(Window, QWidget):
	def __init__(self, application):
		QWidget.__init__(self)
		self.application = application

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.menu_bar = QMenuBar()
		self.notes = QGridLayout()

		self.draw_menu_bar()
		self.draw_notes()

	def draw_menu_bar(self):
		self.layout.addWidget(self.menu_bar)
		self.menu_bar.addMenu(QMenu("Plik"))

	def draw_notes(self):
		self.layout.addLayout(self.notes)
		self.layout.addStretch(1)
		self.notes.setMargin(5)
		#self.notes.setColumnMinimumWidth(20)
		#self.notes.setRowMinimumHeight(20)

		self.notes.addWidget(Note(load_note()), 0, 0)

	def resize(self, width, height):
		QWidget.resize(self, width, height)

	def set_title(self, title):
		self.setWindowTitle(title)

	def show(self):
		QWidget.show(self)
		sys.exit(self.application.exec_())
