BEGIN {
    board_id = 0
}

/([0-9]+,)+/ {
    split($0, numbers1, ",")
    # for (i in numbers1) {
    #     numbers[numbers1[i]] = ""
    # }
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

function win(rows_or_cols, b) {
    for (i in rows_or_cols[b]) {
        all_called = 1
        for (n in rows_or_cols[b][i]) {
            if (! called[b][n]) {
                all_called = 0
            }
        }
        if (all_called) {
            return 1
        }
    }
    return 0
}

function result(b) {
    sum = 0
    for (i in boards[b]) {
        if (!(called[b][i])) {
            sum += i
        }
    }
    print "sum "sum
    print "nb "nb
    print sum * nb
}

END {
    for (i in numbers1) {
        nb = numbers1[i]
        for (b in boards) {
            if (nb in boards[b]) {
                called[b][nb] = 1
            }
            if (win(rows, b) || win(cols, b)) {
                result(b)
                exit 0
            }
        }
    }
}

# 28082
