def counter(results, name, goals, missed, t):
    if goals > missed:
        t[0] += 1
        t[1] += 1
        t[4] += 3
        results[name] = t
    elif goals < missed:
        t[0] += 1
        t[3] += 1
        results[name] = t
    elif goals == missed:
        t[0] += 1
        t[2] += 1
        t[4] += 1
        results[name] = t
        
def count_for_team(results, name, goals, missed):
    t = [0, 0, 0, 0, 0]
    if name not in results.keys():
        counter(results, name, goals, missed, t)
    elif name in results.keys():
        t = results[name]
        counter(results, name, goals, missed, t)

n = int(input())
results = {}
#   Всего_игр  Побед   Ничьих  Поражений   Всего_очков
#   t[0]        t[1]    t[2]    t[3]        t[4]
for i in range(n):
    m = input().split(';')
    count_for_team(results, m[0], m[1], m[3])
    count_for_team(results, m[2], m[3], m[1])        

for i in results.keys():
    print(i,':', sep = '', end = '')
    print(*results[i])

'''
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число 
n
n
— количество завершенных игр.
После этого идет 
n
n
строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.
Sample Input: 
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2
Sample Output: 
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
'''
