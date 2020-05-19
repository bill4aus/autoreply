#!/bin/bash 
#Process name 
#longger than 30m ,kill

# NAME="phantom"
# for PID in `ps -A | grep "$NAME"|awk '{split($3,tab,/:/); if(tab[2]+tab[1]*60>=10) {print $1}}'` 
# do
#     print $PID
#     kill -9 $PID
#     sleep 3
# done



kill -9 `ps -ef |grep phantom|awk '{print $2}' `
echo 1 > /proc/sys/vm/drop_caches

# kill -9 `ps -ef |grep phantom|awk '{print $2}' `
# echo 1 > /proc/sys/vm/drop_caches


# ls -l |grep "json"|wc -l
# find . -name "*" -type f -size -200c  | xargs -n 1 rm -f