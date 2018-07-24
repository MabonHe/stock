#!/bin/bash

    process=`ps -ef | grep -v grep | grep getstockhistorydata.py`
    if [ ! -z "${process}" ];then
        echo "what the fuck" > /home/hemaobin/what_fuck.txt
    else
        date >> /home/hemaobin/check.txt
        pushd /home/hemaobin/workspace/stock/; ./getstockhistorydata.py &
    fi
