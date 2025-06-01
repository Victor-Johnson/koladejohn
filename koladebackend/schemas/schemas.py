from fastapi import FastAPI
from pydantic import BaseModel ,Emailstr,datetime ,Optional
from enum import Enum 

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

class product(BaseModel):
    id : int 
    name : str 
    images : str 
    link_1 : str
    link_2 : str 

class ContactRequest(BaseModel):
    name : str 
    email : Emailstr
    message : str 

class UserRole(BaseModel,Enum):
    admin = "admin"
    user = "user"


class ProjectTag(str, Enum):
    python = "Python"
    pandas = "Pandas"
    scikit_learn = "scikit-learn"
    tensorflow = "TensorFlow"
    nlp = "NLP"
    forecasting = "Time Series Forecasting"
    docker = "Docker"
    mlops = "MLOps"
    dataeng = "Data Engineering"
    cloud = "Cloud"
    aws = "AWS"
    fastapi = "Fastapi"
    Com_vision = "Computer Vision"
    maclearn = "Machine Learning"
    life = "Life & Fun"

class BlogTag(str, Enum):
    ml_theory = "ML Theory"
    data_visualization = "Data Visualization"
    fastapi = "Exploring FastAPI"
    ethics = "AI Ethics"
    open_source = "Open Source in ML"
    model_deployment = "Model Deployment"



class applicationdomain(BaseModel,Enum):
    pass

class Blogpost(BaseModel):
    id : int 
    title : str 
    slug : str 
    content : str 
    tags : Optional[list[BlogTag]]
    domain : Optional[list[str]]
    category : Optional[str]
    cover_images : Optional[str]
    created_at : datetime 
    updated_at : datetime 
    Additional_link : Optional[list[str]]




