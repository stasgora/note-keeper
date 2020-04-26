import sys

from PySide2.QtWidgets import *

from gui.qt.note import Note
from gui.qt.note_popup import NotePopup
from gui.window import Window


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
		self.layout.addLayout(self.notes, 1)
		self.layout.addStretch(1)
		self.notes.setMargin(5)
		#self.notes.setColumnMinimumWidth(20)
		#self.notes.setRowMinimumHeight(20)

		self.notes.addWidget(Note('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer dictum, neque sed lacinia facilisis, arcu magna '
		                          'porttitor sapien, ac dignissim tortor sapien in dolor. In id neque id lacus interdum vehicula.'), 0, 0)
		item_button = QPushButton("Open")
		self.notes.addWidget(item_button, 1, 0)
		item_button.clicked.connect(lambda: NotePopup(self).exec_())

	def resize(self, width, height):
		QWidget.resize(self, width, height)

	def set_title(self, title):
		self.setWindowTitle(title)

	def show(self):
		QWidget.show(self)
		sys.exit(self.application.exec_())
