#!/usr/bin/python3
"""lists states by user name"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    mycursor = conn.cursor()
    mycursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (sys.argv[4], ))
    results = mycursor.fetchall()
    for row in results:
        print(row)
    mycursor.close()
    db.close()
