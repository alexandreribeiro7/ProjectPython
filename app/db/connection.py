from decouple import config 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = config('DB_URL')

engine = create_engine(DB_URL, poll_pre_ping=True)
Session = sessionmaker()