import gi
gi.require_version("Gtk", "3.0")
from gui.gtk.window import GtkWindow


window = GtkWindow()
window.resize(500, 700)
window.set_title("Notatki")
window.show()
