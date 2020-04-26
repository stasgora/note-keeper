from PySide2.QtGui import QColor
from PySide2.QtWidgets import QLabel, QGraphicsDropShadowEffect


class Note(QLabel):
	def __init__(self, text):
		super(Note, self).__init__()
		self.setText(text)
		self.setWordWrap(True)
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
