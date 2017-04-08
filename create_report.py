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


def verify(date):
    """
    Verify correct date length
    """

    if len(date) == 8 and date.isdigit():
        return True
    else:
        return False


def Date(beg_date, end_date):
    """
    Translate the date taken in
    ARGS:
        beg_date(YYYYMMDD), end_date(YYYYMMDD)
    returns:
        YYYY-MM-DD hh:mm
    """
<<<<<<< HEAD
    
    BD =  datetime.datetime.strptime(beg_date, '%Y%m%d').strftime('%Y-%m-%d')
    print(type(BD), BD)
    BegDate = BD + ' 00:00:00'
    print(BegDate)
    ED =  datetime.datetime.strptime(end_date, '%Y%m%d').strftime('%Y-%m-%d')
    print(type(BD), BD)
    EndDate = ED + ' 23:59:59'
    print(EndDate)
    #Return BegDate, EndDate
    #bad input return -1
=======
   
    if verify(beg_date) and verify(end_date):
        bDate = beg_date[:4]+'-'+beg_date[4:6]+'-'+beg_date[6:]+ ' 00:00:00'
        eDate = end_date[:4]+'-'+end_date[4:6]+'-'+end_Date[6:]+ ' 23:59:59'
    else:
        exit(-1)
>>>>>>> origin/cayden


def query_data():
    """
    query the db
    """
    
    #Connect to DB
    conn = sqlite3.connect('hw8SQLite.db')
    if (conn):
        print("Connected to DB")
        print("")
    c = conn.cursor()
    
    # Original query
    #c.execute("""SELECT T.trans_id, T.trans_date, 
        #T.card_num, TL.Qty, TL.amt, P.prod_desc, T.total 
        #FROM trans T 
        #LEFT JOIN trans_line TL ON T.trans_ID=TL.trans_ID 
        #LEFT JOIN products P ON TL.prod_num=P.prod_num 
        #WHERE trans_date 
        #BETWEEN "2017-04-02 00:00" AND "2017-04-02 23:59" 
        #ORDER BY T.trans_ID""")
    #recs = c.fetchall()
    #for row in recs:
        #print(row)    
    
    
    #group_concat(name separator ',')
    #c.execute("""SELECT T.trans_id, T.trans_date,
        #T.card_num, group_concat(TL.Qty), 
        #group_concat( TL.amt),group_concat(P.prod_desc), T.total 
        #FROM trans T 
        #LEFT JOIN trans_line TL ON T.trans_ID=TL.trans_ID 
        #LEFT JOIN products P ON TL.prod_num=P.prod_num 
        #WHERE trans_date BETWEEN "2017-04-02 00:00" AND "2017-04-02 23:59" 
        #GROUP BY T.trans_ID 
        #ORDER BY T.trans_ID""")
    #recs = c.fetchall()
    #for row in recs:
        #print(row)   
    
    c.execute("""SELECT T.trans_id, T.trans_date, 
            T.card_num, TL.Qty, TL.amt, P.prod_desc, T.total 
            FROM trans T 
            LEFT JOIN trans_line TL ON T.trans_ID=TL.trans_ID 
            LEFT JOIN products P ON TL.prod_num=P.prod_num 
            WHERE trans_date 
            BETWEEN "2017-04-02 00:00" AND "2017-04-02 23:59" 
            ORDER BY T.trans_ID""")
     
    recs = c.fetchall()
    index = 0
    for row in recs:
    #l = [list(row) for row in recs]
        while row[0] == index
            
        index += 1
        print(row[0])
    
    
    
    
    
    
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
<<<<<<< HEAD
    #dateF =  Date('20170402,'20170402')
=======

>>>>>>> origin/cayden






if __name__=="__main__":
    # Call Main
    main()

    exit(0)
