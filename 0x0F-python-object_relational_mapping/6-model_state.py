#!/usr/bin/python3
"""
State and clss instance define
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State represemtation for table """
    __tablename__ = 'state'
    id = Colunm(Interger, autoincrement=True, primary_key=True)
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
