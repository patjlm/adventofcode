BEGIN {
    count = 0
    previous = -1
}

/[0-9]+/ {
    if (previous > 0) {
        if ($1 > previous) {
            count += 1
        }
    }
    previous = $1
    next
}
{
    print "invalid input: "$0
}

END {
    print "count: "count
}
