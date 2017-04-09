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
    beg_date = '20170402'
    end_date = '20170402'
    if len(beg_date) != 8 || len(end_date) != 8 || isinstance(beg_date,int) != True || isinstance(end_date,int) != True:
        eCode = -1
    #exit -1
    if int(beg_date[4:6]) > 12 || int(end_date[4:6]) > 12:
        eCode = -1
    #exit -1
    if int(beg_date[6:8]) >31 || int(end_date[6:8]) > 31:
        eCode = -1
    #   exit -1

    #Create Date Varaiables
    bDate = str(beg_date[:4]) + "-" + str(beg_date[4:6]) + "-" + str(beg_date[6:8]) + " 00:00"
    eDate = str(end_date[:4]) + "-" + str(end_date[4:6]) + "-" + str(end_date[6:8]) + " 23:59"

    #getcurrent directory of file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sqlPath = dir_path + "/hw8SQLite.db"

    #connect to db
    conn = sqlite3.connect(sqlPath)
    c=conn.cursor()


    report = ""
    transID = -1
    total = 0
    fill = '0000000          '
    count = 0
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
                    report += '{s:{c}>{n}'.format(s=str('{:.2f}'.format(total)).replace('.',''),n=6, c='0')
                    report += '\n{s:{c}>{n}}'.format(s=str(row[0]),n=5, c='0')

                # Adds first product to report
                transDate = row[1].replace(':','')
                transDate = transDate.replace('-','')
                transDate = transDate.replace(' ','')
                transDate = str(transDate[:12])     
                report += transDate + str(row[2][-6:]) 
                report += '{s:{c}>{n}}'.format(s=str(int(row[3])),n=2,c='0')
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
            print('exit code would be ' + str(eCode)
    
    
    
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
