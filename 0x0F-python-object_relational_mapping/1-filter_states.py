#!/usr/bin/python3
''' Module to execute mysql command'''
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) == 4:
        argv = sys.argv
        usrname = argv[1]
        pwrd = argv[2]
        db_name = argv[3]

        db = MySQLdb.connect(user=usrname, passwd=pwrd, db=db_name)
        c_ursor = db.cursor()
        qry = ("SELECT * FROM states\
               WHERE name LIKE BINARY 'N%' ORDER BY states.id")
        c_ursor.execute(qry)

        rows = c_ursor.fetchall()

        for echR in rows:
            print(echR)
