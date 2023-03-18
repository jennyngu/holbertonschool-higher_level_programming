#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    state_name = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON \
                    cities.state_id = states.id \
                    WHERE states.name=%s", (state_name, ))
    rows = cursor.fetchall()

    if rows == 0:
        print()
    else:
        for row in range(len(rows)):
            if row == len(rows) - 1:
                print(rows[row][0])
            else:
                print(rows[row][0], end=', ')

    cursor.close()
    db.close()
