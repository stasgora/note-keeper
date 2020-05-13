import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from gui.qt.about_popup import QtAboutPopup
from gui.qt.note import QtNote
from gui.qt.note_popup import QtNotePopup
from gui.window import Window
from common.note_handler import *


class QtWindow(Window, QWidget):
	def __init__(self, application):
		QWidget.__init__(self)
		load_notes()
		self.application = application

		self.layout = QVBoxLayout()
		self.layout.setAlignment(Qt.AlignTop)
		self.setLayout(self.layout)

		self.draw_menu_bar()

		self.note_widget = QWidget()
		self.note_layout = QVBoxLayout(self.note_widget)
		self.draw_notes()

	def draw_menu_bar(self):
		menu_bar = QMenuBar()
		self.layout.addWidget(menu_bar)
		menu = QMenu('Menu', self)

		new_note = QAction('Nowa notatka', self)
		new_note.setShortcut('Ctrl+N')
		menu.addAction(new_note)
		new_note.triggered.connect(self.new_note_popup)

		about = QAction('O programie', self)
		menu.addAction(about)
		about.triggered.connect(QtAboutPopup(self).exec_)
		menu_bar.addMenu(menu)

	def new_note_popup(self):
		note = create_note()
		if QtNotePopup(note, self, is_new=True).exec_() == QDialog.Accepted:
			update_note(note)
			self.note_layout.addWidget(QtNote(note, self))
			self.note_layout.update()

	def draw_notes(self):
		note_area = QScrollArea()
		note_area.setWidgetResizable(True)
		self.layout.addWidget(note_area)
		note_area.setWidget(self.note_widget)
		self.note_layout.setParent(self.note_widget)
		self.note_layout.setAlignment(Qt.AlignTop)
		notes = get_notes()
		for i in range(len(notes)):
			self.note_layout.addWidget(QtNote(notes[i], self))

	def resize(self, width, height):
		QWidget.resize(self, width, height)

	def set_title(self, title):
		self.setWindowTitle(title)

	def show(self):
		QWidget.show(self)
		sys.exit(self.application.exec_())
