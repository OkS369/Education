cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kiev', 'Hong Kong']
menu = ['Me',"You",'He','She','Them']

def list_and(l):
    n = len(l) - 1
    for i in range(n - 1):
        print(l[i], end = ', ')
    print(f'{l[n -1]} and {l[n]}')

list_and(cities)
cities.sort()
list_and(cities)

list_and(menu)
