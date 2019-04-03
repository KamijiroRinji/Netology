from contextlib import contextmanager

@contextmanager
def my_open(file_path):
  start_time = datetime.datetime.now()
  print('Start time is', start_time)
  try:
    file = open(file_path)
    yield file
  finally:
    end_time = datetime.datetime.now()
    print('End time is', end_time)
    print('Elapsed time is', end_time - start_time)
    file.close()
