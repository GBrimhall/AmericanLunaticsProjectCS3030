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
#		 AUTHOR:
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
else [[ -z passwd ]]
then
	usage
fi

host="137.190.19.99" #address

file=$(find ./ -name "Place_Holder") 
ftp_success_msg="226 Transfer Complete"
ftplog=$PWD/tmp/ftplogfile


echo "Logging into ftp server as $user"
	ftp -nv $host <<EOF > $ftplog
		quote user $user
			quote pass $pass
				put $file
					bye

EOF

grep "230 Login successful" $ftplog
grep "226 Transfer complete" $ftplog
rc=$?

if [[ $rc -eq 0 ]]
then
echo "ftp OK"
else
echo "ftp Error"
exit 1
fi


exit 0

