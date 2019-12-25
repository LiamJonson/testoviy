n, m = map(int, input().split())
p = [[i for i in input()] for _ in range(n)]
k = [[0 for i in range(m)] for j in range(n)]
for i in range(0, n):
    for j in range(0, m):
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if i + di < n and i + di > -1 and j + dj < m and j + dj > -1:
                    if p[i + di][j + dj] == '*' and p[i][j] != '*':
                        k[i][j] += 1
                    elif p[i][j] == '*':
                        k[i][j] = '*'
for i in k:
    print(*i, sep='')
