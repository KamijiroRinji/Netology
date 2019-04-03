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

files = []

with my_open('myfile.txt') as new_file:
  for number in range(10000000):
    files.append(new_file)
