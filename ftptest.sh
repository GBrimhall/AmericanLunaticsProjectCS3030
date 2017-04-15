
#!/bin/bash - 
#===============================================================================
#
#          FILE: ftptest.sh
# 
#         USAGE: ./ftptest.sh 
# 
#   DESCRIPTION: 
# 
#       OPTIONS: ---
#  REQUIREMENTS: ---
#          BUGS: ---
#         NOTES: ---
#        AUTHOR: Micheal Brewer (), mbrewerramirez@mail.weber.edu
#  ORGANIZATION: 
#       CREATED: 04/15/2017 13:03
#      REVISION:  ---
#===============================================================================

#set -o nounset                  # Treat unset variables as an error

dates='20170402_20170402'
file="company_trans_$dates.dat.zip"
HOST="137.190.19.85"
user="Student1"
pass="I am the shit 91"
ftp -pnv $HOST <<ZZTOP
quote USER $user
quote PASS $pass
put $file
quit
ZZTOP







exit 0

