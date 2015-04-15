__author__ = 'martin.valenzuela'

from look import array_from_file
from look import create_type_array
from sqlalchemy.orm import sessionmaker
from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, Float, Index, Integer, Numeric, SmallInteger, String, Text, VARBINARY, text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta
from sqlalchemy import desc
from sqlalchemy import update
from sqlalchemy import connectors as conn
from sqlalchemy.orm.exc import MultipleResultsFound
from os import system
from authentication import mysql_engine_test



Base = declarative_base()

db = mysql_engine_test()

Session = sessionmaker()
Session.configure(bind=db)

session = Session()



class NewTable(Base):
    __tablename__ = u'New_Table'

    key_id = Column(Integer, primary_key=True)
    id = Column(Integer, nullable=True)
    space_type = Column(String(1), nullable=True)
    advt_details_id = Column(Integer, nullable=True)
    placement_position_id = Column(Integer, nullable=True)


if __name__ == '__main__':
    file = ''
    # while file != 'exit':
    try:
        file_name = raw_input('Please enter file name: ')
        file = '/Users/martin.valenzuela/Desktop/SFDC_exports/' + file_name + '.csv'
        csv_info = array_from_file(file)
        print csv_info
        type_array = create_type_array(csv_info, file_name)

        print(''.join(type_array))



    except IOError:
        print 'Try Again'