## CodeEval
## Pascal's Triangle

import sys

f = open(sys.argv[1], 'r')

for n in f:

    n = n.strip()
    if n:
        n = int(n)
        if n == 1:
            sys.stdout.write('1\n')
        elif n == 2:
            sys.stdout.write('1 1 1\n')
        else:
            sys.stdout.write('1 1 1')
            line = [1,1,1]
            i = 3
            while i <= n:
                line = [1] + [line[j] + line[j-1] for j in xrange(1, i-1)] + [1]
                sys.stdout.write(' ' + ' '.join([str(s) for s in line]))
                i += 1
            sys.stdout.write('\n')


f.close()
