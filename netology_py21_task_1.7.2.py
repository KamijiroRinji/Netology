def polish_notation():
    user_input = input('Enter your expression: ')
    expression = user_input.split(' ')

    try:
        expression[1] = float(expression[1])
    except IndexError:
        print(
            "IndexError: Less args than expected. Please, enter operation and 2 numbers separating them with spaces, e.g. + 2 2")
        exit()
    except ValueError:
        pass

    try:
        expression[2] = float(expression[2])
    except IndexError:
        print(
            "IndexError: Less args than expected. Please, enter operation and 2 numbers separating them with spaces, e.g. + 2 2")
        exit()
    except ValueError:
        pass

    assert expression[0] in ['+', '-', '*', '/'], 'Unsupported operation'

    if expression[0] == '+':
        try:
            print('Ответ:', float(expression[1]) + float(expression[2]))
        except ValueError:
            print('Ответ:', str(expression[1]) + str(expression[2]))
    elif expression[0] == '-':
        try:
            print('Ответ:', float(expression[1]) - float(expression[2]))
        except ValueError:
            print("ValueError: Can't subtract strings!")
    elif expression[0] == '*':
        try:
            print('Ответ:', float(expression[1]) * float(expression[2]))
        except ValueError:
            try:
                expression[1] = int(expression[1])
            except ValueError:
                pass
            try:
                expression[2] = int(expression[2])
            except ValueError:
                pass
            if (type(expression[1]) == int and type(expression[2]) == str) or (
                    type(expression[2]) == int and type(expression[1]) == str):
                print('Ответ:', expression[1] * expression[2])
            else:
                print("ValueError: Can't multiply strings")
    elif expression[0] == '/':
        try:
            print('Ответ:', float(expression[1]) / float(expression[2]))
        except ZeroDivisionError:
            print("ZeroDivisionError: Can't divide by zero!")
        except ValueError:
            print("ValueError: Can't divide by a string!")
    else:
        print('Oopsie, unknown error!')

polish_notation()
