from fastapi import FastAPI
from app.routers import inbox, temp

app = FastAPI()

app.include_router(inbox.router)
app.include_router(temp.router)
