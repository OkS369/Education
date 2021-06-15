#1
print(60*60)
#2
seconds_per_hour = 60 * 60
print(seconds_per_hour)
#3
print(24 * seconds_per_hour)
#4
seconds_per_day = 24 * seconds_per_hour
print(seconds_per_day)
#5
print(seconds_per_day / seconds_per_hour)
#6
print(seconds_per_day // seconds_per_hour)
#7
print(6 + 6)
print(15 - 3)
print(120 / 10)
print(1.2 * 10)
#8
x = 3
print('Your favorite number is', x)
#9
name = 'Roman Matviiv'
print(name)
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.swapcase())
#10
poem = '''Yes, I'll smile, indeed, through tears and weeping
... Sing my songs where evil holds its sway,
... Hopeless, a steadfast hope forever keeping,
... I shall live! You thoughts of grief, away!'''
print(poem[0:15])
print(len(poem))
print(poem.startswith('Yes'))
print(poem.endswith('I shall live!'))
print(poem.find(','))
print(poem.rfind(','))
print(poem.count(','))
print(poem.isalnum() or poem.isalnum())
