from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Notes API", description="A simple Notes API for learning FastAPI")

class Note(BaseModel):
    title: str
    content: str

notes = []

@app.get("/")
def home():
    return {"message": "Notes API is running successfully!"}

@app.get("/notes", tags=["Notes"])
def get_notes():
    return {"notes": notes}

@app.post("/notes", tags=["Notes"])
def add_note(note: Note):
    notes.append(note.dict())
    return {"message": "Note added successfully", "notes": notes}

@app.delete("/notes/{note_id}", tags=["Notes"])
def delete_note(note_id: int):
    if note_id >= len(notes):
        raise HTTPException(status_code=404, detail="Note not found")
    
    deleted_note = notes.pop(note_id)
    return {"message": "Note deleted", "deleted": deleted_note}


