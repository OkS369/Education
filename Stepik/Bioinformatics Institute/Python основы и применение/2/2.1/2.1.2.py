import sys
sys.stdin = open("2.1.2_input_3.txt", "r")


def founder(c, p):
    if p in parents[c]:
        return True
    if c == 'object':
        return False
    else:
        for i in parents[c]:
            if founder(i, p):
                return True
        return False
parents = {'object': ['']}
for i in range(int(input())):
    text = input()
    try:
        child, parent = text.split(' : ')[0], text.split(' : ')[1].split()
    except(ValueError, IndexError):
        child, parent = text, ''
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
for i in parents.keys():
    parents[i] = set(parents[i])
for i in parents.keys():
    parents[i] = sorted(list(parents[i]))
m = int(input())
exceptions, uniq_exceptions, result = [], [], []
order = {}
for i in range(m):
    exceptions.append(input().strip())
for i in range(len(exceptions)):
    if (exceptions[i] not in uniq_exceptions):
        uniq_exceptions.append(exceptions[i])
    elif (exceptions[i] not in uniq_exceptions) and (exceptions.count(exceptions[i]) > 1):
        uniq_exceptions.append(exceptions[i])
for i in range(len(uniq_exceptions)):
    for j in range(len(uniq_exceptions)):
        if (uniq_exceptions[i] in parents[uniq_exceptions[j]]) and (uniq_exceptions.index(uniq_exceptions[j]) > uniq_exceptions.index(uniq_exceptions[i])):
            result.append(uniq_exceptions[j])
        elif (uniq_exceptions[i] not in result) and (exceptions.count(uniq_exceptions[i]) > 1):
            result.append(uniq_exceptions[i])
        else:
            child, parent = uniq_exceptions[j], uniq_exceptions[i]
            if (founder(child, parent)) and (uniq_exceptions.index(uniq_exceptions[j]) > uniq_exceptions.index(uniq_exceptions[i])):
                result.append(uniq_exceptions[j])
for i in range(len(uniq_exceptions)):
    if uniq_exceptions[i] in result:
        print(uniq_exceptions[i])
'''
Вам дано описание наследования классов исключений в следующем формате. 
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.

try: foo() except <имя 1>: print("<имя 1>") except <имя 2>: print("<имя 2>") ... Костя посмотрел на этот код и указал 
Антону на то, что некоторые исключения можно не ловить, так как ранее в коде будет пойман их предок. Но Антон не 
помнит какие исключения наследуются от каких. Помогите ему выйти из неловкого положения и напишите программу, 
которая будет определять обработку каких исключений можно удалить из кода. Важное примечание: В отличие от предыдущей 
задачи, типы исключений не созданы. Создавать классы исключений также не требуется Мы просим вас промоделировать этот 
процесс, и понять какие из исключений можно и не ловить, потому что мы уже ранее где-то поймали их предка. 

Формат входных данных
В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, не изменив при этом поведение программы. Имена следует выводить в том же порядке, в котором они идут во входных данных.

Пример теста 1
Рассмотрим код

try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")


...


По условию этого теста, Костя посмотрел на этот код, и сказал Антону, что исключение FileNotFoundError можно не ловить, ведь мы уже ловим OSError -- предок FileNotFoundError
Sample Input:

4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError
Sample Output:

FileNotFoundError
'''