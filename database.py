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
    return None