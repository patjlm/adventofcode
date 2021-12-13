BEGIN {

}

/[0-9]+,[0-9]+/ {
    DOTS[$0] = 1
}

function get_x(dot) {
    split(dot, a, ",")
    return a[1]
}
function get_y(dot) {
    split(dot, a, ",")
    return a[2]
}

/fold along / {
    split($3, instruction, "=")
    axe = instruction[1]
    idx = instruction[2]
    for (dot in DOTS) {
        x = get_x(dot)
        y = get_y(dot)
        if (axe == "x") {
            MAX_X = idx
            if (x > idx && x <= 2*idx) {
                new_x = 2 * idx - x
                DOTS[new_x","y] = 1
            }
        } else {
            MAX_Y = idx
            if (y > idx && y <= 2*idx) {
                new_y = 2 * idx - y
                DOTS[x","new_y] = 1
            }
        }
    }
}

END {
    OFS=""
    for (y=0; y<MAX_Y; y++) {
        for (x=0; x<MAX_X; x++) {
            printf (x","y in DOTS) ? "#" : " "
        }
        print ""
    }
}
