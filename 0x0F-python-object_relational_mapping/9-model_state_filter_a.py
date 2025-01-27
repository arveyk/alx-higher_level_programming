#!/usr/bin/env python3
""" Script using sqlalchemy to demo ORM
"""


from model_state import Base, State
from string import Template
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()
        for id, name in session.query(State.id, State.name).order_by(State.id):
            if 'a' in name:
                print("{}: {}".format(id, name))
