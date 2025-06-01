from sqlalchemy import Column, Integer, String, ForeignKey,Text,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String,nullable=False)
    # Relationships
    projects = relationship('Project', back_populates='owner')
    blogs = relationship('BlogPost', back_populates='author')

class Products(Base):

    __tablename__ = 'products'

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    images = Column(String)
    link_1 = Column(String)
    link_2 = Column(String)

    
class BlogPost(Base):
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, unique=True, nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String)
    cover_images = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    additional_links = Column(String)  # JSON-encoded string if needed

    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='blogs')


# Model to save your projects

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    tech_stack = Column(String)
    github_link = Column(String)
    live_link = Column(String)
    image = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='projects')

# Model to save histories of request sent
class contact_history(Base):

    __tablename__ = 'contact_requests'

    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False)
    email = Column(String, nullable=False)
    message = Column(Text,nullable=False)


class image_meta(Base):

    __tablename__ = 'image-metadata'

    id = Column(Integer,primary_key=True)
    blog_id = Column(Integer,ForeignKey('blogs.id'),nullable=False)
    url = Column(String,nullable=False)
    alt_text = Column(String,nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

