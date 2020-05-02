import sys
import gi

gi.require_version("Gtk", "3.0")
from gui.gtk.application import GtkApplication
from PySide2.QtWidgets import QApplication

from gui.qt.window import QtWindow

if __name__ == "__main__":
	if sys.argv[1] == 'Qt':
		window = QtWindow(QApplication(sys.argv))
	elif sys.argv[1] == 'Gtk':
		window = GtkApplication().run(sys.argv)
	else:
		print("Wybierz bibliotekę graficzną poprzez podanie argumentu: 'Qt' lub 'Gtk'")
		exit()

	#window.resize(1200, 800)
	#window.set_title("Notatki")
	#window.show()
