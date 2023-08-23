from app.models.base import BaseNote

class TempNote(BaseNote):
    title: str = "_temp"
    moc: str = "Inbox MOC"