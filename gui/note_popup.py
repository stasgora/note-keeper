class NotePopup(object):
	@staticmethod
	def get_popup_title(note):
		if note is None:
			return 'Nowa notatka'
		else:
			return 'Edycja notatki' + (' "{0}"'.format(note['title']) if note['title'] else '')
