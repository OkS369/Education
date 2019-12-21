s = int(input())
x, y, m, n, t = 0, 0, 0, s,1
r = [[0 for i in range(n)] for i in range(n)]
while (t <= s**2):
    for x in range(x,n):
        if t > s**2:            break
        r[y][x] = t
        t += 1
    y += 1
    for y in range(y,n):
        if t > s**2:            break
        r[y][x] = t
        t += 1
    x -= 1
    for x in range(x,m-1,-1):
        if t > s**2:            break
        r[y][x] = t
        t += 1
    y -= 1
    for y in range(y,m,-1):
        if t > s**2:            break
        r[y][x] = t
        t += 1
    x += 1
    n -= 1
    m += 1
for i in range(s):
    for j in range(s):
        # відступ - 1 пробіл між цифрами
        #print(r[i][j], end =' ')
        # відступ - линамічний (довжина максимального елемента +1 - довжину поточного елемента)
        print(r[i][j], end =(' '*(len(str(s**2))+1-len(str(r[i][j])))))
    print()

'''
Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
Sample Input: 
5
Sample Output: 
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
'''
