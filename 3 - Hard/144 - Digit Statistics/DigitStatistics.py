## CodeEval
## Digit Statistics
## idiot naive approach
## problem details indicate that
## n can be up to 1e12 and
## a is in range(1,10)

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        line = line.split(' ')
        a = int(line[0])
        n = int(line[1])

        curr = 1
        out = {i:0 for i in xrange(10)}
        for i in xrange(n):
            curr = (curr*a) % 10
            out[curr] += 1

        sys.stdout.write(', '.join([str(n) + ': ' + str(out[n]) for n in out]) + '\n')


f.close()
