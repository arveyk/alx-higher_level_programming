#!/usr/bin/python3
""" Module to declare the base
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """ Definition of State class
    """
    __tablename__ = 'state'

    id = Column('state_id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)

#    state = relationship("State", back_populates="base")

# Session = sessionmaker(bind=engine)
# session = Session()
