BEGIN {
    A = 0
    B = 0
    C = 0
    A_COUNT = 0
    count = 0
    previous = -1
}

/[0-9]+/ {
    if (A_COUNT < 3) {
        A += $1
        A_COUNT += 1
    }
    if (A_COUNT >= 2) {
        B += $1
    }
    if (A_COUNT == 3) {
        C += $1
    }

    if (A_COUNT == 3) {
        if (previous > 0) {
            if (A > previous) {
                count += 1
            }
        }
        previous = A
        A = B
        A_COUNT = 2
        B = C
        C = 0
    }
    next
}

{
    print "invalid input: "$0
}

END {
    print "count: "count
    # 1633
}
