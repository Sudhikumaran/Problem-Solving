t = int(input())
for _ in range(t):

    row, col = map(int,input().split())

    matrix = []

    for i in range(row):
        rows = list(map(int,input().split()))
        matrix.append(rows)
    
    zero_rows = set()
    zero_cols = set()

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    for i in zero_rows:
        for j in range(col):
            matrix[i][j] = 0

    for j in zero_cols:
        for i in range(row):
            matrix[i][j] = 0
    
    for i in range(row):
        for j in range(col):
            print(matrix[i][j])