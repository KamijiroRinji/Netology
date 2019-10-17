def line_breaker(line, length):
    """Breaks the line by maximum length and joins back to one string.

    Arguments
    _________
        line : str, required
            The line to break into smaller pieces by maximum length
        length : int, required
            The maximum length the line should be broken by

    Returns
    _______
        line : str
            The line broken by maximum length
    """
    try:
        if len(str(line)) > int(length):
            line_list = \
                [line[i: i + int(length)] + '\n' for i in range(0, len(line), int(length))]
            line = ''.join(line_list)
    except ValueError:
        print('The maximum length should be an integer. Please restart the program and provide a valid value.')
    return line


def print_decorator(old_function):
    """Decorator to alter standard "print".

    Keyword arguments
    _________________
        start : str, optional
            The starting line to add to the beginning (default '' - empty string)
        max_line : int, optional
            The maximum length the line should be broken by
        in_file : bool
            The option to write output to a file - write if True
    """
    def new_function(*args, **kwargs):
        if 'in_file' in kwargs.keys():
            if kwargs['in_file']:
                file_name = input('Введите имя файла:\n')
                with open(file_name, 'a') as file:
                    if 'start' in kwargs.keys() and 'max_line' in kwargs.keys():
                        new_line = kwargs['start'] + ''.join(args)
                        file.write(line_breaker(new_line, kwargs['max_line']))
                        return old_function(line_breaker(new_line, kwargs['max_line']))
                    elif 'start' in kwargs.keys() and 'max_line' not in kwargs.keys():
                        new_line = kwargs['start'] + ''.join(args)
                        file.write(new_line)
                        return old_function(new_line)
                    elif 'start' not in kwargs.keys() and 'max_line' in kwargs.keys():
                        new_line = '' + ''.join(args)
                        file.write(line_breaker(new_line, kwargs['max_line']))
                        return old_function(line_breaker(new_line, kwargs['max_line']))
                    else:
                        new_line = '' + ''.join(args)
                        file.write(new_line)
                        return old_function(new_line)
            elif not kwargs['in_file']:
                if 'start' in kwargs.keys() and 'max_line' in kwargs.keys():
                    new_line = kwargs['start'] + ''.join(args)
                    return old_function(line_breaker(new_line, kwargs['max_line']))
                elif 'start' in kwargs.keys() and 'max_line' not in kwargs.keys():
                    new_line = kwargs['start'] + ''.join(args)
                    return old_function(new_line)
                elif 'start' not in kwargs.keys() and 'max_line' in kwargs.keys():
                    new_line = '' + ''.join(args)
                    return old_function(line_breaker(new_line, kwargs['max_line']))
                else:
                    new_line = '' + ''.join(args)
                    return old_function(new_line)
            else:
                print('in_file type is bool thus can be True/False only.'
                      'Please restart the program and provide a valid value.')
        else:
            if 'start' in kwargs.keys() and 'max_line' in kwargs.keys():
                new_line = kwargs['start'] + ''.join(args)
                return old_function(line_breaker(new_line, kwargs['max_line']))
            elif 'start' in kwargs.keys() and 'max_line' not in kwargs.keys():
                new_line = kwargs['start'] + ''.join(args)
                return old_function(new_line)
            elif 'start' not in kwargs.keys() and 'max_line' in kwargs.keys():
                new_line = '' + ''.join(args)
                return old_function(line_breaker(new_line, kwargs['max_line']))
            else:
                new_line = '' + ''.join(args)
                return old_function(new_line)
    return new_function


if __name__ == '__main__':
    adv_print = print_decorator(print)
    adv_print('YEET', in_file=True, start='start', maxline=3)
