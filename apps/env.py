from dotenv import load_dotenv
from os import getenv

load_dotenv()

SERVER = getenv("SQL_SERVER")
USER = getenv("SQL_USERNAME")
PASSWORD = getenv("SQL_PASSWORD")
DATABASE_NAME = getenv("SQL_DATABASE_NAME")
ODBC_VERSION = getenv("SQL_ODBC_VERSION")
API_KEY = getenv("IP_2_LOCATION_API_KEY")