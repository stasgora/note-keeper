import sys
import gi
gi.require_version("Gtk", "3.0")
from PySide2.QtWidgets import QApplication

from gui.qt.window import QtWindow
from gui.gtk.window import GtkWindow

if __name__ == "__main__":
	if sys.argv[1] == 'Qt':
		window = QtWindow(QApplication(sys.argv))
	elif sys.argv[1] == 'GTK':
		window = GtkWindow()
	else:
		print("Wybierz bibliotekę graficzną poprzez podanie argumentu: 'Qt' lub 'GTK'")
		exit()

	window.resize(1200, 800)
	window.set_title("Notatki")
	window.show()
