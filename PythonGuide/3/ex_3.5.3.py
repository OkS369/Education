#1
text = 'Hello world'
print (text)
text = 'Goodbye world'
print (text)

#2
name = input ('What is your name?\n')
print (f"Hello, {name}, would you like to learn some Python today?\n")

#3
famous_person = 'Albert Enstein'
phrase = '"A person who never made a mistake never tried anything new."'
message = famous_person + 'once said, ' + phrase
print (message)

#4
name = '\n\tRoman\t\n'
print('1' + name)
print('2' + name.lstrip('\n'))
print('3' + name.rstrip('\n'))
print('4' + name.strip('\n'))

print('1' + name.strip('\n\t'))
print('2' + name.lstrip('\t'))
print('3' + name.rstrip('\t'))
print('4' + name.strip('\t'))

#5
name = 'Roman Matviiv'
country = 'Ukraine'
index = '79002'
city = 'Lviv'
street = 'Velychkovskoho street'
house = '8'
flat = '48'
adress = name + '\n' + country + '\n' + index + '\n' + city + '\n' + street + '\n' + house + '\n' + flat
print(adress)
#print(name, country, index, city, street, house, flat, sep='\n')

#6
m = float(input('Enter number of meters\n'))
inch = m * 39.37
foot = m * 3.2808
mile = m * 0.00054
yard = m * 1.0936
print('Your distance:\n\
meters - {0:.2f}\n\
inches - {1:.2f}\n\
foots  - {2:.2f}\n\
miles  - {3:.2f}\n\
yards  - {4:.2f}\n'.format(m, inch, foot, mile, yard))

#7
days = float(input('How many days are the holidays?\n'))
print('Days    - {0:<.3f}'.format(days))
print('Hours   - {0:<.3f}'.format(days * 24))
print('Minutes - {0:<.3f}'.format(days * 24 * 60))
print('Seconds - {0:<.3f}'.format(days * 24 *60 * 60))

#8
C = float(input('Temparetature in Celsius:\n'))
F = 32 + 9/5 * C
K = C + 273.15
print('Temperature'.center(60)					    + '\n' +\
'Celsius'.center(20)+ 'Fahrenheit'.center(20)+ 'Kelvin'.center(20)  + '\n' +\
'{0:^20.2f}{1:^20.2f}{2:^20.2f}'.format(C,F,K).center(60),sep='',end='\n\n\n')

print('|{0:^62s}|\n\
|{1:^20s}|{2:^20s}|{3:^20s}|\n\
|{4:^20.2f}|{5:^20.2f}|{6:^20.2f}|'\
.format('Temperature','Celsius','Fahrenheit','Kelvin',C,F,K,''),end='\n\n\n')

print(' {7:-^60}\n\
|{0:^62s}|\n\
 {7:-^60}\n\
|{1:^20s}|{2:^20s}|{3:^20s}|\n\
|{4:^20.2f}|{5:^20.2f}|{6:^20.2f}|'\
.format('Temperature','Celsius','Fahrenheit','Kelvin',C,F,K,''),end='\n\n\n')

#9
digits = input('Type some integer digit, please\n')
n = len(digits)-1
s = 0
for i in range(n):
    s += int(digits[i])
    print(digits[i], end = ' + ')
print(digits[n], end = ' = ')
s += int(digits[n])
print(s)

#10
import math
print('Визначаємо відстань між двома містами за їх координатами')
x1 = float(input('Введіть широту першого міста:\n'))
y1 = float(input('Введіть довготу першого міста:\n'))
x2 = float(input('Введіть широту другого міста:\n'))
y2 = float(input('Введіть довготу другого міста:\n'))
x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)
d = 6371.032 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1)* math.cos(x2)* math.cos(y1 - y2))
print('Відстань:  {0:.3f} км'.format(d))
