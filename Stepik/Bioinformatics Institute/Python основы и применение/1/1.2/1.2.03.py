x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))

x = [1, 2, 3]
y = x
print(y is x)
print(y is [1, 2, 3])

x = [1, 2, 3]
y = x
print(y is x)
x.append(4)
print(x)
print(y)
