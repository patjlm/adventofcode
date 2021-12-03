BEGIN {
    # position = 0
    # depth = 0
    # aim = 0
}

/forward / {
    position += $2
    depth += aim * $2
    next
}
/down / {
    aim += $2
    next
}
/up / {
    aim -= $2
    next
}

END {
    print position * depth
}

# 1997106066
