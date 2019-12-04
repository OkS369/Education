try:
    old = int(input('Ваш вік: '))
    print('Рекомендовано:', end=' ')

except ValueError:
    print('Введіть ціле число!')
    old = int(input('Ваш вік: '))
     
if 3 <= old < 6:
    print('"Важко, але я зможу"')   
elif 6 <= old < 12:
    print('"Хочу одружитись на Мерлін Монро"')
elif 12 <= old < 16:
    print('"Я люблю Леонардо Ді Капріо"')
elif 16 <= old:
    print('"я люблю CURSOR "')
else:
    print('Треба підрости')




