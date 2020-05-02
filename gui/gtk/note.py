from gi.repository import Gtk, Gdk

from gui.gtk.note_popup import GtkNotePopup
from gui.note import Note


class GtkNote(Gtk.EventBox, Note):
	def __init__(self, note, window):
		super(GtkNote, self).__init__()
		self.note = note
		self.window = window
		self.label = Gtk.Label()
		self.update_content()
		self.add(self.label)
		# self.note.set_selectable(True)
		self.label.set_line_wrap(True)
		self.connect('button-press-event', self.button_event)
		self.connect('enter-notify-event', lambda w, e: self.set_cursor(Gdk.CursorType.HAND1))
		self.connect('leave-notify-event', lambda w, e: self.set_cursor(Gdk.CursorType.ARROW))

		self.label.get_style_context().add_class('note')

	def set_cursor(self, cursor):
		self.window.get_window().set_cursor(Gdk.Cursor(cursor))

	def update_content(self):
		self.label.set_markup('<b>{0}</b>\n\n{1}'.format(self.note['title'], self.note['content']))

	def button_event(self, widget, event):
		if event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:  # _2BUTTON_PRESS
			edit_note = self.note.copy()
			popup = GtkNotePopup(edit_note, self.window)
			if popup.run() == Gtk.ResponseType.APPLY:
				self.update_note(edit_note)
			popup.destroy()
