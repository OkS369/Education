def getNum(n, x, y):
    x = 2 * x - n + 1
    y = 2 * y - n + 1
    m = max(abs(x), abs(y))
    p = (x + y) / 2
    if x < y: p = 2 * m - p
    return int(n * n - m * m - m + p)


n = int(input())
# for y in range(n):  print(" ".join(map(str,[getNum(n,x,y) for x in range(n)])))
for y in range(n):  print(*[getNum(n,x,y) for x in range(n)])