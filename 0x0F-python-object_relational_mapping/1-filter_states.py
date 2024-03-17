#!/usr/bin/python3
"""
a script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """Here we connect to MySQL database to list al states"""
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
    )
    current = db.cursor()
    current.execute(
        """SELECT * FROM states WHERE name LIKE
        BINARY 'N%' ORDER BY states.id"""
    )
    rows = current.fetchall()
    for row in rows:
        print(row)
    current.close()
    db.close()
