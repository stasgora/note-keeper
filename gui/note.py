from common.note_handler import update_note


class Note(object):
	def update_content(self):
		pass  # abstract

	def update_note(self, note):
		self.note = note
		self.update_content()
		update_note(self.note)
