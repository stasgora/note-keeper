from gi.repository import Gtk

from gui.note_popup import NotePopup
from logic.note_handler import set_title


class GtkNotePopup(Gtk.Dialog, NotePopup):
	def __init__(self, note, parent):
		Gtk.Dialog.__init__(self, self.get_popup_title(note), parent, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.APPLY))
		self.note = note
		width = 400
		height = 300
		self.set_default_size(width, height)
		self.layout = self.get_content_area()

		self.add_title_field()
		self.show_all()

	def add_title_field(self):
		title_field = Gtk.Entry()
		title_field.set_text(self.note['title'])
		title_field.set_placeholder_text('Tytuł')
		title_field.connect('changed', lambda field: set_title(self.note, field.get_text()))
		self.layout.add(title_field)
