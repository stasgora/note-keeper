import sys

from PySide2.QtWidgets import *

from gui.qt.note import QtNote
from gui.qt.note_popup import QtNotePopup
from gui.window import Window
from logic.note_handler import load_note, create_note


class QtWindow(Window, QWidget):
	def __init__(self, application):
		QWidget.__init__(self)
		self.application = application

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.notes = QGridLayout()

		self.draw_menu_bar()
		self.draw_notes()

	def draw_menu_bar(self):
		menu_bar = QMenuBar()
		self.layout.addWidget(menu_bar)
		menu = QMenu('Menu', self)

		new_note = QAction('Nowa notatka', self)
		new_note.setShortcut('Ctrl+N')
		menu.addAction(new_note)
		menu.triggered.connect(self.new_note_popup)

		about = QAction('O programie', self)
		menu.addAction(about)

		quit = QAction('Zakończ', self)
		quit.setShortcut('Ctrl+Q')
		quit.triggered.connect(self.close)
		menu.addAction(quit)
		menu_bar.addMenu(menu)

	def new_note_popup(self):
		if QtNotePopup(create_note(), self, is_new=True).exec_() == QDialog.Accepted:
			pass

	def draw_notes(self):
		self.layout.addLayout(self.notes)
		self.layout.addStretch(1)
		self.notes.setMargin(5)
		#self.notes.setColumnMinimumWidth(20)
		#self.notes.setRowMinimumHeight(20)

		self.notes.addWidget(QtNote(load_note()), 0, 0)

	def resize(self, width, height):
		QWidget.resize(self, width, height)

	def set_title(self, title):
		self.setWindowTitle(title)

	def show(self):
		QWidget.show(self)
		sys.exit(self.application.exec_())
