#!/bin/bash
proc=`ps -ef | grep -v grep | grep getstockhistorydata.py`

cmd="hemaobin  9613 25488  1 16:19 pts/22   00:00:13 python3 ./getstockhistorydata.py"

pid=`echo $proc | awk -F' ' '{ print $2 }'`
kill -9 $pid

echo "$pid" >> /home/hemaobin/what.txt
date >> /home/hemaobin/what.txt
