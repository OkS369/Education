s, x = 0, 1
while x != 0:
    x = int(input())
    s += x
print(s)

x, s = 1, 0
while x != 0:
    x, s = int(input()), s + x
print(s)

'''
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
Sample Input 1: 
5
-3
8
4
0
Sample Output 1: 
14
Sample Input 2: 
0
Sample Output 2: 
0
'''
