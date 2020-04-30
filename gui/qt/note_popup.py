from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from gui.note_popup import NotePopup
from logic.note_handler import set_title


class QtNotePopup(QDialog, NotePopup):
	def __init__(self, note, parent):
		super(QtNotePopup, self).__init__(parent)
		width = 400
		height = 300
		self.setWindowTitle(self.get_popup_title(note))
		# self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
		self.move((parent.width() - width) / 2, (parent.height() - height) / 2)
		self.resize(width, height)

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.title_field = QLineEdit()
		self.title_field.setPlaceholderText('Tytuł')
		self.title_field.setText(note['title'])
		self.title_field.textChanged.connect(lambda title: set_title(note, title))
		self.layout.addWidget(self.title_field)
		self.layout.addStretch(1)

		self.add_buttons()

	def add_buttons(self):
		container = QHBoxLayout()
		container.addStretch(1)
		cancel_button = QPushButton('Cancel')
		cancel_button.clicked.connect(lambda: self.reject())
		container.addWidget(cancel_button, alignment=Qt.AlignRight)
		save_button = QPushButton('Save')
		save_button.clicked.connect(lambda: self.accept())
		container.addWidget(save_button, alignment=Qt.AlignRight)
		self.layout.addLayout(container)
