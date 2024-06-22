#!/usr/bin/python3
"""Script to connect to mysql database"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class State(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    cities = relationship(
       "City",
       cascade="all, delete-orphan",
       backref=backref("state", cascade="all"),
       single_parent=True)
