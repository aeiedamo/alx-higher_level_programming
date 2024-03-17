#!/usr/bin/python3
"""creates a city class objects"""

from enum import unique
from sqlalchemy import Column, ForeignKey, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship

meta_data = MetaData()
Base = declarative_base(metadata=meta_data)


class City(Base):
    """creates a city class"""

    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
