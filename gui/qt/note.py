import PySide2
from PySide2.QtGui import QColor, Qt
from PySide2.QtWidgets import QLabel, QGraphicsDropShadowEffect

from gui.qt.note_popup import NotePopup


class Note(QLabel):
	def __init__(self, note):
		super(Note, self).__init__()
		self.setText(self.parse_note_data(note))
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

	def parse_note_data(self, note):
		return '<b>{0}</b><br><br>{1}'.format(note['title'], note['content'])

	def mouseDoubleClickEvent(self, ev: PySide2.QtGui.QMouseEvent):
		super().mouseReleaseEvent(ev)
		NotePopup(self).exec_()