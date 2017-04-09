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
import os


def query_data():
    """
    query the db
    """


    #connect to db
    conn = sqlite3.connect('hw8SQLite.db')
    c=conn.cursor()


    report = ""
    transID = -1
    total = 0
    fill = '0000000          '
    count = 0
    bDate = '2017-04-02 00:00'
    eDate = '2017-04-02 23:59'
    # Query data AJ
    for row in c.execute("""SELECT trans_id, trans_date, card_num, qty, amt, prod_desc 
                            FROM trans 
                            LEFT JOIN trans_line USING (trans_id) 
                            LEFT JOIN products USING (prod_num) 
                            WHERE trans_date > '""" + bDate +"' AND trans_date < '" + eDate +"'"):
        if row[0] is None:
                    print("nothing") 
            #Determine if same transaction
        if transID != row[0]:
                #Generate report Data from new transaction
                if report == "":
                    report = '{s:{c}>{n}}'.format(s=str(row[0]),n=5,c='0')
                else:
                    # Fills in blank products in report
                    while (count < 3):
                        report += fill
                        count += 1

                    #adds total to the new transaction
                    report += '{s:{c}>{n}}'.format(s=str('{:.2f}'.format(total)).replace('.',''),n=6, c='0')
                    report += '\n{s:{c}>{n}}'.format(s=str(row[0]),n=5, c='0')

                # Adds first product to report
                transDate = row[1].replace(':','')
                transDate = transDate.replace('-','')
                transDate = transDate.replace(' ','')
                transDate = str(transDate[:12])     
                report += transDate + str(row[2][-6:]) 
                report += '{s:{c}>{n}}'.format(s=str(row[3])),n=2,c='0')
                price = '{:.2f}'.format(row[4])
                price = '{s:{c}>{n}}'.format(s=str(price).replace('.',''),n=6,c='0')
                report += price + '{s:{c}<{n}}'.format(s=row[5],n=10,c=' ')
                transID=row[0]  
                total = row[4]
                count = 1
            # Print last entry of report
        #Determine if data in query

            if report =="":
                eCode =-2
                #exit -2
            else:
                while (count < 3):
                    report += fill
                    count+= 1
                eCode = 0
            #exit = 0
            # adds total then the new transaction
            report += '{s:{c}>{n}}'.format(s=str('{:.2f}'.format(total)).replace('.',''),n=6,c='0')
            print(report)
            print('exit code would be ' + str(eCode))
    
    
    
    #close the cursor

    #close connection
    #conn.close()



    # test exist Not return -2




def fix_len(data):
    """
    Format of the return
    """
    #sort data
    #print(format)
    #return 0
    pass

#Main Function
def main():
    """
    Test Function
    """
    query_data()
    #dateF =  Date('20170402,'20170402')







if __name__=="__main__":
    # Call Main
    main()

    exit(0)
