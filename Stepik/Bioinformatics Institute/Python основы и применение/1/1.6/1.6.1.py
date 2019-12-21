# import sys
# sys.stdin = open("1.6.1_input_1.txt", "r")
# sys.stdin = open("1.6.1_input_2.txt", "r")
# sys.stdin = open("1.6.1_input_3.txt", "r")


def print_dic(ancestors):
    print()
    for i in ancestors.keys():
        print(i, '\n', ancestors[i])
    print()


def founder(c, p):
    if p in parents[c]:
        return True
    if c == 'object':
        return False
    else:
        for next_parent in parents[c]:
            if founder(next_parent, p):
                return True
        return False



parents = {'object': ['']}
for i in range(int(input())):
    text = input()
    try:
        child, parent = text.split(' : ')[0], text.split(' : ')[1].split()
        #print('child:\t', child, '\n', 'parent:\t', parent, sep='')
    except(ValueError, IndexError):
        child, parent = text, ''
        #print(child, parent)
    if child not in parents.keys():
        parents[child] = ['object']
    for i in parent:
        if i not in parents.keys():
            parents[i] = ['object']
        if child not in parents.keys():
            parents[child] = parent
        elif child == parent:
            parents[child].append(parent)
        else:
            parents[child].extend(parent)

# print_dic(parents)
for i in parents.keys():
    parents[i] = set(parents[i])
for i in parents.keys():
    parents[i] = sorted(list(parents[i]))
# print_dic(parents)

for i in range(int(input())):
    parent, child = input().split()
    if child == parent:
        print('Yes')
    elif parent in parents[child]:
        print('Yes')
    else:
        if founder(child, parent):
            print('Yes')
        else:
            print('No')

'''
Вам дано описание наследования классов в следующем формате. 
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass

Класс A является прямым предком класса B, если B отнаследован от A:

class B(A):
    pass


Класс A является предком класса B, если 

A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.
В следующих n строках содержится описание наследования классов. 
В i-й строке указано от каких классов наследуется i-й класс. 
Обратите внимание, что класс может ни от кого не наследоваться. 
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
что класс не наследуется явно от одного класса более одного раза.
В следующей строке содержится число q - количество запросов.
В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", 
если класс 1 является предком класса 2, и "No", если не является. 


Sample Input: 
4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output: 
Yes
Yes
Yes
No
'''
