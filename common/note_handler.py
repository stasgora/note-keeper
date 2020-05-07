import json
import os

note_file = 'notes.ndt'
notes_data = {}
note_index_counter = 0


def load_notes():
	global notes_data
	global note_index_counter
	if not os.path.isfile(note_file):
		with open(note_file, 'w+') as data:
			json.dump({}, data)
	with open(note_file, 'r') as data:
		data = json.load(data)
		for note in data.values():
			notes_data[str(note_index_counter)] = note
			notes_data[str(note_index_counter)]['id'] = str(note_index_counter)
			note_index_counter += 1


def load_note(index=0):
	if str(index) not in notes_data:
		print('Nie znaleziono notatki o indeksie {0}'.format(index))
	return notes_data[str(index)]


def get_notes():
	return list(notes_data.values())


def create_note():
	global note_index_counter
	note = {"title": "", "content": "", 'id': str(note_index_counter)}
	notes_data[str(note_index_counter)] = note
	note_index_counter += 1
	return note


def delete_note(note):
	del notes_data[note['id']]
	save_notes()


def update_note(note):
	notes_data[note['id']] = note
	save_notes()


def save_notes():
	with open(note_file, 'w') as data:
		json.dump(notes_data, data, indent='\t')


def set_note_field(note, field, value):
	note[field] = value
