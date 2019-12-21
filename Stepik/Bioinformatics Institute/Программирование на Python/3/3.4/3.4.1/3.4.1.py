numbers = []
letters = []
flag = 0
with open('dataset_3363_2.txt','r') as x:
    s = x.readline().strip()
    print(s)
    for i in range(len(s)):
        if  '0' <= str(s[i]) <= '9':
            if flag == 1:             
                numbers.append(int(str(numbers[-1]) + str(s[i])))
                del numbers[-2]
                continue
            flag = 1
            numbers.append(int(s[i]))
        else:
            flag = 0
            letters.append(str(s[i]))
print(letters, '\n', numbers, sep = '')       
with open('file2.txt','w') as y:
    for i in range(len(letters)):
        y.write(letters[i] * numbers[i])
        print(letters[i] * numbers[i], sep = '', end = '')

'''
На прошлой неделе мы сжимали строки, используя кодирование повторов. Теперь нашей задачей будет восстановление исходной строки обратно.
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.
Примечание. Это первое задание типа Dataset Quiz. В таких заданиях после нажатия "Start Quiz" у вас появляется ссылка "download your dataset". Используйте эту ссылку для того, чтобы загрузить файл со входными данными к себе на компьютер. Запустите вашу программу, используя этот файл в качестве входных данных. Выходной файл, который при этом у вас получится, надо отправить в качестве ответа на эту задачу. 

Sample Input: 
a3b4c2e10b1
Sample Output: 
aaabbbbcceeeeeeeeeeb
'''
