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
#		 AUTHOR: Cayden Allen, caydenallen@mail.weber.edu
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
dates=$begDate\_$endDate
theFile=company_trans_$dates.dat
toZip=company_trans_$dates.dat.zip

# FTP transfer
ftp()
{
	ip="137.190.19.87"
	ftp -nv $ip <<END_SCRIPT
	quote USER $user
	quote PASS $passwd
	put $toZip
	quit
END_SCRIPT
exit 0
}


# Do wrapper
#create_report($begDate $endDate)
#exit_code =
PYTHON="/usr/bin/python3"

#CHANGE THE PYTHON command
python3 ./create_report.py $begDate $endDate
ret=$?
#dates=$begDate\_$endDate
#theFile=company_trans_$dates.dat
#toZip=company_trans_$dates.dat.zip


if [[ $ret == 0 ]]
then	
	date=`date +%Y_%m_%d_%H:%M`
		echo "Zipping up new file"
		#`$PYTHON -c 'import create_report.py; create_report.zip_file()'`  #attempt to call python function for zip
		#zip 'company_trans_'$begDate'_'$endDate'.dat.zip' 'company_trans_'$begDate'_'$endDate'.dat'
		zip $toZip $theFile
		echo "Transferring to FTP"
		ftp
		echo "Sending confirmation to email: $email"
		` mail -s "Successfully transfered file ($HOST) " $email << "Successfully created a transaction report from $begDate to $endDate"`

	elif [[ $ret == 1 ]]
	then	
		echo "Sending error -1 to email: $email"
		` mail -s "The create_report program exit with code -1 " $email <<< "Bad Input parameters begin date: $begDate and end date: $endDate"`

	elif [[ $ret == 2 ]]
	then
		echo "Sending error -2 to email: $email"
		` mail -s "The create_report program exit with code -2 " $email <<< "No Transaction available from begin date: $begDate to end date: $endDate"`
	fi

exit 0
