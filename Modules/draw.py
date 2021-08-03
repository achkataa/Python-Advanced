def draw_triange(n):
    for i in range(1, n + 1):
        row = []
        for j in range(1, i + 1):
            row.append(str(j))
        print(" ".join(row))
    for k in range(n - 1, 0, -1):
        row = []
        for j in range(1, k + 1):
            row.append(str(j))
        print(" ".join(row))
