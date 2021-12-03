#!/bin/sh

input=${1:-day2.input}

position=0
depth=0
aim=0

forward() {
    position=$((position + $1))
    depth=$((depth + (aim * $1)))
}
down() {
    aim=$((aim + $1))
}
up() {
    aim=$((aim - $1))
}

. "$input"

echo "result: $((position * depth))"

# 1997106066
