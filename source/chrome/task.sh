#!/bin/bash  
  
step=10 #间隔的秒数，不能大于60  
  
for (( i = 0; i < 60; i=(i+step) )); do  
    $(/opt/anaconda/bin/python '/usr/application/autoreplay/chrome/earthquake_email.py')  
    sleep $step  
done  
  
exit 0  