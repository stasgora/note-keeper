import sys
from PySide2.QtWidgets import QApplication

from src.gui.qt.window import Window


if __name__ == "__main__":
	if sys.argv[1] == 'Qt':
		app = QApplication(sys.argv)

		widget = Window()
		widget.resize(1200, 800)
		widget.show()

		sys.exit(app.exec_())
	elif sys.argv[1] == 'GTK':
		pass
	else:
		print("Wybierz bibliotekę graficzną poprzez podanie argumentu: 'Qt' lub 'GTK'")
