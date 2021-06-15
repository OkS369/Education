print('Порахуємо, у якому році вам було Х років')
while True:
    born_year = int(input('Коли ви народились?\n'))
    now_age = int(input('Скільки вам зараз років?\n'))
    years_list = []
    answer = 1
    while answer == 1:
        for i in range(now_age+1):
            years_list.append (born_year + i)
        age = int(input('Який вік вас цікавить?\n'))
        try:
            year = years_list [age]
            print(f'Вам було {age} у {year}')
            answer = int(input('Ввести інший вік - "1"\nПочати з початку - усе окрім "1"\n')) 
        except (IndexError):
            print('Вам ще стільки не було, але уявиимо, що є і порахуємо')
            years_list = []
            for i in range(age+1):
                years_list.append (born_year + i)
            year = years_list [age]
            print(f'Вам було {age} у {year}')
            answer = int(input('Ввести інший вік - "1"\nПочати з початку - усе окрім "1"\n')) 
