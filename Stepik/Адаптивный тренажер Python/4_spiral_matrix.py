def spiral(s, x=0, y=0, m=0, t=1):
    n = s
    r = [[0 for i in range(s)] for j in range(s)]
    while t <= s ** 2:
        for x in range(x, n):
            r[y][x] = t
            t += 1
        y += 1
        for y in range(y, n):
            r[y][x] = t
            t += 1
        x -= 1
        for x in range(x, m - 1, -1):
            r[y][x] = t
            t += 1
        y -= 1
        for y in range(y, m, -1):
            r[y][x] = t
            t += 1
        x += 1
        n -= 1
        m += 1
    for y in range(s):
        print(' '.join(str(r[y][x]) for x in range(s)))


spiral(int(input()))
