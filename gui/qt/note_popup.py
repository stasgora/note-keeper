import PySide2
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from gui.note_popup import NotePopup
from logic.note_handler import set_note_field


class QtNotePopup(QDialog, NotePopup):
	def __init__(self, note, parent):
		super(QtNotePopup, self).__init__(parent)
		self.note = note
		width = 400
		height = 300
		self.setWindowTitle(self.get_popup_title(note))
		# self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
		self.move((parent.width() - width) / 2, (parent.height() - height) / 2)
		self.resize(width, height)

		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		self.add_title_field()
		self.add_note_field()

		self.add_buttons()

	def add_title_field(self):
		title_field = QLineEdit()
		title_field.setPlaceholderText('Tytuł')
		title_field.setText(self.note['title'])
		title_field.textChanged.connect(lambda title: set_note_field(self.note, 'title', title))
		self.layout.addWidget(title_field)

	def add_note_field(self):
		note_field = QPlainTextEdit()
		note_field.setPlaceholderText('Notatka')
		note_field.setPlainText(self.note['content'])
		note_field.textChanged.connect(lambda: set_note_field(self.note, 'content', note_field.toPlainText()))
		self.layout.addWidget(note_field, 1)

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

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
			return
		super(QtNotePopup, self).keyPressEvent(event)
