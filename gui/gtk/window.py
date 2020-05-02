from gui.gtk.note import GtkNote
from gui.window import Window

from gi.repository import Gtk, Gdk

from logic.note_handler import load_note


class GtkWindow(Window, Gtk.ApplicationWindow):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.layout = Gtk.VBox()
		self.add(self.layout)

		self.notes = Gtk.Grid()
		self.draw_notes()
		self.apply_styles()

	def draw_notes(self):
		self.layout.pack_end(self.notes, True, True, 0)
		self.notes.attach(GtkNote(load_note(), self), 0, 0, 1, 1)

	def apply_styles(self):
		css = Gtk.CssProvider()
		css.load_from_data(b"""
			.note {
				background-color: white;
				border-radius: 5px;
				color: #222;
				padding: .8em 1em;
				margin: 1em;
				box-shadow: 0 3px 6px rgba(0,0,0,0.4);
			}
			.note-field {
				padding: .8em;
			}
			""")
		Gtk.StyleContext().add_provider_for_screen(Gdk.Screen.get_default(), css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

	def resize(self, width, height):
		Gtk.Window.resize(self, width, height)

	def set_title(self, title):
		Gtk.Window.set_title(self, title)

	def show(self):
		Gtk.Window.connect(self, "destroy", Gtk.main_quit)
		Gtk.Window.show_all(self)
		Gtk.main()
