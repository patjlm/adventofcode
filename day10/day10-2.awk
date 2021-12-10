BEGIN {
    CLOSING[")"] = "("; CLOSING["]"] = "["; CLOSING["}"] = "{"; CLOSING[">"] = "<"
    OPENING["("] = ")"; OPENING["["] = "]"; OPENING["{"] = "}"; OPENING["<"] = ">"
    POINTS[")"] = 1; POINTS["]"] = 2; POINTS["}"] = 3; POINTS[">"] = 4
    FS=""
    NB_SCORES = 0
}

/./ {
    nb_opened = 0
    for (i=1; i<=NF; i++) {
        if ($i in OPENING) opened[++nb_opened] = $i
        else if (opened[nb_opened--] != CLOSING[$i]) next
    }
    score = 0
    for (i=nb_opened; i>0; i--) {
        c = OPENING[opened[i]]
        score *= 5
        score += POINTS[c]
    }
    SCORES[++NB_SCORES] = score
}

function ceil(x, y) {
    y = int(x)
    return (x+0 > y ? y+1 : y)
}

END {
    asort(SCORES)
    print SCORES[ceil(length(SCORES)/2)]
}

# 2776842859
