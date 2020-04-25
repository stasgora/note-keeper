from gui.window import Window

from gi.repository import Gtk


class GtkWindow(Window, Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)

	def resize(self, width, height):
		Gtk.Window.resize(self, width, height)

	def set_title(self, title):
		Gtk.Window.set_title(self, title)

	def show(self):
		Gtk.Window.connect(self, "destroy", Gtk.main_quit)
		Gtk.Window.show_all(self)
		Gtk.main()
