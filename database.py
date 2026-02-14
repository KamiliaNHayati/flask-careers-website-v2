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