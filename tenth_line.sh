#!/bin/bash
# Xiang Wang @ 2017-05-12 15:52:02

filename="data/tenth_line.txt"
a=`head -10 $filename`
line=`head -10 $filename | wc | awk '{print $1}'`
if [ $line != "10" ]
then
    :
else
    echo `head -10 $filename | tail -n 1`
fi
