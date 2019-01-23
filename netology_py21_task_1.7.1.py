def polish_notation():
    user_input = input('Введите выражение: ')
    expression = user_input.split(' ')

    if float(expression[1]) > 0 and float(expression[2]) > 0:
        if expression[0] == '+':
            print('Ответ:', float(expression[1]) + float(expression[2]))
        elif expression[0] == '-':
            print('Ответ:', float(expression[1]) - float(expression[2]))
        elif expression[0] == '*':
            print('Ответ:', float(expression[1]) * float(expression[2]))
        elif expression[0] == '/':
            print('Ответ:', float(expression[1]) / float(expression[2]))
    else:
        print('Программа работает только для положительных чисел.')


polish_notation()
