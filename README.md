# Car Service Management System

Web application for managing a car repair workshop: cars, work orders, parts inventory and users.

## Features

- Role-based access (Manager / Mechanic / Client)
- Cars management with optional uploads
- Work orders, assignment and parts usage
- Inventory for parts with basic integrity checks

## Tech stack

- Python 3, Flask, SQLAlchemy, Flask-Login, SQLite

## Quick start

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. (Optional) Set environment variables for production:

```powershell
setx SECRET_KEY "a-strong-secret"
setx FLASK_DEBUG 0
```

3. Run the app:

```powershell
python app.py
```

4. Open http://127.0.0.1:5000 and log in with the default manager account `admin` / `admin123` (created automatically on first run).

## Notes & improvements made

- Config now reads `SECRET_KEY`, `DATABASE_URL` and `FLASK_DEBUG` from environment variables.
- Default manager account is created at startup if missing.
- Removed duplicate `LoginManager` from `blueprints/auth.py` (app-level manager used instead).
- Work order image URLs built using `url_for('static', ...)`.

If you'd like, I can run the app locally, add tests, or harden authentication (CSRF, password rules).
