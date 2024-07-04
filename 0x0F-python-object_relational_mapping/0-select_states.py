#!/usr/bin/python3
""" list states """

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
          user=sys.argv[1],
          host="localhost",
          port=3306,
          password=sys.argv[2],
          db=sys.argv[3]
    )
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states")
    results = mycursor.fetchall()
    for row in results:
        print(row)
    mycursor.close()
    db.close()


if __name__ == "__main__":
    main()
