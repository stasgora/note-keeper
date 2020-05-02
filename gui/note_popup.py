from logic.note_handler import set_note_field


class NotePopup(object):
	def set_note_title(self, title):
		set_note_field(self.note, 'title', title)
		self.set_window_title(self.get_popup_title(self.note))

	def set_window_title(self, title):
		pass  # abstract

	@staticmethod
	def get_popup_title(note):
		if note is None:
			return 'Nowa notatka'
		else:
			return 'Edycja notatki' + (' "{0}"'.format(note['title']) if note['title'] else '')
