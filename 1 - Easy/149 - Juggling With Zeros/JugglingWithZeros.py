## CodeEval
## Juggline with Zeros

import sys

f = open(sys.argv[1], 'r')

for n in f:

    n = n.strip()
    if n:
        n = n.split(' ')
        size = len(n)/2
        bina = []
        for i in xrange(size):
            if  '0' == n[2*i]:
                bina = bina + [0]*len(n[2*i+1])
            if '00' == n[2*i]:
                bina = bina + [1]*len(n[2*i+1])
        size = len(bina)
        out = 0
        for i in xrange(size):
            if bina[i]:
                out += 2**(size-i-1)
        sys.stdout.write(str(out) + '\n')


f.close()
