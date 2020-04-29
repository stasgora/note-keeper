from gi.repository import Gtk

from gui.note_popup import NotePopup


class GtkNotePopup(Gtk.Dialog, NotePopup):
	def __init__(self, note, parent):
		Gtk.Dialog.__init__(self, self.get_popup_title(note), parent, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_SAVE, Gtk.ResponseType.APPLY))
		width = 400
		height = 300
		self.set_default_size(width, height)
