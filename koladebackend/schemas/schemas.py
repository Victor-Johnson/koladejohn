from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

app = FastAPI()

# Project model
class Project(BaseModel):
    id: int
    title: str
    description: str
    tech_stack: str
    github_link: Optional[str]
    live_link: Optional[str]
    image: Optional[str]
    created_at: datetime

# User model
class User(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str

# Product model
class Product(BaseModel):
    id: int
    name: str
    images: str
    link_1: str
    link_2: str

# Contact Request
class ContactRequest(BaseModel):
    name: str
    email: EmailStr
    message: str

# Roles
class UserRole(str, Enum):
    admin = "admin"
    user = "user"

# Project Tags
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

# Blog Tags
class BlogTag(str, Enum):
    ml_theory = "ML Theory"
    data_visualization = "Data Visualization"
    fastapi = "Exploring FastAPI"
    ethics = "AI Ethics"
    open_source = "Open Source in ML"
    model_deployment = "Model Deployment"

# Blog Post Model
class Blogpost(BaseModel):
    title: str
    slug: str
    content: str
    tags: Optional[List[BlogTag]]
    domain: Optional[List[str]]
    category: Optional[str]
    cover_images: Optional[str]
    Additional_link: Optional[List[str]]

class BlogCreate(Blogpost):
    pass

class BlogUpdate(Blogpost):
    pass

class Blogpost(Blogpost):
    id : int 
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 