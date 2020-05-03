from gui.gtk.note import GtkNote
from gui.gtk.note_popup import GtkNotePopup
from gui.window import Window

from gi.repository import Gtk, Gdk

from logic.note_handler import load_note, create_note


class GtkWindow(Window, Gtk.ApplicationWindow):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.layout = Gtk.VBox()
		self.add(self.layout)
		self.draw_menu_bar()

		self.notes = Gtk.Grid()
		self.draw_notes()
		self.apply_styles()

	def draw_menu_bar(self):
		menu_bar = Gtk.MenuBar()
		menu_item = Gtk.MenuItem('Menu')
		menu = Gtk.Menu()
		menu_item.set_submenu(menu)

		new_note = Gtk.MenuItem('Nowa notatka')
		new_note.connect('button-press-event', lambda w, e: self.new_note_popup())
		menu.append(new_note)

		about = Gtk.MenuItem('O programie')
		about.connect('button-press-event', lambda w, e: self.new_note_popup())
		menu.append(about)

		menu_bar.add(menu_item)
		self.layout.pack_start(menu_bar, False, False, 0)

	def new_note_popup(self):
		popup = GtkNotePopup(create_note(), self, is_new=True)
		if popup.run() == Gtk.ResponseType.APPLY:
			pass
		popup.destroy()

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
