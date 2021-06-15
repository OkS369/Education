Altai = {'type': 'dog', 'owner': 'Martin', 'name': 'Altai'}
Azyr = {'type': 'dog',  'owner': 'Martin', 'name': 'Azyr'}
Stormagedon = {'type': 'parrot', 'owner': 'Mirik', 'name': 'Stormagedon'}
Marsik = {'type': 'cat', 'owner': 'Nataly', 'name': 'Marsik'}

pets = [Altai, Azyr, Stormagedon, Marsik]
for x in pets:
    print(x['owner'], 'is the owner of a pet - a', x['type'], x['name'])
#for x in range(len(pets)):    print(pets[x]['owner'], 'is the owner of a pet - a', pets[x]['type'], pets[x]['name'])
