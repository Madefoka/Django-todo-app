# Django To-Do App ✅

A simple, clean to-do list built with Django — add tasks, mark them done, and remove them. A compact reference project covering Django CRUD fundamentals end-to-end, from models to a deployable configuration.

## Features

- ➕ **Add, complete and delete tasks** (full CRUD)
- 🗂️ Server-rendered templates with a straightforward, no-frills UI
- ⚙️ **Environment-based config** (`django-environ`) — no secrets in code
- 🚀 **Deploy-ready** — `Procfile` + `runtime.txt` for Render / Railway / Heroku-style hosting

## Tech stack

| Layer | Tech |
|-------|------|
| Backend | Django 5.0 (Python) |
| Database | PostgreSQL (SQLite for local dev) |
| Server | Gunicorn |
| Config | `django-environ` |

## Running locally

```bash
git clone https://github.com/Madefoka/Django-todo-app.git
cd Django-todo-app
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000.

Create a `.env` file for local configuration (secret key, database URL) — these are read via `django-environ`.
