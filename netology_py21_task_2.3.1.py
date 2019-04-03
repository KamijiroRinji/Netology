# https://www.hackerrank.com/challenges/py-if-else/submissions/code/93865501

n = int(raw_input())

if n % 2 == 0 and (n in range(2,5) or n > 20):
    print('Not Weird')
elif n % 2 == 1 or (n % 2 == 0 and n in range(6,21)):
    print ('Weird')
