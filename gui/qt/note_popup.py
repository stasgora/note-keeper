import PySide2
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

from gui.note_popup import NotePopup
from logic.note_handler import set_note_field, delete_note


class QtNotePopup(QDialog, NotePopup):
	def __init__(self, note, parent, is_new):
		self.is_new = is_new
		self.note = note
		super(QtNotePopup, self).__init__(parent)
		width = 400
		height = 300
		self.set_window_title(self.get_popup_title(note))
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
		title_field.textChanged.connect(lambda title: self.set_note_title(title))
		self.layout.addWidget(title_field)

	def add_note_field(self):
		note_field = QPlainTextEdit()
		note_field.setLineWrapMode(QPlainTextEdit.NoWrap)
		note_field.setPlaceholderText('Notatka')
		note_field.setPlainText(self.note['content'])
		note_field.textChanged.connect(lambda: set_note_field(self.note, 'content', note_field.toPlainText()))
		self.layout.addWidget(note_field, 1)

	def add_buttons(self):
		container = QHBoxLayout()
		container.addStretch(1)
		cancel_button = QPushButton('Anuluj')
		cancel_button.clicked.connect(self.reject)
		container.addWidget(cancel_button, alignment=Qt.AlignRight)
		if not self.is_new:
			remove_button = QPushButton('Usuń')
			remove_button.clicked.connect(self.return_delete)
			container.addWidget(remove_button, alignment=Qt.AlignRight)
		save_button = QPushButton('Zapisz')
		save_button.clicked.connect(self.accept)
		container.addWidget(save_button, alignment=Qt.AlignRight)
		self.layout.addLayout(container)

	def return_delete(self):
		delete_note(self.note)
		self.reject()

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
			return
		super(QtNotePopup, self).keyPressEvent(event)

	def set_window_title(self, title):
		self.setWindowTitle(title)
