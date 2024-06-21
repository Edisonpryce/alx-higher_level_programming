#!/usr/bin/python3
"""Lists states by user name"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (argv[4], ))
    query_rows = mycursor.fetchall()
    for row in query_rows:
        print(row)
    mycursor.close()
    db.close()
