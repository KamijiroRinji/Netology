import datetime


def decorator(old_function):
    def new_function(*args, **kwargs):
        start = datetime.datetime.now()
        the_function_call = old_function(*args, **kwargs)
        print(f'At {start} function {old_function.__name__} was called '
              f'with args ({args}, {kwargs}) and return value {the_function_call}')
        return the_function_call
    return new_function
