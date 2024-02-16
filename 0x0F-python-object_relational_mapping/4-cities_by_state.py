#!/usr/bin/python3
''' Module to execute mysql command'''
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) == 4:
        argv = sys.argv
        usrname = argv[1]
        password = argv[2]
        db_name = argv[3]

        db = MySQLdb.connect(user=usrname, passwd=password, db=db_name)
        c_ursor = db.cursor()
        # qry = "SELECT id, name FROM cities ORDER BY cities.id ASC"
        qry = "SELECT cities.id, cities.name, states.name\
                FROM  cities INNER JOIN states\
                ON cities.state_id = states.id"
        c_ursor.execute(qry)
        rows = c_ursor.fetchall()

        for eachRow in rows:
            print("{}".format(eachRow))
