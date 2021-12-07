BEGIN {
    RS = ","
    min = -1
    max = -1
}

/[0-9]+/ {
    if (min == -1 || $1 < min) min = $1
    if (max == -1 || $1 > max) max = $1
    count[$1] += 1
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
    min_fuel = -1
    target = -1
    for (i = min ; i <= max ; i++) {
        f = fuel(i)
        if (min_fuel == -1 || f < min_fuel) {
            target = i
            min_fuel = f
        }
    }
    print "fuel " min_fuel " for target position " target
}

# fuel 91638945 for target position 466
