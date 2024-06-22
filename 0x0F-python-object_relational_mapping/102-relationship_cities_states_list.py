#!/usr/bin/python3
"""Script to fetch city by state"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from relationship_city import City
import sys


def db_engine():
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
        )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for city, state in session.query(City, State)\
                              .join(State, State.id == City.state_id)\
                              .order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))


if __name__ == "__main__":
    db_engine()
