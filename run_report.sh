#! /bin/sh
#
# run_report.sh
# Copyright (C) 2017 student1 <student1@CS3030_87>
#
# Distributed under terms of the MIT license.
#



#!/bin/bash -
#===============================================================================
#
#          FILE: run_report.sh
#
#         USAGE: ./run_report.sh
#
#   DESCRIPTION:
#
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Micheal Brewer (), mbrewerramirez@mail.weber.edu
#		 AUTHOR: Gavin Brimhall, gavinbrimhall@mail.weber.edu
#		 AUTHOR:
#  ORGANIZATION:
#       CREATED: 04/05/2017 21:14
#      REVISION:  ---
#===============================================================================

#set -o nounset                  # Treat unset variables as an error


# how the script is suppose to be used.
usage()
{
	echo "Invalid Option"
	echo "Usage: $0 [-f BeginDate] [-t EndDate] [-e email] [-u FTPusername] [-p password]"
	echo " -f -t -e -u -p are required."
	exit 1
}

# if the user desires to use $0 --help
if [[ $1 == "--help" ]]
then
	usage
fi


# Getopts while loop
while getopts ":f:t:e:u:p:" opt
do
    case $opt in
		f) begDate=$OPTARG #first opt
			;;
		t) endDate=$OPTARG #second opt
			;;
		e) email=$OPTARG # third opt
			;;
		u) user=$OPTARG # fourth opt
			;;
		p) passwd=$OPTARG # fifth opt
			;;
		\?)
			usage
			;;
	esac
done


#IF statement to test if parameters are set. -z checks to see if value is null
if [[ -z $begDate ]] || [[ -z $endDate ]]
then
	usage
elif [[ -z $email ]] || [[ -z $user ]]
then
	usage
elif [[ -z $passwd ]]
then
	usage
fi


#HOST = "137.190.19.87"
#File = 'company_trans_'+$begDate+'_'+$endDate+'.dat'

#File = "company_trans_${begDate}'_'${endDate}.dat"

# FTP transfer
ftp(){
	File = "company_trans_${begDate}'_'${endDate}.dat"
	ftp -n "137.190.19.87" <<END_SCRIPT
	quote USER $user
	quote PASS $passwd
	binary
	put $File
	quit
END_SCRIPT
exit 0
}


# Do wrapper
#create_report($begDate $endDate)
#exit_code =

#CHANGE THE PYTHON command
python3 ./create_report.py $begDate $endDate
ret=$?

if [[ $ret == 0 ]]
		date=`date +%Y_%m_%d_%H:%M`
		echo "Zipping up new file"
		python -c 'import create_report.py; create_report.zip_file()'  #attempt to call python function for zip
		echo "Transferring to FTP"
		ftp
		echo "Sending confirmation to email: $email"
		` mail -s "Successfully transfered file ($HOST) " $email <<< "Successfully created a transaction report from $begDate to $endDate"`

else if [[ $ret == 1 ]]
		echo "Sending error -1 to email: $email"
		` mail -s "The create_report program exit with code -1 " $email <<< "Bad Input parameters begin date: $begDate and end date: $endDate"`

else if [[ $ret == 2 ]]
		echo "Sending error -2 to email: $email"
		` mail -s "The create_report program exit with code -2 " $email <<< "No Transaction available from begin date: $begDate to end date: $endDate"`


exit 0
