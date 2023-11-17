#!/usr/bin/python3
import MySQLdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine = create_engine('sqlite:///:memory:', echo=True)

#Session = sessionmaker(bind=engine)
#session = session()



if __name__ == '__main__':
    if len(sys.argv) == 4:
        argv = sys.argv
        username = argv[1]
        password = argv[2]
        db_name = argv[3]

        db=MySQLdb.connect(user=username ,passwd=password, db=db_name)
        c_ursor=db.cursor()
        c_ursor.execute("SELECT states FROM (%s)",(db_name, ))
