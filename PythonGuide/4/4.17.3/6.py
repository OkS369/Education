text_of_code = '''for each token in the postfix expression : if the token is a number : print('Convert it to an integer and add it to the end of values') else : print('Append the result to the end of values')'''
keywords = ('for', 'if', 'else', 'in', ':')
text = [i for i in text_of_code.split()]
print(text)
code = ''
level = 0
flag = 0
for i in text:
    if i == keywords[0]:
        code += i
        code += ' '
        flag = 1
        continue
    elif i == keywords[1]:
        code += i
        code += ' '
        flag = 1
        continue
    elif i == keywords[2]:
        code += '\n'
        level -= 1
        code += '\t' * level
        code += i
        code += ' '
        flag = 1
        continue
    elif i == keywords[4]:
        code += i
        code += '\n'
        if flag == 1:
            level += 1
        code += '\t' * level
        continue
    else:
        code += i
        code += ' '
print(code)
