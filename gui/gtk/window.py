from gui.gtk.note import GtkNote
from gui.window import Window

from gi.repository import Gtk

from logic.note_handler import load_note


class GtkWindow(Window, Gtk.ApplicationWindow):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.layout = Gtk.VBox()
		self.add(self.layout)

		self.notes = Gtk.Grid()
		self.draw_notes()

	def draw_notes(self):
		self.layout.pack_end(self.notes, True, True, 0)
		self.notes.attach(GtkNote(load_note(), self), 0, 0, 1, 1)

	def resize(self, width, height):
		Gtk.Window.resize(self, width, height)

	def set_title(self, title):
		Gtk.Window.set_title(self, title)

	def show(self):
		Gtk.Window.connect(self, "destroy", Gtk.main_quit)
		Gtk.Window.show_all(self)
		Gtk.main()
