## CodeEval
## Number of Ones

import sys

f = open(sys.argv[1], 'r')

for n in f:

    n = int(n)
    out = 0
    while 0 < n:
        d = n % 2
        n = (n - d)/2
        out += d
    sys.stdout.write(str(out) + '\n')


f.close()
