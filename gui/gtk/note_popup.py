from gi.repository import Gtk


class NotePopup(Gtk.Dialog):
	def __init__(self, parent):
		Gtk.Dialog.__init__(self, "Nowa notatka", parent, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))
		width = 400
		height = 300
		self.set_default_size(width, height)
