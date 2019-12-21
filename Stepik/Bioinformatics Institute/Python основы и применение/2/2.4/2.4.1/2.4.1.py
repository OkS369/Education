with open("dataset_24465_4.txt", "r") as f1, open('file2.txt', 'w') as f2:
    lines = []
    for line in f1:
        lines.append(line.strip())
    lines.reverse()
    lines = '\n'.join(lines)
    f2.write(lines)
'''
with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
    fw.writelines(fr.readlines()[::-1])
'''

'''Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab'''