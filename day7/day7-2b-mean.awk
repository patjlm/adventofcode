BEGIN {
    RS = ","
    min = -1
    max = -1
}

/[0-9]+/ {
    # if (min == -1 || $1 < min) min = $1
    # if (max == -1 || $1 > max) max = $1
    count[$1] += 1
    sum += $1+0
    total += 1
}

function floor(x, y) {
    y = int(x)
    return (x < y ? y-1 : y)
}

function ceil(x, y) {
    y = int(x)
    return (x+0 > y ? y+1 : y)
}

function fuel(target) {
    f = 0
    for (pos in count) {
        n = (pos+0 >= target) ? (pos - target) : (target - pos)
        f += (count[pos] * n * (n + 1) / 2) + 0
    }
    return f
}

END {
    f1 = fuel(floor(sum / total))
    f2 = fuel(ceil(sum / total))
    f = f1 < f2 ? f1 : f2
    print "fuel " f " for target position " (sum / total)
}

# fuel 91638945 for target position 466
