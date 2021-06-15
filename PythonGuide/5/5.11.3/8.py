Lviv = {'country': 'Ukraine',
        'population': 'less than 1 million',
        'fact': 'Lviv is a cultures capital of Ukraine'}
London = {'country': 'UK',
        'population': '2 millions',
        'fact': ''}
New_York = {'country': 'USA',
        'population': '3 millions',
        'fact': 'New York is a city of abilities'}
cities = {
    'Lviv': Lviv,
    'London': London,
    'New York': New_York
    }
for i in cities.keys():
    print('\t', i, '\n', i, ' in ', cities[i]['country'],\
          '\nPopulations of ', i, ' is ', cities[i]['population'],\
          '\nFact about ', i, ' - ', cities[i]['fact'],'\n', sep = '')
