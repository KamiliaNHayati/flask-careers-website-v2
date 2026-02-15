# Carreerly - Job Careers Website

A careers website built with Python Flask, featuring dynamic job listings from a PostgreSQL database.

**Live Demo:** [kamilianhayati.pythonanywhere.com](https://kamilianhayati.pythonanywhere.com/)

## Tech Stack

- Python Flask
- Jinja2 Templates
- Bootstrap 5
- SQLAlchemy + pg8000
- Neon PostgreSQL
- Gunicorn (production server)

## Features

- Dynamic job listings from PostgreSQL database
- Individual job detail pages with responsibilities & requirements
- Application form with database storage
- REST API endpoints (`/api/jobs`, `/api/job/<id>`)
- Reusable template components (navbar, banner, footer, job cards)
- Graceful fallback to static data when DB is unavailable
- Responsive design with Bootstrap

## Run Locally

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add .env file with your database connection
# DATABASE_URI=postgresql+pg8000://user:pass@host/db

# Run
python app.py
```

Visit `http://127.0.0.1:5000`

## API

```
GET /api/jobs        → Returns all jobs in JSON
GET /api/job/<id>    → Returns a specific job in JSON
```

## Credits

Built following [freeCodeCamp Flask Tutorial](https://www.youtube.com/watch?v=yBDHkveJUf4&t=7460s)
