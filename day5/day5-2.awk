function sign(v) {
    return v < 0 ? -1 : 1
}

BEGIN {
    pattern = "([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"
}

{
    x1 = gensub(pattern, "\\1", "g")
    y1 = gensub(pattern, "\\2", "g")
    x2 = gensub(pattern, "\\3", "g")
    y2 = gensub(pattern, "\\4", "g")
    stepx = x1 == x2 ? 0 : sign(x2-x1)
    stepy = y1 == y2 ? 0 : sign(y2-y1)
    x = x1
    y = y1
    for (; x != x2 || y != y2;) {
        POINT[x","y] += 1
        x += stepx
        y += stepy
    }
    POINT[x2","y2] += 1
}

END {
    SUM = 0
    for (p in POINT) {
        if (POINT[p] >= 2) {
            SUM += 1
        }
    }
    print SUM
}

# 17882
