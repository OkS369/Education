hardware = ('SoC','CPU','RAM','GPU')
software = ['OS','File Manager','Store']
p = hardware, software
print (p)
print(hardware,software)
for h in hardware:
    print(h)
for s in software:
    print(s)
software [1] = 'Programs'
#hardware [0] = 'Hard'  #TypeEror
for h in hardware:
    print(h)
for s in software:
    print(s)
