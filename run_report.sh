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





exit 0

