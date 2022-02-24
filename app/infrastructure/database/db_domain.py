### UML

import uuid

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Tutorial: https://realpython.com/python-sqlite-sqlalchemy/#working-with-sqlalchemy-and-python-objects
class CustomerDBObject(Base):
    # table name
    __tablename__ = 'customer'
    # columns in the table
    customer_id = Column(Integer, primary_key=True)
    organisation_or_person = Column(sqlalchemy.String)
    organisation_name = Column(sqlalchemy.String)
    gender = Column(sqlalchemy.String)
    first_name = Column(sqlalchemy.String)
    middle_name = Column(sqlalchemy.String)
    last_name = Column(sqlalchemy.String)
    email_address = Column(sqlalchemy.String)
    login_name = Column(sqlalchemy.String)
    login_password = Column(sqlalchemy.String)
    phone_number = Column(sqlalchemy.String)
    address_part_1 = Column(sqlalchemy.String)
    address_part_2 = Column(sqlalchemy.String)
    address_part_3 = Column(sqlalchemy.String)
    address_part_4 = Column(sqlalchemy.String)
    town_city = Column(sqlalchemy.String)
    state = Column(sqlalchemy.String)
    country = Column(sqlalchemy.String)
    # foreign keys


