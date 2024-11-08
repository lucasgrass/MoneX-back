import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_DB_HOST = os.getenv("SUPABASE_DB_HOST")
SUPABASE_DB_NAME = os.getenv("SUPABASE_DB_NAME")
SUPABASE_DB_USER = os.getenv("SUPABASE_DB_USER")
SUPABASE_DB_PASSWORD = os.getenv("SUPABASE_DB_PASSWORD")
SUPABASE_DB_PORT = os.getenv("SUPABASE_DB_PORT")

try:
  connection = psycopg2.connect(
    host=SUPABASE_DB_HOST,
    database=SUPABASE_DB_NAME,
    user=SUPABASE_DB_USER,
    password=SUPABASE_DB_PASSWORD,
    port=SUPABASE_DB_PORT
  )
  cursor = connection.cursor()
  cursor.execute("SELECT version();")
  db_version = cursor.fetchone()
  print(f"200")
  cursor.close()
  connection.close()

except Exception as e:
  print(f"Error: {e}")
