BEGIN {
    FS = "|"
}

function sorted(a) {
    split(a, arr, "")
    asort(arr)
    joined = ""
    for (i=1; i in arr; i++) {
        joined = joined "" arr[i]
    }
    return joined
}

function inter(a, b) {
    lena = length(a)
    matches = 0
    for (i = 1; i <= lena; i++) {
        c = substr(a, i, 1)
        if (index(b, c)) {
            matches += 1
        }
    }
    return matches
}

function diff(a, b) {
    lena = length(a)
    matches = lena
    for (i = 1; i <= lena; i++) {
        c = substr(a, i, 1)
        if (index(b, c)) {
            matches -= 1
        }
    }
    return matches
}

{
    split($1, pattern, " ")
    # empty arrays
    split("", to_digit, ":")
    split("", to_pattern, ":")
    for (pidx in pattern) {
        p = sorted(pattern[pidx])
        if (length(p) == 2) {
            to_digit[p] = 1
            to_pattern[1] = p
        } else if (length(p) == 3) {
            to_digit[p] = 7
            # to_pattern[7] = p
        } else if (length(p) == 4) {
            to_digit[p] = 4
            to_pattern[4] = p
        } else if (length(p) == 7) {
            to_digit[p] = 8
            # to_pattern[8] = p
        }
    }

    for (pidx in pattern) {
        p = sorted(pattern[pidx])
        if (length(p) == 6) {
            if (inter(p, to_pattern[4]) == 4) {
                to_digit[p] = 9
                to_pattern[9] = p
            } else if (inter(p, to_pattern[1]) == 1) {
                to_digit[p] = 6
                # to_pattern[6] = p
            } else {
                to_digit[p] = 0
                # to_pattern[0] = p
            }
        }
    }

    for (pidx in pattern) {
        p = sorted(pattern[pidx])
        if (length(p) == 5) {
            if (inter(p, to_pattern[1]) == 2) {
                to_digit[p] = 3
                # to_pattern[3] = p
            } else if (diff(p, to_pattern[9]) == 0) {
                to_digit[p] = 5
                # to_pattern[5] = p
            } else {
                to_digit[p] = 2
                # to_pattern[2] = p
            }
        }
    }

    split($2, output, " ")
    for (idx in output) {
        p = sorted(output[idx])
        sum += to_digit[p] * 10^(4-idx)
    }
}

END {
    print sum
}
