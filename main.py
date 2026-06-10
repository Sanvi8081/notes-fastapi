# Import FastAPI framework
from fastapi import FastAPI, HTTPException

# Import BaseModel for validation
from pydantic import BaseModel


# Create FastAPI app
app = FastAPI(
    title="Basic CRUD API",
    description="Simple Notes CRUD using FastAPI",
    version="1.0.0"
)


# Define Note structure
class Note(BaseModel):
    title: str
    content: str


# Temporary database (list)
notes = []


# ---------------- CREATE NOTE ----------------
@app.post("/create-note", tags=["Notes"])
def create_note(note: Note):

    notes.append(note)

    return {
        "message": "Note created successfully",
        "note": note
    }


# ---------------- GET ALL NOTES ----------------
@app.get("/get-notes", tags=["Notes"])
def get_notes():

    return {
        "total_notes": len(notes),
        "notes": notes
    }


# ---------------- GET SINGLE NOTE ----------------
@app.get("/get-note/{note_id}", tags=["Notes"])
def get_single_note(note_id: int):

    # Check if note exists
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return {
        "note_id": note_id,
        "note": notes[note_id]
    }


# ---------------- UPDATE NOTE ----------------
@app.put("/update-note/{note_id}", tags=["Notes"])
def update_note(note_id: int, updated_note: Note):

    # Check if note exists
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    # Update note
    notes[note_id] = updated_note

    return {
        "message": "Note updated successfully",
        "updated_note": updated_note
    }


# ---------------- DELETE NOTE ----------------
@app.delete("/delete-note/{note_id}", tags=["Notes"])
def delete_note(note_id: int):

    # Check if note exists
    if note_id < 0 or note_id >= len(notes):
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    deleted_note = notes.pop(note_id)

    return {
        "message": "Note deleted successfully",
        "deleted_note": deleted_note
    }