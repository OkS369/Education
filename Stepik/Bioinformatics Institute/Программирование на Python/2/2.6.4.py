array = []                  
while (True):
    x = input()
    if (x) == 'end':  break
    row = x.split()
    for i in range(len(row)):
        row[i] = int(row[i])
    array.append(row)
n, m = len(array),len(array[0])           
for i in range(n):
    for j in range(m):
        print (array[i-1][j] + array[i-n+1][j] + array[i][j-1] + array[i][j-m+1], end = ' ')
    print()
        
#r = (array[i-1][j] + array[i-n+1][j] + array[i][j-1] + array[i][j-m+1])
#r = (array[(i-1)%n][j] + array[(i+1)%n][j] + array[i][(j-1)%m] + array[i][(j+1)%m])

'''
# input
array = []                  
while (True):
    x = input()
    if (x) == 'end':  break
    row = x.split()
    for i in range(len(row)):
        row[i] = int(row[i])
    array.append(row)
# calculate
result, n, m = [], len(array),len(array[0])              
for i in range(n):
    for j in range(m):
        result.append(array[i-1][j] + array[i-n+1][j] + array[i][j-1] + array[i][j-m+1])
        #result.append(array[(i-1)%n][j] + array[(i+1)%n][j] + array[i][(j-1)%m] + array[i][(j+1)%m])
# output
for i in range(n):          
    for j in range(m):
        print(result[j+i*m], end=' ')
    print()
'''

'''
Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
Sample Input 1: 
9 5 3
0 7 -1
-5 2 9
end
Sample Output 1: 
3 21 22
10 6 19
20 16 -1
Sample Input 2: 
1
end
Sample Output 2: 
4
'''
