name=input('What is your name?\n')
age=input('How old are you?\n')
city=input('Where are you from?\n')
sex=input('Are you male or female?\n')
print('This is',name)
print('It is',age)
if (sex == 'Male'):
    print('He live in',city)
else:
    if (sex == 'Female'):
        print('She live in',city)
    else:
        print('It live in',city)

