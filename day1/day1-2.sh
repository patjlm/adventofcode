#!/bin/sh

minus3=0
minus2=0
minus1=0
current=0
count=0
# previous_sum=0
for input in $(cat day1.input) ; do
    minus3=$minus2
    minus2=$minus1
    minus1=$current
    current=$input
    # do something only once we have enough data
    if [ ! $minus3 -eq 0 ] ; then
        # b=$((minus2+minus1+current))
        # if [ $b -gt $previous_sum ] ; then
        # comparing minus3+minus2+minus1 and minus2+minus1+current is 
        # the same as comparing minus3 and current
        if [ $current -gt $minus3 ] ; then
            count=$((count+1))
        fi
    fi
    # previous_sum=$((minus3+minus2+minus1))
done

echo "count: $count"
# 1633
