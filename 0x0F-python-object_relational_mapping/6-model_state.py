#!/usr/bin/python3
"""Script connects to mysql db """


from sqlalchemy import create_engine
import sys


def db_engine():
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@localhost:3306/{db}'
            )
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    db_engine()
