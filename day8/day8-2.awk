BEGIN {
    FS = "|"
}

# sorts the characters of an input string
function sorted(a) {
    split(a, arr, "")
    asort(arr)
    joined = ""
    for (i=1; i in arr; i++) {
        joined = joined "" arr[i]
    }
    return joined
}

# counts the number of common letters between the two input strings
function intersect(a, b) {
    matches = 0
    for (i = 1; i <= length(a); i++) {
        c = substr(a, i, 1)
        if (index(b, c)) {
            matches += 1
        }
    }
    return matches
}

# counts the number of letters/segments from 'a' which are not in 'b'
function diff(a, b) {
    return length(a) - intersect(a, b)
}

{
    # empty our previous array so we don't have garbage pattern->digit data
    split("", to_digit, ":")

    split($1, pattern, " ")

    # find patterns for 1, 7, 4 and 8
    for (pidx in pattern) {
        p = sorted(pattern[pidx])
        if (length(p) == 2) {
            to_digit[p] = 1
            to_pattern[1] = p
        } else if (length(p) == 3) {
            to_digit[p] = 7
        } else if (length(p) == 4) {
            to_digit[p] = 4
            to_pattern[4] = p
        } else if (length(p) == 7) {
            to_digit[p] = 8
        }
    }

    # find patterns for 9, 6, 0 which have 6 segments each
    for (pidx in pattern) {
        p = sorted(pattern[pidx])
        if (length(p) == 6) {
            if (intersect(p, to_pattern[4]) == 4) {         # 9 and 4 have 4 segments in common
                to_digit[p] = 9
                to_pattern[9] = p
            } else if (intersect(p, to_pattern[1]) == 1) {  # 6 and 1 have 1 segment in common
                to_digit[p] = 6
            } else {                                        # otherwise it's 0
                to_digit[p] = 0
            }
        }
    }

    # find patterns for 3, 5, 2 which have 5 segments each
    for (pidx in pattern) {
        p = sorted(pattern[pidx])
        if (length(p) == 5) {
            if (intersect(p, to_pattern[1]) == 2) {    # 3 and 1 have 2 segments in common
                to_digit[p] = 3
            } else if (diff(p, to_pattern[9]) == 0) {  # 5 and 9 differ only by 1 segment
                to_digit[p] = 5
            } else {                                   # otherwise it's 2
                to_digit[p] = 2
            }
        }
    }

    # compute output
    split($2, output, " ")
    for (idx in output) {
        p = sorted(output[idx])
        sum += to_digit[p] * 10^(4-idx)
    }
}

END {
    print sum
}
