import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QLabel, QGraphicsDropShadowEffect, QDialog

from gui.note import Note
from gui.qt.note_popup import QtNotePopup


class QtNote(QLabel, Note):
	def __init__(self, note, window):
		super(QtNote, self).__init__()
		self.note = note
		self.window = window
		self.update_content()
		self.setWordWrap(True)
		self.setCursor(Qt.PointingHandCursor)
		self.setTextInteractionFlags(Qt.TextSelectableByMouse)
		self.setStyleSheet(
			"QLabel {"
				"background-color: white;"
				"border-radius: 5px;"
				"color: #222;"
				"padding: .8em 1em;"
				"margin: 1em;"
			"}")
		shadow = QGraphicsDropShadowEffect(self)
		shadow.setColor(QColor(0, 0, 0, 50))
		shadow.setBlurRadius(8)
		shadow.setOffset(3, 6)
		self.setGraphicsEffect(shadow)

	def update_content(self):
		return self.setText('<b>{0}</b>\n\n{1}'.format(self.note['title'], self.note['content']).replace('\n', '<br>'))

	def mouseDoubleClickEvent(self, ev: PyQt5.QtGui.QMouseEvent):
		super().mouseReleaseEvent(ev)
		edit_note = self.note.copy()
		popup = QtNotePopup(edit_note, self, is_new=False)
		if popup.exec_() == QDialog.Accepted:
			self.update_note(edit_note)
		elif popup.note_removed:
			self.setParent(None)
