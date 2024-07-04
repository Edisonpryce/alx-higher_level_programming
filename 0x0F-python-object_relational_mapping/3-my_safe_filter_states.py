#!/usr/bin/python3
""" Script to protect against sql injection"""

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
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    mycursor.execute(query, (sys.argv[4],))
    results = mycursor.fetchall()
    for row in results:
        print(row)
    mycursor.close()
    db.close()


if __name__ == "__main__":
    main()
