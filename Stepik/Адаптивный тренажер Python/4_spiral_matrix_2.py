def spiral(s, x=0, y=0, m=0, t=1):
    n = s
    while t <= s ** 2:
        for x in range(x, n):
            print(t, end=" ")
            t += 1
        y += 1
        for y in range(y, n):
            print(t, end=" ")
            t += 1
        x -= 1
        for x in range(x, m - 1, -1):
            print(t, end=" ")
            t += 1
        y -= 1
        for y in range(y, m, -1):
            print(t, end=" ")
            t += 1
        x += 1
        n -= 1
        m += 1


spiral(int(input()))
