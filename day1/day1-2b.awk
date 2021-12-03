BEGIN {
    # MINUS3 = 0
    MINUS2 = -1
    MINUS1 = -1
    CURRENT = -1
    COUNT = 0
}

/[0-9]+/ {
    MINUS3 = MINUS2
    MINUS2 = MINUS1
    MINUS1 = CURRENT
    CURRENT = $1
    # do something only once we have enough data
    if (MINUS3 != -1) {
        # comparing minus3+minus2+minus1 and minus2+minus1+current is 
        # the same as comparing minus3 and current
        if (CURRENT > MINUS3) {
            COUNT += 1
        }
    }
    next
}

{
    print "invalid input: "$0
}

END {
    print "count: "COUNT
    # 1633
}
