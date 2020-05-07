from gi.repository import Gtk

from gui.note_popup import NotePopup
from common.note_handler import set_note_field


class GtkNotePopup(Gtk.Dialog, NotePopup):
	def __init__(self, note, parent, is_new):
		self.is_new = is_new
		self.note = note
		Gtk.Dialog.__init__(self, self.get_popup_title(note), parent, 0)
		self.add_action_widget(Gtk.Button("Anuluj"), Gtk.ResponseType.CANCEL)
		if not self.is_new:
			self.add_action_widget(Gtk.Button("Usuń"), Gtk.ResponseType.DELETE_EVENT)
		self.add_action_widget(Gtk.Button("Zapisz"), Gtk.ResponseType.APPLY)
		width = 400
		height = 300
		self.set_default_size(width, height)
		self.layout = self.get_content_area()

		self.add_title_field()
		self.add_note_field()
		self.show_all()

	def add_title_field(self):
		title_field = Gtk.Entry()
		title_field.set_text(self.note['title'])
		title_field.set_placeholder_text('Tytuł')
		title_field.connect('changed', lambda field: self.set_note_title(field.get_text()))
		self.layout.add(title_field)

	def add_note_field(self):
		scroll_view = Gtk.ScrolledWindow()
		scroll_view.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
		note_field = Gtk.TextView()
		note_field.set_wrap_mode(True)
		scroll_view.add(note_field)
		scroll_view.get_style_context().add_class('note-field')
		buffer = note_field.get_buffer()
		buffer.set_text(self.note['content'])
		buffer.connect('changed', lambda field: set_note_field(self.note, 'content', buffer.get_text(buffer.get_start_iter(), buffer.get_end_iter(), True)))
		self.layout.pack_start(scroll_view, True, True, 0)

	def set_window_title(self, title):
		self.set_title(title)
