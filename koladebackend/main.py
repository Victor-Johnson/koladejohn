from fastapi import FastAPI
from database import engine
import models
from routes import blogs, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(blogs.router)
