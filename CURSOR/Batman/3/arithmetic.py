print('Hi, guys! \nCan you answer for these?\nx=4*100-54')
rightanswer=4*100-54
answer=int(input('What is yuor answer?\n'))
print('Now check your answer...\nOne moment...')
print('Your answer is',answer)
print('Right snwer is',rightanswer)
if (answer == rightanswer):
    print('You are cool!')
else:
        print('Another time, friend')
        
print('...\n...\nAre you try another arithmetic?')
a=float(input('Write the number a\n'))
b=float(input('Write the number b\n'))
c=float(input('Write the number c\n'))
d=float(input('Write the number d\n'))
rightanswer=(a+b)/(c+d)
answer=float(input('Now, tell me answer x=(a+b)/(c+d)\n'))
print('Now check your answer...\nOne moment...')
print('Your answer is %.2f'%(answer))
print('Right snwer is %.2f'%(rightanswer))
if (answer == rightanswer):
    print('You are cool!')
else:
        print('Another time, friend')
