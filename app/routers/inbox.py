from fastapi import APIRouter
from app.models.inbox import InboxNote
from app import obsidian_utils
import logging

router = APIRouter(prefix="/inbox", tags=["inbox"])

@router.post("/")
async def create_inbox_note(note: InboxNote):
    obsidian_utils.create_note(note)
    logging.info(f"NEW INBOX NOTE CREATED: {note.title}")
