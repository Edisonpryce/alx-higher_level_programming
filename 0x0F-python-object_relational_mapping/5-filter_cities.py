#!/usr/bin/python3
""" Script listing cities by states"""

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
          user=sys.argv[1],
          host="localhost",
          port=3306,
          password=sys.argv[2],
          database=sys.argv[3]
    )
    mycursor = db.cursor()
    query = """
    SELECT c.id, c.name
    FROM cities c
    JOIN states s ON c.state_id = s.id
    WHERE s.name = %s
    ORDER BY c.id ASC
    """
    mycursor.execute(query, (sys.argv[4],))
    results = mycursor.fetchall()
    print(", ".join([row[1] for row in results]))
    mycursor.close()
    db.close()


if __name__ == "__main__":
    main()
