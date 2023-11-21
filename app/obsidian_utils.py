from app.models.base import BaseNote, ReadNote
from app.models.temp import TempNote
from app.setup import VAULT_PATH
import os

def create_note(note: BaseNote):
    note_path = os.path.join(VAULT_PATH, str(note.title + '.md'))
    with open(note_path, "w+") as note_file:
        moc_link = f"[[{note.moc}]]\n"
        note_file.write(moc_link + note.text)

def append_note(note: BaseNote):
    note_path = os.path.join(VAULT_PATH, str(note.title + '.md'))
    with open(note_path, "a+") as note_file:
        note_file.write(note.text + "\n")

def read_note(note: ReadNote):
    note_path = os.path.join(VAULT_PATH, str(note.title + '.md'))
    with open(note_path, "r") as note_file:
        note_text = note_file.read()
        return TempNote(text=note_text)