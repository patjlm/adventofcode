BEGIN {
    position = 0
    depth = 0
}

{
    action = $1
    count = $2
    if (action == "forward") {
        position += count
    }
    if (action == "down") {
        depth += count
    }
    if (action == "up") {
        depth -= count
    }
    next
}

END {
    print "position="position" ; depth="depth
    print position * depth
    # 1936494
}
