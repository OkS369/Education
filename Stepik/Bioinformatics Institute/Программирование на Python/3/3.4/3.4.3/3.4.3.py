first = []
second = []
third = []
n = 0
with open('dataset_3363_4.txt','r') as x:
    for i in x:
        si = i.strip().split(';')
        first.append(float(si[1]))
        second.append(float(si[2]))
        third.append(float(si[3]))
        n += 1
        #print(si)
        print((float(si[1]) + float(si[2]) + float(si[3]))/3,sep ='\n')
    print(sum(first)/n, sum(second)/n, sum(third)/n)
    

'''
Имеется файл с данными по успеваемости абитуриентов. Он представляет из себя набор строк, где в каждой строке записана следующая информация:
Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
Поля внутри строки разделены точкой с запятой, оценки — целые числа.
Напишите программу, которая считывает файл с подобной структурой и для каждого абитуриента выводит его среднюю оценку по этим трём предметам на отдельной строке, соответствующей этому абитуриенту.
Также в конце файла, на отдельной строке, через пробел запишите средние баллы по математике, физике и русскому языку по всем абитуриентам:

Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом: 

print('First;Second-1 Second-2;Third'.split(';'))
# ['First', 'Second-1 Second-2', 'Third']

Sample Input: 
Петров;85;92;78
Сидоров;100;88;94
Иванов;58;72;85
Sample Output: 
85.0
94.0
71.666666667
81.0 84.0 85.666666667
'''
