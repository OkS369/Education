lst, x = [i for i in input().split()], input()
if x not in lst:
    print('Отсутствует')
else:
    for i in range(len(lst)):
        if lst[i]==x:
            print(i, end = ' ')

'''
lst, x, flag = [i for i in input().split()], input(), 0
for i in range(len(lst)):
    if lst[i]==x:
        print(i, end = ' ')
        flag = 1
if flag == 0:
    print('Отсутствует')
'''
'''
lst, x, flag, result = [i for i in input().split()], input(), 0, ''
for i in range(len(lst)):
    if lst[i]==x:
        result += str(i)+ ' '
        flag = 1
if flag == 0:
    print('Отсутствует')
else:
    print(result[:-1:])
'''

'''
Напишите программу, которая считывает список чисел 
lst
lst
из первой строки и число 
x
x
из второй строки, которая выводит все позиции, на которых встречается число 
x
x
в переданном списке 
lst
lst
.
Позиции нумеруются с нуля, если число 
x
x
не встречается в списке, вывести строку "Отсутствует" (без кавычек, с большой буквы).
Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
Sample Input 1: 
5 8 2 7 8 8 2 4
8
Sample Output 1: 
1 4 5
Sample Input 2: 
5 8 2 7 8 8 2 4
10
Sample Output 2: 
Отсутствует
'''
