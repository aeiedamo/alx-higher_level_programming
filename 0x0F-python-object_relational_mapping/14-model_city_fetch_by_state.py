#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    eng = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    louisiana = State(name="Louisiana")
    for ins in session.query(State.name, City.id, City.name).filter(
        State.id == City.state_id
    ):
        print(ins[0] + ": (" + str(ins[1]) + ") " + ins[2])
