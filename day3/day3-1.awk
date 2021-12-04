function bitsToString(bits) {
    res = 0
    for (i=1; i<=12; i++) {
        res = or(lshift(res, 1), bits[i])
    }
    return res
}

BEGIN {
    split("000000000000", ONES, "")
    split("000000000000", MAJORITY, "")
    split("000000000000", MINORITY, "")
    LINES = 0
}
{
    LINES += 1
    len = split($0, chars, "")
    for (i=1; i <= len; i++) {
        ONES[i] += chars[i]
    }
    next
}
END {
    for (i=1; i <= 12; i++) {
        if (ONES[i] > LINES / 2) {
            MAJORITY[i] = 1
        } else {
            MINORITY[i] = 1
        }
    }
    GAMMA = bitsToString(MAJORITY)
    EPSILON = bitsToString(MINORITY)
    print GAMMA * EPSILON
}

# gamma=1300 ; epsilon=2795
# 3633500
