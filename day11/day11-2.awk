BEGIN {
    FS=""
    rows = 0
}

{
    rows += 1
    cols = NF
    for (i=1; i<=NF; i++) {
        MATRIX[rows][i] = $i
    }
}

function flash(row, col) {
    if (flashed[row][col] == 1) return
    flashed[row][col] = 1

    from_row = row==1 ? 1 : row-1
    to_row = row==rows ? rows : row+1
    from_col = col==1 ? 1 : col-1
    to_col = col==cols ? cols : col+1
    for (r=from_row; r<=to_row; r++) {
        for (c=from_col; c<=to_col; c++) {
            if (r != row || c != col) {
                MATRIX[r][c] += 1
                if (MATRIX[r][c] > 9) {
                    flash(r, c)
                }
            }
        }
    }
}

END {
    step = 0
    while (1) {
        step += 1
        flashes = 0
        split("", flashed, ":")
        for (row=1; row<=cols; row++) {
            for (col=1; col<=cols; col++) {
                MATRIX[row][col] += 1
            }
        }
        for (row=1; row<=cols; row++) {
            for (col=1; col<=cols; col++) {
                if (MATRIX[row][col] > 9) {
                    flash(row, col)
                }
            }
        }
        for (row=1; row<=cols; row++) {
            for (col=1; col<=cols; col++) {
                if (MATRIX[row][col] > 9) {
                    MATRIX[row][col] = 0
                    flashed[row][col] = 0
                    flashes += 1
                }
            }
        }
        print step " -> " flashes
        if (flashes == 100 || step > 383) break
    }
    print step
}
