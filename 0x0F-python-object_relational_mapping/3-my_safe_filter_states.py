#!/usr/bin/python3
''' Module to execute mysql command'''
import MySQLdb
import sys


if __name__ == '__main__':
    if len(sys.argv) == 5:
        argv = sys.argv
        usrname = argv[1]
        password = argv[2]
        db_name = argv[3]
        stt = argv[4]

        db = MySQLdb.connect(user=usrname, passwd=password, db=db_name)
        c_ursor = db.cursor()
        qry = ("SELECT * FROM states WHERE name = stt ORDER BY states.id")
        c_ursor.execute(qry)
        c_ursor.fetchall()
