import datetime


def logger(path):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            start = datetime.datetime.now()
            the_function_call = old_function(*args, **kwargs)
            with open(path, 'a') as log_file:
                log_file.write(f'At {start} function {old_function.__name__} was called '
                               f'with args ({args}, {kwargs}) and return value {the_function_call}\n')
            return the_function_call
        return new_function
    return decorator
