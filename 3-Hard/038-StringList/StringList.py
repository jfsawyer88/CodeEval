## CodeEval
## String List

import sys


def next_n(n, b):
    if n[-1] < b-1:
        return n[:-1] + [n[-1]+1]
    else:
        return next_n(n[:-1], b) + [0]


f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(',')
        size = int(line[0])
        alpha = ''.join(sorted(set(line[1])))

        b = len(alpha)        
        n = [0] * size
        sys.stdout.write(''.join([alpha[i] for i in n]))
        for i in xrange(1, b**size):
            n = next_n(n, b)
            sys.stdout.write(',' + ''.join([alpha[i] for i in n]))
        sys.stdout.write('\n')


f.close()
