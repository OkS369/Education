

def test():
    number=input('Введіть ціле число:\n')
    while type(number) != int:
        try:
            number=int(number)
        except ValueError:
            print('Помилка введення\n')
            number=input('Введіть  ЦІЛЕ число\n(0,1,2,3...10,100...)\n')
    if (number < 0):
        negative()
    elif (number > 0):
        positive()
    elif (number == 0):
        print('І додатній і від\'ємний наш нуль. Чи ні?\nЗапитайте у знайомого математика\n')
    else:
        print('Помилка введення')
def positive():
    print('Додатнє\n')

def negative():
    print('Від\'ємне\n')    


while (True):
    test()
