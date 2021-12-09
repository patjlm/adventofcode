BEGIN {
}

{
    rows += 1
    split($0, line, "")
    cols = length(line)
    for (col=1; col<=cols; col++) {
        points[rows][col] = line[col]
    }
}

function coord(r, c) {
    return r","c
}

# find adjacent points
function adjacents(row, col, adj) {
    split("", adj, ":")  # empty array
    if (row+0 > 1)    { adj[coord(row-1, col)] = "" }
    if (row+0 < rows) { adj[coord(row+1, col)] = "" }
    if (col+0 > 1)    { adj[coord(row, col-1)] = "" }
    if (col+0 < cols) { adj[coord(row, col+1)] = "" }
}

# discover recursively the basin points,
# setting basins[pt] and incrementing basin_points
function discover(basin_id, row, col, pt) {
    if (points[row][col] == 9) return;
    basins[pt] = basin_id
    basin_points[basin_id] += 1
    adjacents(row, col, adj)
    for (p in adj) {
        if (!(p in basins)) {
            split(p, rowcol, ",")
            discover(basin_id, rowcol[1], rowcol[2], p)
        }
    }
}

END {
    # discover all basins
    basin_id = 0
    for (row in points) {
        for (col in points[row]) {
            pt = coord(row, col)
            if (!(pt in basins)) {
                basin_id += 1
                discover(basin_id, row, col, pt)
            }
        }
    }

    # get the 3 largest basins
    for (b in basin_points) {
        value = basin_points[b]
        for (i=1; i<=3; i++) {
            if (max[i] == "" || max[i] < value) {
                tmp = max[i]
                max[i] = value
                value = tmp
            } else break
        }
    }
    print max[1] * max[2] * max[3]
}

# 1142757
