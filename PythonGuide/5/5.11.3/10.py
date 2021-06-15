things = {'key': 3, 'mace': 1, 'gold coin': 24, 'lantern': 1, 'stone': 10}
print('Equipment:')
for i in things.keys():
    print(things[i], i, sep = ' ')
print('Total number of things: ',sum(things.values()))

