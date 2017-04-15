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
#        AUTHOR: Cayden Allen ,  caydenallen@mail.weber.edu
#  ORGANIZATION:
#       CREATED: 03/03/2017 14:27
#      REVISION:  ---
#===========================================================================

import sys
import os
import zipfile
import sqlite3

#beg_date = sys.argv[1]
#end_date = sys.argv[2]
eCode = ' '
#bDate = ""
#eDate = ""


def help():
    """
    Help Funciton
    """
    print("Usage is: " + sys.argv[0] + "<begDate>  <endDate>")
    exit(1)



def verify(date):
    """
    Verify correct date length
    """
    if len(date) == 8 and date.isdigit():
        return True
    else:
        return False


def convert_date():
    """
    Args:
        beg_date(YYYYMMDD), end_date(YYYYMMDD)
    returns:
        YYYY-MM-DD hh:mm
    """
    
    if len(sys.argv) > 1:
        beg_date = sys.argv[1]
        end_date = sys.argv[2]
    else:
        help()
    #beg_date = sys.argv[1]
    #end_date = sys.argv[2]
    global eDate 
    global bDate 
    
    if verify(beg_date) and verify(end_date):
        bDate = beg_date[:4]+'-'+beg_date[4:6]+'-'+beg_date[6:]+ ' 00:00:00'
        eDate = end_date[:4]+'-'+end_date[4:6]+'-'+end_date[6:]+ ' 23:59:59'
        #print("after conversion", bDate, eDate)
    else:
        exit(1)
        eCode = '1'
    


def query():
    """
    Pulls the arguments when the script is called
    """
    
    #connect to db
    conn = sqlite3.connect('hw8SQLite.db')
    c=conn.cursor()

    #variables managing report data
    report =""
    transID = -1
    total = 0
    fill = '00000000          '
    count = 0

    #Query database
    for row in c.execute("SELECT trans_id, trans_date, card_num, qty, amt, prod_desc, total FROM trans LEFT JOIN trans_line USING (trans_id) LEFT JOIN products USING (prod_num) WHERE trans_date > '" + bDate +"' AND trans_date < '" + eDate +"'"):
        if row[5] is None:
            desc =''
        else:
            desc = row[5]
        #Determine if same transaction  
        if transID != row[0]:
            #Generate report Data for new transaction
            if report == "":
                report = '{s:{c}>{n}}'.format(s=str(row[0]),n=5,c='0')      
            else:
                #fills in blank products in report
                while (count < 3):                   
                    report += fill      
                    count += 1                                                                                                                      
                
                #adds total tothe new transaction
                report += '{s:{c}>{n}}'.format(s=str('{:.2f}'.format(total)).replace('.',''),n=6,c='0')
                report += '\n{s:{c}>{n}}'.format(s=str(row[0]),n=5,c='0')
                            
            #Adds first product to report         
            transDate = row[1].replace(':','')
            transDate = transDate.replace('-','')
            transDate = transDate.replace(' ','')
            transDate = str(transDate[:12])     
            report += transDate + str(row[2][-6:]) 
            if row[3] is None:
                report += '{s:{c}>{n}}'.format(s='0',n=2,c='0')
            else:
                report += '{s:{c}>{n}}'.format(s=str(int(row[3])),n=2,c='0')
            if row[4] is None:
                price = 0
            else:
                price = '{:.2f}'.format(row[4])
            price = '{s:{c}>{n}}'.format(s=str(price).replace('.',''),n=6,c='0')
            report += price + '{s:{c}<{n}}'.format(s=desc,n=10,c=' ')
            transID=row[0]  
            total = row[6]
            count = 1
        else:
            #Adds remaining products
            report += '{s:{c}>{n}}'.format(s=str(int(row[3])),n=2,c='0')
            price = '{:.2f}'.format(row[4])
            price = '{s:{c}>{n}}'.format(s=str(price).replace('.',''),n=6,c='0')
            report += price + '{s:{c}<{n}}'.format(s=desc,n=10,c=' ')
            total += row[6]
            count += 1
        #Print last entry of report
    #Determine if data in query

    if report == "":     
        eCode = '-2'
        #exit -2
        exit(2)
    else:
        while (count < 3):
            report += fill
            count += 1
        eCode = '0'
        #exit = 0
        #adds total then then the new transaction
        report += '{s:{c}>{n}}'.format(s=str('{:.2f}'.format(total)).replace('.',''),n=6,c='0')
    print(report)

    #Create file for report
    text_file = open ('company_trans_'+ sys.argv[1] + '_'+ sys.argv[2]+'.dat', 'w')
    text_file.write('%s' % report)
    text_file.close()
    
    return(eCode)


def zip_file(): 
    #Zip file
    with zipfile.ZipFile('company_trans_'+ sys.argv[1] + '_'+ sys.argv[2]+'.dat.zip', 'w') as myzip:
        myzip.write('company_trans_'+ sys.argv[1] + '_'+ sys.argv[2]+'.dat')

    #print('exit code would be ' + str(eCode))



#Main Function
def main():
    """
    Test Function
    """
    convert_date()
    query()
    #zip_file()


if __name__=="__main__":
    # Call Main
    main()

    exit(0)
