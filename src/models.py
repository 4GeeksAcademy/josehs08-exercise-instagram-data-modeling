import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name= Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    description = Column(String(50))
    gender = Column(String(1))
#Basados en user:

class Follows(Base):
    __tablename__ = 'follows'
    id = Column(Integer, primary_key=True)
    followed_user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    following_user_id = Column(Integer, ForeignKey('User.id'), nullable=False)

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    recipient_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    sender_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    created_at= Column(String(10), nullable=False)

#Basados en post:

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    caption = Column(String(250))
    image_url = Column(String(250), nullable=False)
    created_at = Column(String(10), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    post_id=Column(Integer, ForeignKey('post.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    created_at = Column(String(10), nullable=False)

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    created_at = Column(String(10), nullable=False)


class Bookmark(Base):
    __tablename__ = "bookmark"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    created_at = Column(String(10), nullable=False)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
