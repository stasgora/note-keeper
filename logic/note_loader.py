import json


def load_note():
	with open('notes.ndt', 'r') as note:
		return json.load(note)