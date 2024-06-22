#!/usr/bin/python3
''' Script creates first sqlalchemy state model '''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
