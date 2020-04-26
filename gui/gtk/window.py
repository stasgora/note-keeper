from gui.gtk.note import Note
from gui.gtk.note_popup import NotePopup
from gui.window import Window

from gi.repository import Gtk


class GtkWindow(Window, Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self)
		self.layout = Gtk.VBox()
		self.add(self.layout)

		self.notes = Gtk.Grid()
		self.draw_notes()

	def draw_notes(self):
		self.layout.pack_end(self.notes, True, True, 0)
		self.notes.attach(Note('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer dictum, neque sed lacinia facilisis, arcu magna '
		                            'porttitor sapien, ac dignissim tortor sapien in dolor. In id neque id lacus interdum vehicula.'), 0, 0, 1, 1)
		button = Gtk.Button(label="Push")
		button.connect('clicked', self.show_note_popup)
		self.notes.attach(button, 0, 1, 1, 1)

	def show_note_popup(self, button):
		popup = NotePopup(self)
		popup.run()
		popup.destroy()

	def resize(self, width, height):
		Gtk.Window.resize(self, width, height)

	def set_title(self, title):
		Gtk.Window.set_title(self, title)

	def show(self):
		Gtk.Window.connect(self, "destroy", Gtk.main_quit)
		Gtk.Window.show_all(self)
		Gtk.main()
