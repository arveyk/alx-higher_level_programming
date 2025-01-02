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
        state = argv[4]

        db = MySQLdb.connect(user=usrname,
                             passwd=password, db=db_name)
        c_ursor = db.cursor()
        qry = '''SELECT cities.name\
                FROM  cities INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name=%s'''
        c_ursor.execute(qry, (state,))
        rows = c_ursor.fetchall()

        count = 0
        len_query = len(rows)
        for eachRow in rows:
            print("{}".format(eachRow[0]), end='')
            count += 1
            if count < len_query:
                print(', ', end='')
        print()
