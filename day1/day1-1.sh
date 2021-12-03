#!/bin/sh

previous=-1
count=0
# previous_sum=0
for input in $(cat day1.input) ; do
    # do something only once we have enough data
    if [ ! $previous -eq -1 ] ; then
        if [ $input -gt $previous ] ; then
            count=$((count+1))
        fi
    fi
    previous=$input
done

echo "count: $count"
# 1602
