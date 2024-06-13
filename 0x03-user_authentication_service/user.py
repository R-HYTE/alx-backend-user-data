#!/usr/bin/env python3
""" This module defines the User model for the users table using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """
    User model for the 'users' table.

    Attributes:
        id (int): The primary key for the user.
        email (str): The email of the user, cannot be null.
        hashed_password (str): The hashed password of the user, cannot be null.
        session_id (str): The session ID, can be null.
        reset_token (str): The reset token, can be null.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
