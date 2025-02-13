from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')

Base = declarative_base()

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker()



# Create an engine (replace with your own database URI)
