from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="Notes API with Frontend")

# Mount static folder (IMPORTANT)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates setup
templates = Jinja2Templates(directory="templates")

class Note(BaseModel):
    title: str
    content: str

notes = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "notes": notes})

@app.get("/notes")
def get_notes():
    return {"notes": notes}

@app.post("/notes")
def add_note(note: Note):
    notes.append(note)
    return {"message": "Note added successfully"}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    if note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    notes.pop(note_id)
    return {"message": "Note deleted"}


