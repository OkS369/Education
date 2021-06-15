e2g = {
    'stork': 'storch',
    'hawk': 'falke',
    'woodpecker': 'specht',
    'owl': 'eule',
    'goose': 'gans',
    'raven': 'rabe'
    }
print(e2g)
print(e2g['owl'])
for i in e2g.keys():
    print(i, ' - ',e2g[i], sep = '')
    
print(list(e2g.items()))
print(list(e2g.keys()))
print(list(e2g.values()))

