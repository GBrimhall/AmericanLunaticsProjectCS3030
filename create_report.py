#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 student1 <student1@CS3030_87>
#


#===========================================================================
#
#       File: create_report.py 
#
#       Usage: ./create_report.py
#
#   Description:
#
#       Options: ---
#       ReqOPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Micheal Brewer (), mbrewerramirez@mail.weber.edu
#        AUTHOR:
#        AUTHOR:
#  ORGANIZATION:
#       CREATED: 03/03/2017 14:27
#      REVISION:  ---
#===========================================================================

import sys
import sqlite3
import time
import datetime



def Date(beg_date, end_date):
    """
    Translate the date taken in
    ARGS:
        beg_date(YYYYMMDD), end_date(YYYYMMDD)
    returns:
        YYYY-MM-DD hh:mm
    """
    



    #bad input return -1


def query_data():
    """
    query the db
    """
    
    #Connect to DB
    conn = sqlite3.connect('hw8SQLite.db')
    if (conn):
        print("Connected to DB")
    c = conn.cursor()
    c.execute('SELECT T.trans_id, T.trans_date, T.card_num, TL.Qty, TL.amt, P.prod_desc, T.total FROM trans T INNER JOIN trans_line TL ON T.trans_ID=TL.trans_ID INNER JOIN products P ON TL.prod_num=P.prod_num WHERE trans_date BETWEEN "2017-04-02 00:00" AND "2017-04-02 23:59" ORDER BY T.trans_ID')
    recs = c.fetchall()
    for row in recs:
        print(row)
    #close the cursor

    #close connection
    conn.close()



    # test exist Not return -2




def fix_len(data):
    """
    Format of the return
    """
    #sort data
    #print(format)
    #return 0


#Main Function
def main():
    """
    Test Function
    """
    query_data()







if __name__=="__main__":
    # Call Main
    main()

    exit(0)
