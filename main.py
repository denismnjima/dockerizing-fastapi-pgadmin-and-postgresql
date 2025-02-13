from fastapi import FastAPI
from config import engine,Session
from models import User


app = FastAPI()

session = Session(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/users")
async def get_users():
    users = session.query(User).all()
    return users

