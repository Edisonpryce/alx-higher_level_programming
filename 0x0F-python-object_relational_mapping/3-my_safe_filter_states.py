#!/usr/bin/python3
"""Lists states by user name"""

import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
          host="localhost",
          port=3306,
          user=sys.argv[1],
          passwd=sys.argv[2],
          db=sys.argv[3]
          )
    mycursor = db.cursor()
    mycursor.execute(
            """
            SELECT * FROM states WHERE name = %s ORDER BY states.id ASC
            """, (sys.argv[4], ))
    results = mycursor.fetchall()
    for row in results:
        print(row)
    mycursor.close()
    db.close()


if __name__ == '__main__:
    main()
