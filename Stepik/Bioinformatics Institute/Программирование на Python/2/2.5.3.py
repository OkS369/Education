'''
x = [int(i) for i in input().split()]
y = []
y1 = []
x.sort()
t = x [0]
n = 0
for i in x:
    if t == i:
        n += 1
    else:
        y.append(t)
        y1.append(n)
        t = i
        n = 1
y.append(t)
y1.append(n)
for o in range(len(y)):
    if y1[o] > 1:
        print(y[o], end =' ')
'''


ls = [int(i) for i in input().split()]
for i in set(ls):
    if ls.count(i) > 1:
        print(i, end=' ')


'''
x = input().split()
print (x)
print (*(i for i in set(x) if x.count(i) > 1))
'''

'''
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
Sample Input 1: 
4 8 0 3 4 2 0 3
Sample Output 1: 
0 3 4
Sample Input 2: 
10
Sample Output 2: 

Sample Input 3: 
1 1 2 2 3 3
Sample Output 3: 
1 2 3
Sample Input 4: 
1 1 1 1 1 2 2 2
Sample Output 4: 
1 2
'''
