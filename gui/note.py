from logic.note_handler import save_note


class Note(object):
	def update_content(self):
		pass  # abstract

	def update_note(self, note):
		self.note = note
		self.update_content()
		save_note(self.note)
