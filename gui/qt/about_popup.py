from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QDialog, QLabel

from common.about import get_about_text


class QtAboutPopup(QDialog):
	def __init__(self, parent):
		super(QtAboutPopup, self).__init__(parent)
		self.resize(400, 400)
		self.setWindowTitle("O programie")

		layout = QVBoxLayout()
		layout.setAlignment(Qt.AlignTop)
		self.setLayout(layout)
		about_label = QLabel(get_about_text().replace('\n', '<br>'))
		about_label.setWordWrap(True)
		layout.addWidget(about_label)
