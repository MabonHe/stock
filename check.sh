#!/bin/bash

    process=`ps -ef | grep -v grep | grep getdata.py`
    if [ ! -z "${process}" ];then
        echo "what the fuck" > /home/hemaobin/what_fuck.txt
    else
        date >> /home/hemaobin/check.txt
        /home/hemaobin/workspace/stock/getdata.py &
    fi
