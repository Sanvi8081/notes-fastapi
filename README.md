
# 📝 Notes App – FastAPI Full Stack Project

A beginner-friendly full-stack Notes Web Application built using **FastAPI (Python)** for the backend and **HTML, CSS, JavaScript** for the frontend.
This application allows users to add, view, and delete notes through a simple web interface and REST API.

---

## 🚀 Features

* ➕ Add new notes
* 📄 View all notes dynamically
* ❌ Delete notes
* 🌐 Interactive frontend UI (HTML + CSS)
* ⚡ FastAPI backend with REST APIs
* 📚 Automatic API documentation (Swagger UI)
* 🔄 Real-time updates using JavaScript Fetch API

---

## 🛠️ Tech Stack

### 🔹 Backend

* Python
* FastAPI
* Uvicorn (ASGI Server)
* Pydantic (Data Validation)
* Jinja2 (Template Rendering)

### 🔹 Frontend

* HTML5
* CSS3
* JavaScript (Fetch API)

### 🔹 Tools

* VS Code
* Git & GitHub

---

## 📁 Project Structure

```
notes-api/
│── main.py              # FastAPI backend
│── templates/
│   └── index.html       # Frontend UI
│── static/
│   └── style.css        # CSS styling
│── README.md
```

---

## ⚙️ How the Application Works

1. User opens the web app in the browser
2. Frontend sends API requests using JavaScript (Fetch)
3. FastAPI processes requests (CRUD operations)
4. Notes are stored in memory (Python list)
5. Data is returned as JSON and displayed on the UI

---

## 🔗 API Endpoints

| Method | Endpoint           | Description                 |
| ------ | ------------------ | --------------------------- |
| GET    | `/`                | Load the frontend interface |
| GET    | `/notes`           | Retrieve all notes          |
| POST   | `/notes`           | Add a new note              |
| DELETE | `/notes/{note_id}` | Delete a note by ID         |

---

## ▶️ Installation & Setup (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/notes-api.git
cd notes-api
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn jinja2
```

### 3️⃣ Run the Server

```bash
uvicorn main:app --reload
```

### 4️⃣ Open in Browser

Frontend UI:

```
http://127.0.0.1:8000/
```

API Documentation (Swagger):

```
http://127.0.0.1:8000/docs
```

---

## 🧠 Key Concepts Demonstrated

* FastAPI framework fundamentals
* REST API development (GET, POST, DELETE)
* Pydantic data modeling & validation
* Frontend and backend integration
* Template rendering using Jinja2
* Static file serving (CSS) in FastAPI
* JSON request and response handling
* Basic full-stack project architecture

---

## 📌 Portfolio Description

Developed a full-stack Notes Web Application using FastAPI, HTML, CSS, and JavaScript with RESTful APIs, CRUD functionality, template rendering, and frontend-backend integration as a beginner full-stack project.
