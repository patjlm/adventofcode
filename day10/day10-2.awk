BEGIN {
    CLOSING[")"] = "("; CLOSING["]"] = "["; CLOSING["}"] = "{"; CLOSING[">"] = "<"
    OPENING["("] = ")"; OPENING["["] = "]"; OPENING["{"] = "}"; OPENING["<"] = ">"
    POINTS[")"] = 1; POINTS["]"] = 2; POINTS["}"] = 3; POINTS[">"] = 4
    FS=""
    NB_SCORES = 0
}

/./ {
    nb_opened = 0
    print $0
    for (i=1; i<=NR; i++) {
        printf "char " $i ": "
        incomplete = 1
        if ($i in OPENING) {
            opened[++nb_opened] = $i
            print "  opened(" nb_opened ") : " $i
        }
        else {
            if (opened[nb_opened] != CLOSING[$i]) {
                incomplete = 0
                break
            }
            print $i " --> pop "opened[nb_opened]
            nb_opened--
        }
    }
    if (incomplete) {
        printf " --> "
        score = 0
        for (i=nb_opened; i>0; i--) {
            c = OPENING[opened[i]]
            printf c
            score *= 5
            score += POINTS[c]
        }
        print ""
        SCORES[++NB_SCORES] = score
    }
}

END {
    for (score in SCORES) printf SCORES[score] ", "
    print ""
}
