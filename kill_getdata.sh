#!/bin/bash
proc=`ps -ef |grep  -v grep | grep getdata.py`
pid=`echo $proc | awk '{print$2}'`
echo $proc
echo $pid

kill -9 $pid
