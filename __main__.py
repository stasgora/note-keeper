import sys
import gi
gi.require_version("Gtk", "3.0")
from PyQt5.QtWidgets import QApplication

from gui.qt.window import QtWindow
from gui.gtk.window import GtkWindow

if __name__ == "__main__":
	if sys.argv[1] == 'Qt':
		window = QtWindow(QApplication(sys.argv))
	elif sys.argv[1] == 'Gtk':
		window = GtkWindow()
	else:
		print("Wybierz bibliotekę graficzną poprzez podanie argumentu: 'Qt' lub 'Gtk'")
		exit()

	window.resize(500, 700)
	window.set_title("Notatki")
	window.show()
