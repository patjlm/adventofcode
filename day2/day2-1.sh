#!/bin/sh

position=0
depth=0

forward() {
    position=$((position+$1))
}
down() {
    depth=$((depth+$1))
}
up() {
    depth=$((depth-$1))
}

# while read line ; do
#     # action=$(echo "$line" | cut -f1 -d" ")
#     # count=$(echo "$line" | cut -f2 -d" ")
#     # echo "action=$action ; count=$count"
#     # $action $count
#     $line
# done < day2.input
. day2.input

echo "result: $((position*depth))"
# 1936494
