total = 25
 
while total > 0:
    print('Залишилось учасників:   ',total)
    n = int(input('Введіть кількість убитих вами:\n'))
    total = total - n
    if  (total < 0):
        print('Недопустима операція')
        total = total + n
        break
 
print("Ресурс вичерпано")
exit()
