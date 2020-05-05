from common.note_handler import set_note_field


class NotePopup(object):
	def set_note_title(self, title):
		set_note_field(self.note, 'title', title)
		self.set_window_title(self.get_popup_title(self.note))

	def set_window_title(self, title):
		pass  # abstract

	def get_popup_title(self, note):
		title = (' "{0}"'.format(note['title']) if note['title'] else '')
		return ('Nowa notatka' if self.is_new else 'Edycja notatki') + title
