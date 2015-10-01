## CodeEval
## Max Range Sum

import sys

f = open(sys.argv[1], 'r')

for line in f:

    line = line.strip()
    if line:
        N, M = line.split(';')
        N = int(N)
        M = [int(m) for m in M.split(' ')]

        out = 0
        for i in xrange(len(M) - N + 1):
            out = max(sum(M[i:i+N]), out)
        sys.stdout.write(str(out) + '\n')


f.close()
