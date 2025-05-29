from fastapi import FastAPI
from pydantic import BaseModel ,Emailstr,datetime ,Optional

app = FastAPI()

class projects(BaseModel):
    id : int 
    title : str 
    description : str 
    tech_stack : str 
    github_link : Optional[str]
    live_link : Optional[str]
    image : Optional[str]
    created_at : datetime

class User(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str

class ContactRequest(BaseModel):
    name : str 
    email : Emailstr
    message : str 

class Blogpost(BaseModel):
    id : int 
    title : str 
    slug : str 
    content : str 
    category : Optional[str]
    cover_images : Optional[str]
    created_at : datetime 
    updated_at : datetime 
    Additional_link : Optional[list[str]]




