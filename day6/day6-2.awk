BEGIN {
    RS = ","
}
{
    count[$1] += 1
}
END {
    for (day=0; day<256; day++) {
        spawned = count[0]
        for (i=0; i<8; i++) {
            count[i] = count[i+1]
        }
        count[6] += spawned  # parents reset (previous count[0])
        count[8] = spawned  # new borns
    }
    sum = 0
    for (i in count) {
        sum += count[i]
    }
    print sum
}

# 1738377086345
