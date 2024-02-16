#!/usr/bin/python3
''' Module to execute mysql command'''
import MySQLdb
import sys


if __name__ == '__main__':
    """ this conditions ensures script is not executed when imported
    """
    if len(sys.argv) == 5:
        argv = sys.argv
        usrname = argv[1]
        pwd = argv[2]
        db_name = argv[3]
        stt = str(argv[4])

        db = MySQLdb.connect(user=usrname, port=3306, passwd=pwd, db=db_name)
        c_ursor = db.cursor()
        query = "SELECT * FROM states
        WHERE BINARY name = %s  ORDER BY states.id"
        c_ursor.execute(query, (stt,))
        rows = c_ursor.fetchall()

        for eachRow in rows:
            print("{}".format(eachRow))
