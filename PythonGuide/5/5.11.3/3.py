languages_programmers = {
    'JavaSript': 'Brendan Eich',
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    'Scala': 'Martin Odersky',
    'C': 'Dennis Ritchie'
    }

for i in languages_programmers.keys():
    print('My favorite programming language is ',i,'.\
It was created by ',languages_programmers[i],'.', sep = '')
    
del  languages_programmers['Scala']
print(languages_programmers)
