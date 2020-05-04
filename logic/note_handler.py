import json
import os

note_file = 'notes.ndt'
notes_data = []
note_index_counter = 0


def load_notes():
	global notes_data
	global note_index_counter
	if not os.path.isfile(note_file):
		with open(note_file, 'w+') as data:
			json.dump([], data)
	with open(note_file, 'r') as data:
		notes_data = json.load(data)
		for i in range(len(notes_data)):
			notes_data[i]['id'] = i
		note_index_counter = len(notes_data)


def load_note(index=0):
	note = next((note for note in notes_data if note['id'] == index), None)
	if note is None:
		print('Nie znaleziono notatki o indeksie {0}'.format(index))
	return note


def create_note():
	global note_index_counter
	note = {"title": "", "content": "", 'id': note_index_counter}
	notes_data.append(note)
	note_index_counter += 1
	return note


def delete_note(note):
	for i in range(len(notes_data)):
		if notes_data[i]['id'] == note['id']:
			del notes_data[i]
			break
	save_notes()


def update_note(note):
	for i in range(len(notes_data)):
		if notes_data[i]['id'] == note['id']:
			notes_data[i] = note
			break
	save_notes()


def save_notes():
	with open(note_file, 'w') as data:
		json.dump(notes_data, data, indent='\t')


def set_note_field(note, field, value):
	note[field] = value
