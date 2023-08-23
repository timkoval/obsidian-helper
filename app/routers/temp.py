from fastapi import APIRouter
from app.models.temp import TempNote
from app.models.base import ReadNote
from app import obsidian_utils
import logging

router = APIRouter(prefix="/temp", tags=["temp"])

@router.post("/")
async def append_temp_note(note: TempNote):
    obsidian_utils.append_note(note)
    logging.info(f"TEMP NOTE APPENDED: {note.title}")

@router.get("/")
async def read_temp_note():
    note = ReadNote(title="_temp")
    temp_note = obsidian_utils.read_note(note)
    logging.info(f"TEMP NOTE READ: {note.title}")
    return temp_note