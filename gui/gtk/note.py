from gi.repository import Gtk, Gdk

from gui.gtk.note_popup import GtkNotePopup


class Note(Gtk.EventBox):
	def __init__(self, note, window):
		super(Note, self).__init__()
		self.note = note
		self.window = window
		self.label = Gtk.Label()
		self.label.set_markup(self.parse_note_data(note))
		self.add(self.label)
		# self.note.set_selectable(True)
		self.label.set_line_wrap(True)
		self.connect('button-press-event', self.button_event)
		self.connect('enter-notify-event', lambda w, e: self.set_cursor(Gdk.CursorType.HAND1))
		self.connect('leave-notify-event', lambda w, e: self.set_cursor(Gdk.CursorType.ARROW))

		self.label.get_style_context().add_class('note')
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
			""")
		Gtk.StyleContext().add_provider_for_screen(Gdk.Screen.get_default(), css, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

	def set_cursor(self, cursor):
		self.window.get_window().set_cursor(Gdk.Cursor(cursor))

	def parse_note_data(self, note):
		return '<b>{0}</b>\n\n{1}'.format(note['title'], note['content'])

	def button_event(self, widget, event):
		if event.type == Gdk.EventType.DOUBLE_BUTTON_PRESS:  # _2BUTTON_PRESS
			popup = GtkNotePopup(self.note, self.window)
			popup.run()
			popup.destroy()
