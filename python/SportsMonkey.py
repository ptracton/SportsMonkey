#! /usr/bin/env python3


import logging
import pandas as pd
import ORM

if __name__ == "__main__":
    logging.basicConfig(filename="SportsMonkey.log",
                        level=logging.INFO,
                        format='%(asctime)s,%(levelname)s,%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    print("Sports Monkey is a Go!")
    CSVFile = "../data/airyards.csv"

    TableName = "Players"
    if not ORM.tableExists(ORM.inspector, TableName):
        logging.info("Creating Table {} from {}".format(TableName, CSVFile))
        ORM.csvToTable(CSVFile, tableName="Players", db=ORM.db)

    RBPlayers = ORM.session.query(ORM.Players).filter(
        ORM.Players.position == """RB""").all()

    for x in RBPlayers:
        print("{:20} {:4}".format(x.full_name, x.position))
