#!/usr/bin/python3
''' Module to execute mysql command'''


import MySQLdb
import sys

'''engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = session()
'''

if __name__ == '__main__':
    if len(sys.argv) == 4:
        argv = sys.argv
        username = argv[1]
        password = argv[2]
        db_name = argv[3]

        db = MySQLdb.connect(host='localhost', user=username, passwd=password, db=db_name)
        c_ursor = db.cursor()
        c_ursor.execute("SHOW TABLES")
        #c_ursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")
