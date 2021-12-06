{
    split($0, inputs, ",")
    for (i in inputs) {
        count[inputs[i]] += 1
    }
}
END {
    for (day=0; day<256; day++) {
        spawned = count[0]
        for (i=0; i<6; i++) {
            count[i] = count[i+1]
        }
        count[6] = count[7] + spawned
        count[7] = count[8]
        count[8] = spawned
    }
    sum = 0
    for (i in count) {
        sum += count[i]
    }
    print sum
}

# 1738377086345
