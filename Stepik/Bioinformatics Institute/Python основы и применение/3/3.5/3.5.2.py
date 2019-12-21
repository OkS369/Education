import json


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


data = json.loads(input().strip())
ans = {'object': 0}
parents = {'object': ['']}
for clss in data:
    if clss['name'] not in parents.keys():
        parents[clss['name']] = clss['parents']
    if clss['name'] not in ans.keys():
        ans[clss['name']] = 0
for i in parents.keys():
    for j in parents.keys():
        parent, child = i, j
        if child == parent:
            ans[i] += 1
        elif parent in parents[child]:
            ans[i] += 1
        else:
            if founder(child, parent):
                ans[i] += 1
for i in sorted(ans.keys()):
    if i == 'object': continue
    print(i, ':', ans[i])


'''
Вам дано описание наследования классов в формате JSON. 
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. 
У каждого JSON-объекта есть поле name, которое содержит имя класса, 
и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, 
и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
'''