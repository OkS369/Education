def multiplication():
    global x
    x = 1.0
    while (x != 0):
        print('Введіть число і ми його помножимо на попередньо введені')
        y = float(input('Ваше число:\n'))
        x = x * y
        print('Поточне значення:\n',x,sep='')
    return x

multiplication()
