#!/usr/bin/python3
""" list states """

import MySQLdb

def main():
    db = MySQLdb.connect(user=sys.argv[1], host="localhost", port=3306,
                           password=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    results = cur.fetchall()
    for row in results:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
