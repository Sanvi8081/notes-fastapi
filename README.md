# 📝 Notes CRUD API using FastAPI.

A simple **CRUD (Create, Read, Update, Delete) API** built using **FastAPI**. This project demonstrates basic API development concepts such as routes, request validation, path parameters, exception handling, and Swagger API testing.

## 🚀 Features

* Create a note
* Get all notes
* Get a single note by ID
* Update an existing note
* Delete a note
* Built-in Swagger UI for API testing

---

## 🛠 Tech Stack

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**

---

## 📂 Project Structure

```text
project-folder/
│── main.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-github-repo-link>
```

### 2. Move into project folder

```bash
cd your-project-folder
```

### 3. Create virtual environment (Optional but Recommended)

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn
```

Or using requirements file:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the FastAPI server using:

```bash
uvicorn main:app --reload
```

If port `8000` is already in use:

```bash
uvicorn main:app --reload --port 8001
```

---

## 📌 API Endpoints

| Method | Endpoint                 | Description       |
| ------ | ------------------------ | ----------------- |
| POST   | `/create-note`           | Create a new note |
| GET    | `/get-notes`             | Get all notes     |
| GET    | `/get-note/{note_id}`    | Get note by ID    |
| PUT    | `/update-note/{note_id}` | Update a note     |
| DELETE | `/delete-note/{note_id}` | Delete a note     |

---

## 📖 API Documentation (Swagger UI)

FastAPI provides automatic interactive API documentation.

Open in browser:

```text
http://127.0.0.1:8000/docs
```

Or if using port `8001`:

```text
http://127.0.0.1:8001/docs
```

---

## 📥 Example Request Body

### Create / Update Note

```json
{
    "title": "Learning FastAPI",
    "content": "Building CRUD APIs"
}
```

---

## 🔍 Example Response

```json
{
    "message": "Note created successfully",
    "note": {
        "title": "Learning FastAPI",
        "content": "Building CRUD APIs"
    }
}
```

---

## 🎯 Learning Outcomes

This project helped in understanding:

* FastAPI basics
* CRUD operations
* API endpoints
* Request validation using Pydantic
* Path parameters
* Exception handling
* Swagger documentation

---



