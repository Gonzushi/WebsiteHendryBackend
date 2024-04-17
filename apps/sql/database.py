from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

SERVER = getenv("SQL_SERVER")
USER = getenv("SQL_USERNAME")
PASSWORD = getenv("SQL_PASSWORD")
DATABASE_NAME = getenv("SQL_DATABASE_NAME")
ODBC_VERSION = getenv("SQL_ODBC_VERSION")

params_url = (
    f"?driver=ODBC+Driver+{ODBC_VERSION}+for+SQL+Server"
    "&Encrypt=yes&TrustServerCertificate=no"
    "&Connection+Timeout=30"
)
connection_url = (
    f"mssql+pyodbc://{USER}:{PASSWORD}@{SERVER}:1433/{DATABASE_NAME}{params_url}"
)

engine = create_engine(connection_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
