n = int(input())
A = [[0]*n for i in range(n)]
x, y, dx, dy = 0, 0, 0, 1
for i in range(n*n):
    A[x][y] = i + 1
    if A[(x + dx) % n][(y + dy) % n]:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy
for line in A: print(*line)