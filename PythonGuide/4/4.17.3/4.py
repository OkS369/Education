l = [int(i) for i in input('Type some naubers (separate with space):\n').split()]
r = l[::-1]
print('List of your numbers:', l, 'Reversed list of your numbers:', r,\
      'Sum of this nubers:', sum(r), 'Concatenate this numbers in one string:', sep = '\n')
for i in l:
    print(i, end = '')
print()
for i in r:
    print(i, end = '')

'''
input_numbers = input('Type some numbers:\n(separate with space)\n')
input_numbers = input_numbers.split(' ')
numbers = []
for i in input_numbers:
    numbers.append(int(i))
numbers_reversed  = numbers.copy()
numbers_reversed.sort(reverse=True)
print(f'You input {len(input_numbers)} numbers. Here them {numbers_reversed} Their sum is {sum(numbers_reversed)}')
'''

