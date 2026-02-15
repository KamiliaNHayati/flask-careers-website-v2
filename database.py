from sqlalchemy import create_engine, text
import os
import ssl
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

def get_engine():
    try:
        db_url = os.getenv("DATABASE_URI", "").split("?")[0]
        if not db_url:
            return None
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        engine = create_engine(db_url, connect_args={"ssl_context": ssl_context})
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return engine
    except Exception:
        return None

engine = get_engine()

JOBS = [
    {'id': 1, 'title': 'Data Analyst', 'location': 'Remote', 'salary': '$80,000'},
    {'id': 2, 'title': 'Data Scientist', 'location': 'Remote', 'salary': '$90,000'},
    {'id': 3, 'title': 'Data Engineer', 'location': 'Remote', 'salary': '$100,000'}
]

def load_jobs_from_db():
    if engine is None:
        return JOBS
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        return [dict(row._mapping) for row in result.all()]


def load_job_from_db(id):
    if engine:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
            row = result.fetchone()
            if row is None:
                return None
            return dict(row._mapping)
    # Fallback to static JOBS list
    for job in JOBS:
        if str(job['id']) == str(id):
            return job
    return None

def add_application_to_db(job_id, application):
    if engine is None:
        return

    query = """
    INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) 
    VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)
    """

    with engine.connect() as conn:
        conn.execute(text(query), 
            {"job_id": job_id, 
            "full_name": application["full_name"], 
            "email": application["email"], 
            "linkedin_url": application["linkedin_url"], 
            "education": application["education"], 
            "work_experience": application["work_experience"], 
            "resume_url": application["resume_url"]})
        conn.commit()
