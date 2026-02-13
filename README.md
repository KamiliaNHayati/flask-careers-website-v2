# Carreerly - Job Careers Website

A careers website built with Python Flask.

**Live Demo:** [kamilianhayati.pythonanywhere.com](https://kamilianhayati.pythonanywhere.com/)

## Tech Stack

- Python Flask
- Jinja2 Templates
- Bootstrap 5
- Gunicorn (production server)

## Features

- Dynamic job listings
- REST API endpoint (`/api/jobs`)
- Reusable template components (navbar, footer, job cards)
- Responsive design with Bootstrap

## Run Locally

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
python app.py
```

Visit `http://127.0.0.1:5000`

## API

```
GET /api/jobs    → Returns all jobs in JSON
```

## Credits

Built following [freeCodeCamp Flask Tutorial](https://www.youtube.com/watch?v=yBDHkveJUf4)
