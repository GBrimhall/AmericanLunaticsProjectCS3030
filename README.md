# AmericanLunaticsProjectCS3030

Homework Assignment 8 Group Project
Authors: Micheal Brewer, Cayden Allen, Gavin Brimhall
CS 3030 – Hugo Valle


The purpose of the these scripts is to search through a database by year and pull all transactions duing that time frame. 

# Script Usage

`run_report.sh`

$ bash `run_report.sh` <-f BeginDate> <-t EndDate> <-e email> <-u FTPusername> <-p password>

`create_report.py`

$ python3 `create_report.py` <BeginDate> <EndDate>

# What each file does.

- The `run_report.sh` calls the `create_report.py` and passes it the dates taken in the arguments. After the python script has run it will send an email depending on teh exit code. If 0 it will zip the output file, ftp it, and email success. If 1 the dates were not inputted correctly and it will send an eroor email. If 2 there were no transactions on the dates provided and an email is sent.
- The `create_report.py` takes the dates given from the bash script and converts them to match the database files. It will then run SQLite and query for the transactions. Once the transactions are queried it will organize them into a fix-legnth. 
