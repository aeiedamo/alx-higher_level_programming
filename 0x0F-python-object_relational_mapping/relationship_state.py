#!/usr/bin/python3
"""creates a state class objects"""

from enum import unique
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class State(Base):
    """creates a state class"""

    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
