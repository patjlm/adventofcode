BEGIN {
    FS=""
}

NR==1 {
    TEMPLATE=$0
    for (i=1; i<=NF; i++) {
        LETTERS[$i] += 1
        j=i+1
        if (j<=NF) PAIRS[$i$j] += 1
    }
    FS=" "
}

/ -> / {
    INSERT[$1] = $3
}

END {
    for (step=1; step<=40; step++) {
        # copy the PAIRS array to consider previous counts and avoid changing our list in place
        split("", OLD_PAIRS, ":")
        for (pair in PAIRS)
            OLD_PAIRS[pair] = PAIRS[pair]
        # perform splits and count new letters
        for (pair in OLD_PAIRS) {
            count = OLD_PAIRS[pair]
            ins = INSERT[pair]
            PAIRS[pair] -= count
            split(pair, arr, "")
            PAIRS[arr[1] ins] += count
            PAIRS[ins arr[2]] += count
            LETTERS[ins] += count
        }
    }

    min = -1
    max = -1
    for (l in LETTERS) {
        if (min == -1 || LETTERS[l] < min) min = LETTERS[l]
        if (max == -1 || LETTERS[l] > max) max = LETTERS[l]
    }
    print max - min
}

# 4110215602456
