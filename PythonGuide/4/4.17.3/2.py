input_numbers = input('Type some numbers:\n(separate with space)\n')
input_numbers = input_numbers.split(' ')
numbers= []
for i in input_numbers:
    numbers.append(int(i))
print(f'You input {len(input_numbers)} numbers. Their sum is {sum(numbers)}')
