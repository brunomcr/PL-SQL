import os
import cx_Oracle
from dotenv import load_dotenv


# Take environment variables from .env.
load_dotenv()

# DSN
dsn = cx_Oracle.makedsn(
    host=os.getenv("host"), port=os.getenv("port"), sid=os.getenv("sid")
)

# CONNECTION
connection = cx_Oracle.connect(
    user=os.getenv("user"), password=os.getenv("password"), dsn=dsn
)

print("Conectado a Oracle Database com Sucesso!")
