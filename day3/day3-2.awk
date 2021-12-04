function bitsToString(bits) {
    res = 0
    for (i=1; i<=12; i++) {
        res = or(lshift(res, 1), bits[i])
    }
    return res
}

BEGIN {
    # split("000000000000", ONES, "")
    # split("000000000000", MAJORITY, "")
    # split("000000000000", MINORITY, "")
    # LINES = 0
}
{
    LINES += 1
    INPUT[LINES] = $0
    len = split($0, chars, "")
    # for (i=1; i <= len; i++) {
    #     ONES[i] += chars[i]
    # }
    next
}
function copyArray(a, b) {
    for (i in a) {
        b[i] = a[i]
    }
}
function printArray(a) {
    for (i in a)
        print a[i]
}
END {
    copyArray(INPUT, FILTERED)
    count = LINES
    for (pos=1; pos<=12; pos++) {
        one_count = 0
        for (i=1; i<=count; i++) {
            if (and(1, rshift(FILTERED[i], 12-pos)) == 1) {
                one_count += 1
                FILTER1[one_count] = FILTERED[i]
            } else {
                FILTER0[i - one_count] = FILTERED[i]
            }
        }

        if (one_count < LINES/2) {
            majority = 0
            count = count - one_count
            copyArray(FILTER0, FILTERED)
        } else {
            majority = 1
            count = one_count
            copyArray(FILTER1, FILTERED)
        }
        if (count == 1) {
            print "Found oxygen_rating"
            oxygen_rating = FILTERED[1]
            break
        }
    }
    printf and(oxygen_rating, 0xFFF)
}

# oxygen_rating = 010100101111 = 1327
# co2_rating    = 110101100101 = 3429
# 4550283
