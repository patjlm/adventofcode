BEGIN {
    position = 0
    depth = 0
    aim = 0
}

{
    action = $1
    count = $2
    if (action == "forward") {
        position += count
        depth += aim * count
    }
    if (action == "down") {
        aim += count
    }
    if (action == "up") {
        aim -= count
    }
    next
}

END {
    print "position="position" ; depth="depth
    print position * depth
    # 1997106066
}
