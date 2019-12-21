def modify_list(l):
    for i in range(len(l)-1, -1, -1):
        if (l[i] % 2) == 1:
            del l[i]    
    for i in range(len(l)-1, -1, -1):
        if (l[i] % 2) == 0:
            l.insert(i+1, l[i] // 2)
            del l[i]
        
             
lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

lst = [1, 2, 3, 3, 5, 4, 5, 7, 6]
modify_list(lst)
print(lst)               # [1, 2, 3]

lst = [8]
modify_list(lst)
print(lst)               # [4]

lst = [5]
modify_list(lst)
print(lst)               # []

lst = [1, 1, 4, 4]
modify_list(lst)
print(lst)               # [2, 2]


'''
def modify_list(l):
    c = 0
    for i in range(len(l)-1, -1, -1):
        if (l[i] % 2) == 1:
            l.insert(i+1, 0)
            c += 1
            l.remove(l[i])
    
    for i in range(len(l)-1, -1, -1):
        if (l[i] % 2) == 0:
            l.insert(i+1, l[i] // 2)
            l.remove(l[i])
            
    for i in range(c):
        l.remove(0)
'''

'''
def modify_list(l):
    for i in range(len(l)):
        if (l[i] % 2) == 0:
            l.insert(i+1, l[i] // 2)
            l.remove(l[i])
        elif (l[i] % 2) == 1:
            l.insert(i+1, 'z')
            l.remove(l[i])
    c = 0
    while ('z' in l):
        if l[c] == 'z':
            l.remove(l[c])
            c = 0
        c += 1
'''

'''
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения, а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка, например:

lst = [1, 2, 3, 4, 5, 6]
print(modify_list(lst))  # None
print(lst)               # [1, 2, 3]
modify_list(lst)
print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)               # [5, 4]

Функция не должна осуществлять ввод/вывод информации.
'''
