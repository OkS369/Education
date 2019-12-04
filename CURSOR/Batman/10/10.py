def cylinder():
    def circle():
        return float(2 * 3.14 * r)
    answer = input('Зараз ми обчислимо площу циліндра.\n\
Хочете отримати тільки площу бокової поверхні циліндру чи повну площу циліндра?\n\
1- повна площа, 2 - площа бокової поверхні, 3 - піти поспати.\n')   
    if (answer == '1'):
        r = float(input('Введіть значення радіуса основи циліндра\n'))
        h = float(input('Введіть значення висоти циліндра\n'))
        circle()
        side = 2 * 3.14 * r * h
        square = side + 2 * circle()
    elif (answer == '2'):
        r = float(input('Введіть значення радіуса основи циліндра\n'))
        h = float(input('Введіть значення висоти циліндра\n'))
        side = 2 * 3.14 * r * h
        square = side
    else:
        print('Давно пора!')
        exit()
    print('Площа: %.2f' % square)

cylinder()
