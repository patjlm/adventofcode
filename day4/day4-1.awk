BEGIN {
    board_id = 0
}

/([0-9]+,)+/ {
    split($0, numbers1, ",")
    for (i in numbers1) {
        numbers[numbers1[i]] = ""
    }
    next
}

/^$/ {
    row = 1
    board_id += 1
    next
}

/ / {
    split($0, inputs, " ")
    for (col in inputs) {
        nb = inputs[col]
        boards[board_id][nb] = row","col
        rows[board_id][row][nb] = col
        cols[board_id][col][nb] = row
        called[board_id][nb] = 0
    }
    row += 1
    next
}

END {
    for (i in numbers1) {
        nb = numbers1[i]
        for (b in boards) {
            if (nb in boards[b]) {
                called[b][nb] = 1
            }
            for (row in rows[b]) {
                all_called = 1
                for (n in rows[b][row]) {
                    if (called[b][n] == 0) {
                        all_called = 0
                    }
                }
                if (all_called == 1) {
                    sum = 0
                    for (i in boards[b]) {
                        if (!(called[b][i])) {
                            sum += i
                        }
                    }
                    print "sum "sum
                    print "nb "nb
                    print sum * nb
                    exit 0
                }
            }
            for (col in cols[b]) {
                all_called = 1
                for (n in cols[b][col]) {
                    if (called[b][n] == 0) {
                        all_called = 0
                    }
                }
                if (all_called == 1) {
                    for (i in rows[b]) {
                    }
                    sum = 0
                    for (i in boards[b]) {
                        if (!(called[b][i])) {
                            sum += i
                        }
                    }
                    print "sum "sum
                    print "nb "nb
                    print sum * nb
                    exit 0
                }
            }
        }
    }
}

# 28082
