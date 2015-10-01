## CodeEval
## Reverse and Add

import sys


def reverse_digits(n):
    res = 0
    while 0 < n:
        d = n % 10
        n = (n - d) / 10
        res = res*10 + d
    return res

f = open(sys.argv[1], 'r')

for n in f:

    n = int(n)
    rev = reverse_digits(n)
    cnt = 0
    while n != rev:
        n   += rev
        rev = reverse_digits(n)
        cnt += 1
    sys.stdout.write(str(cnt) + ' ' + str(n) + '\n')


f.close()
