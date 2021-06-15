transport = ['car','byke','airplane','trane','scooter','tram','trolleybus']
print('Transport:')
i = 0
for t in transport:
    print(f'{i} - {t}')
    i += 1
n = int(input('Which transport do you want?\n'))
print('I want buy', transport[n])
