import os.path
with open('main_ans.txt', 'w') as m_ans:
    ans = []
    for current_dir, dirs, files in os.walk('main'):
        if any([file[-3:] == '.py' for file in files]) and (str(current_dir) not in ans):
            ans.append(current_dir)
    ans.sort()
    m_ans.write('\n'.join(ans))


'''
Вам дана в архиве (main) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, 
и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py". 

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.

Для лучшего понимания формата задачи, ознакомьтесь с примером.
'''