def f(x):
    if x <= -2:
        res = 1 - ((x + 2) * (x + 2))
        return res
    elif -2 < x <= 2:
        res = -(x / 2)
        return res
    elif 2< x:
        res = ((x - 2) * (x - 2)) + 1
        return res

print(f(float(input())))

'''
Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

f(x)=
1−(x+2)2,   при x≤−2
−(x/2),     при −2<x≤2
(x−2)2+1,   при 2<x

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

Sample Input 1: 
4.5
Sample Output 1: 
7.25
Sample Input 2: 
-4.5
Sample Output 2: 
-5.25
Sample Input 3: 
1
Sample Output 3: 
-0.5
'''
