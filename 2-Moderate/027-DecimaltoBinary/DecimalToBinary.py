## CodeEval
## Decimal to Binary

import sys

f = open(sys.argv[1], 'r')

for n in f:

    n = int(n)
    out = ''
    if 0 == n:
        out = '0'
    while 0 < n:
        d = n % 2
        n = (n - d)/2
        out = str(d) + out
    sys.stdout.write(out + '\n')


f.close()
