import csv
Crimes_2015 = {}
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if '2015' in row[2]:
            if row[5] not in Crimes_2015.keys():
                Crimes_2015[row[5]] = 1
            else:
                Crimes_2015[row[5]] += 1
for i in Crimes_2015.keys():
    if Crimes_2015[i] == max(Crimes_2015.values()):
        print(i)


'''
Вам дана частичная выборка из датасета зафиксированных преступлений, 
совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
'''