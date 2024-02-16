#!/usr/bin/python3
''' Module to execute mysql command'''
import MySQLdb
import sys


if __name__ == '__main__':
    argv = sys.argv
    usrname = argv[1]
    password = argv[2]
    db_name = argv[3]
    stt = argv[4]

    db = MySQLdb.connect(user=usrname, passwd=password, db=db_name)
    c_ursor = db.cursor()
    qry = ("SELECT * FROM states WHERE name = %s \
            ORDER BY states.id")
    c_ursor.execute(qry, (stt,))
    rows = c_ursor.fetchall()
    
    for eachRow in rows:
        print('{}'.format(eachRow))
