import json


note_file = 'notes.ndt'


def load_note():
	with open(note_file, 'r') as notes_data:
		note = json.load(notes_data)[0]
		note['id'] = 0
		return note


def save_note(note):
	with open(note_file, 'r') as notes_data:
		notes = json.load(notes_data)
		notes[note['id']] = note
	with open(note_file, 'w') as notes_data:
		json.dump(notes, notes_data, indent='\t')


def set_title(note, title):
	note['title'] = title
