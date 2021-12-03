BEGIN {
    # position = 0
    # depth = 0
}

/forward / {
    position += $2
    next
}
/down / {
    depth += $2
    next
}
/up / {
    depth -= $2
    next
}

END {
    print position * depth
}

# 1936494
