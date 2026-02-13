from sqlalchemy import create_engine, text
import os
import ssl
from dotenv import load_dotenv

load_dotenv()

# Remove sslmode from URL (pg8000 doesn't support it)
db_url = os.getenv("DATABASE_URI").split("?")[0]

# Skip SSL verification (MSYS2 Python missing CA certs)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

engine = create_engine(
    db_url,
    connect_args={"ssl_context": ssl_context}
)
