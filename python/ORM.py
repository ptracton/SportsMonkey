"""
FILE: ORM.py

This file handles all SQLAlchemy ORM related operations and classes 

"""

import logging
import traceback

import pandas as pd

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# Global Setup
db_string = 'sqlite:///../database/sports_monkey.db'

db = sqlalchemy.create_engine(db_string)
base = sqlalchemy.ext.declarative.declarative_base()
inspector = sqlalchemy.inspect(db)
Session = sqlalchemy.orm.sessionmaker(db)
session = Session()
base.metadata.create_all(db)


def tableExists(inspector=None, table=None):
    """
    Returns true if this table exists in this database
    and false otherwise
    """
    return (table in inspector.get_table_names())


def csvToTable(fileName=None, tableName=None, db=None):
    """
    Read this fileName, expected to be a CSV file, and put it
    into the tableName of this database 
    """
    try:
        df_csv = pd.read_csv(fileName)
        df_csv.columns = [c.lower() for c in df_csv.columns]
        df_csv.to_sql(tableName, db)
        logging.info("PASSED to create table {} from CSV file {}".format(
            tableName, fileName))
        return True
    except Exception:
        logging.error("FAILED to create table {} from CSV file {}".format(
            tableName, fileName))
        print(traceback.format_exc())
        logging.error(traceback.format_exc())
        return False


class Players(base):
    """
    Data downloaded from http://www.airyards.com/tables.html
    """

    __tablename__ = "Players"
    id = sqlalchemy.Column(sqlalchemy.Numeric, primary_key=True)
    full_name = sqlalchemy.Column(sqlalchemy.String)
    position = sqlalchemy.Column(sqlalchemy.String)
    team = sqlalchemy.Column(sqlalchemy.String)
    targets = sqlalchemy.Column(sqlalchemy.Integer)
    rec = sqlalchemy.Column(sqlalchemy.Integer)
    rec_yards = sqlalchemy.Column(sqlalchemy.Integer)
    air_yards = sqlalchemy.Column(sqlalchemy.Integer)
    yac = sqlalchemy.Column(sqlalchemy.Integer)
    td = sqlalchemy.Column(sqlalchemy.Integer)
    adot = sqlalchemy.Column(sqlalchemy.Float)
    racr = sqlalchemy.Column(sqlalchemy.Float)
    ms_air = sqlalchemy.Column(sqlalchemy.Float)
    tgt_share = sqlalchemy.Column(sqlalchemy.Float)
    wopr = sqlalchemy.Column(sqlalchemy.Float)
    ppr = sqlalchemy.Column(sqlalchemy.Float)
