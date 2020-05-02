import PySide2
from PySide2.QtGui import QColor, Qt
from PySide2.QtWidgets import QLabel, QGraphicsDropShadowEffect, QDialog

from gui.note import Note
from gui.qt.note_popup import QtNotePopup


class QtNote(QLabel, Note):
	def __init__(self, note):
		super(QtNote, self).__init__()
		self.note = note
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

	def mouseDoubleClickEvent(self, ev: PySide2.QtGui.QMouseEvent):
		super().mouseReleaseEvent(ev)
		edit_note = self.note.copy()
		if QtNotePopup(edit_note, self).exec_() == QDialog.Accepted:
			self.update_note(edit_note)
